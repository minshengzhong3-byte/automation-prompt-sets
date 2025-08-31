#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
GitHub提示词集自动同步工具
根据user_rules.yaml配置自动从GitHub拉取提示词集
"""

import os
import yaml
import subprocess
import requests
import shutil
import logging
from pathlib import Path
from typing import Dict, List, Optional
from datetime import datetime

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('git_prompt_sync.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class GitPromptSync:
    """GitHub提示词集同步器"""
    
    def __init__(self, config_path: str = "user_rules.yaml"):
        """初始化同步器"""
        self.config_path = config_path
        self.config = self._load_config()
        self.github_config = self.config.get('git_prompt_collection', {})
        self.repo_config = self.github_config.get('github_repository', {})
        
    def _load_config(self) -> Dict:
        """加载配置文件"""
        try:
            with open(self.config_path, 'r', encoding='utf-8') as f:
                return yaml.safe_load(f)
        except Exception as e:
            logger.error(f"加载配置文件失败: {e}")
            raise
    
    def sync_all_prompts(self) -> bool:
        """同步所有提示词集"""
        logger.info("开始同步GitHub提示词集...")
        
        target_mapping = self.github_config.get('target_mapping', [])
        success_count = 0
        total_count = len(target_mapping)
        
        for mapping in target_mapping:
            github_path = mapping.get('github_path')
            local_path = mapping.get('local_path')
            priority = mapping.get('priority', 'medium')
            
            if not github_path or not local_path:
                logger.warning("跳过无效的映射配置")
                continue
            
            logger.info(f"同步 {github_path} -> {local_path} (优先级: {priority})")
            
            if self._sync_directory(github_path, local_path):
                success_count += 1
            else:
                logger.error(f"同步失败: {github_path}")
        
        success_rate = (success_count / total_count) * 100 if total_count > 0 else 0
        logger.info(f"同步完成: {success_count}/{total_count} ({success_rate:.1f}%)")
        
        return success_count == total_count
    
    def _sync_directory(self, github_path: str, local_path: str) -> bool:
        """同步单个目录"""
        try:
            # 确保本地目录存在
            os.makedirs(local_path, exist_ok=True)
            
            # 尝试使用git clone/pull
            if self._try_git_sync(github_path, local_path):
                return True
            
            # 如果git失败，使用curl下载
            if self._try_curl_download(github_path, local_path):
                return True
            
            logger.error(f"所有同步方法都失败: {github_path}")
            return False
            
        except Exception as e:
            logger.error(f"同步目录失败 {github_path}: {e}")
            return False
    
    def _try_git_sync(self, github_path: str, local_path: str) -> bool:
        """尝试使用git同步"""
        try:
            owner = self.repo_config.get('owner')
            repo = self.repo_config.get('repo')
            branch = self.repo_config.get('branch', 'main')
            
            github_url = f"https://github.com/{owner}/{repo}.git"
            
            # 检查是否已经是git仓库
            if os.path.exists(os.path.join(local_path, '.git')):
                # 执行git pull
                cmd = ["git", "pull", "origin", branch]
                result = subprocess.run(cmd, cwd=local_path, capture_output=True, text=True)
                if result.returncode == 0:
                    logger.info(f"Git pull成功: {github_path}")
                    return True
                else:
                    logger.warning(f"Git pull失败: {result.stderr}")
                    return False
            else:
                # 克隆特定目录
                cmd = [
                    "git", "clone", 
                    "--filter=tree:0",
                    "--sparse",
                    "--depth", "1",
                    "--branch", branch,
                    github_url,
                    local_path
                ]
                
                result = subprocess.run(cmd, capture_output=True, text=True)
                if result.returncode == 0:
                    # 切换到特定目录
                    cmd = ["git", "sparse-checkout", "set", github_path]
                    result = subprocess.run(cmd, cwd=local_path, capture_output=True, text=True)
                    if result.returncode == 0:
                        logger.info(f"Git clone成功: {github_path}")
                        return True
                    else:
                        logger.warning(f"Git sparse-checkout失败: {result.stderr}")
                        return False
                else:
                    logger.warning(f"Git clone失败: {result.stderr}")
                    return False
                    
        except Exception as e:
            logger.warning(f"Git同步失败: {e}")
            return False
    
    def _try_curl_download(self, github_path: str, local_path: str) -> bool:
        """使用curl下载文件"""
        try:
            base_url = self.repo_config.get('base_url')
            if not base_url:
                logger.warning("缺少base_url配置")
                return False
            
            # 获取目录文件列表
            api_url = f"https://api.github.com/repos/{self.repo_config['owner']}/{self.repo_config['repo']}/contents/{github_path}"
            
            response = requests.get(api_url)
            if response.status_code != 200:
                logger.warning(f"获取文件列表失败: {response.status_code}")
                return False
            
            files = response.json()
            if not isinstance(files, list):
                logger.warning("无效的API响应")
                return False
            
            success_count = 0
            total_count = 0
            
            for file_info in files:
                if file_info['type'] == 'file':
                    total_count += 1
                    file_name = file_info['name']
                    download_url = file_info['download_url']
                    local_file_path = os.path.join(local_path, file_name)
                    
                    # 下载文件
                    file_response = requests.get(download_url)
                    if file_response.status_code == 200:
                        with open(local_file_path, 'wb') as f:
                            f.write(file_response.content)
                        success_count += 1
                        logger.info(f"下载成功: {file_name}")
                    else:
                        logger.warning(f"下载失败: {file_name}")
            
            success_rate = (success_count / total_count) * 100 if total_count > 0 else 0
            logger.info(f"CURL下载完成: {success_count}/{total_count} ({success_rate:.1f}%)")
            
            return success_count > 0
            
        except Exception as e:
            logger.warning(f"CURL下载失败: {e}")
            return False
    
    def validate_sync(self) -> Dict:
        """验证同步结果"""
        validation_config = self.github_config.get('validation', {})
        target_mapping = self.github_config.get('target_mapping', [])
        
        results = {
            'total_directories': len(target_mapping),
            'validated_directories': 0,
            'missing_files': [],
            'invalid_files': [],
            'successful_validations': 0
        }
        
        for mapping in target_mapping:
            local_path = mapping.get('local_path')
            if not local_path or not os.path.exists(local_path):
                results['missing_files'].append(local_path)
                continue
            
            # 检查文件数量
            files = list(Path(local_path).rglob('*'))
            file_count = len([f for f in files if f.is_file()])
            
            if file_count < validation_config.get('min_file_count', 0):
                results['invalid_files'].append({
                    'path': local_path,
                    'reason': f'文件数量不足: {file_count}'
                })
                continue
            
            # 检查必需文件
            required_files = validation_config.get('required_files', [])
            missing_required = []
            
            for req_file in required_files:
                req_path = os.path.join(local_path, req_file)
                if not os.path.exists(req_path):
                    missing_required.append(req_file)
            
            if missing_required:
                results['invalid_files'].append({
                    'path': local_path,
                    'reason': f'缺少必需文件: {missing_required}'
                })
                continue
            
            results['validated_directories'] += 1
            results['successful_validations'] += 1
        
        return results
    
    def generate_report(self) -> str:
        """生成同步报告"""
        validation_results = self.validate_sync()
        
        report = f"""
# GitHub提示词集同步报告

## 基本信息
- 同步时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
- 配置文件: {self.config_path}
- GitHub仓库: {self.repo_config.get('owner')}/{self.repo_config.get('repo')}

## 同步统计
- 总目录数: {validation_results['total_directories']}
- 验证通过目录: {validation_results['validated_directories']}
- 成功验证数: {validation_results['successful_validations']}

## 问题详情
"""
        
        if validation_results['missing_files']:
            report += "\n### 缺失目录\n"
            for missing in validation_results['missing_files']:
                report += f"- {missing}\n"
        
        if validation_results['invalid_files']:
            report += "\n### 无效目录\n"
            for invalid in validation_results['invalid_files']:
                report += f"- {invalid['path']}: {invalid['reason']}\n"
        
        return report

def main():
    """主函数"""
    try:
        sync = GitPromptSync()
        
        # 执行同步
        success = sync.sync_all_prompts()
        
        # 生成报告
        report = sync.generate_report()
        print(report)
        
        # 保存报告
        with open('sync_report.md', 'w', encoding='utf-8') as f:
            f.write(report)
        
        if success:
            logger.info("同步任务完成")
            return 0
        else:
            logger.warning("同步任务部分失败")
            return 1
            
    except Exception as e:
        logger.error(f"同步任务失败: {e}")
        return 2

if __name__ == "__main__":
    exit(main())