#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
GitHub提示词集同步功能测试脚本
"""

import os
import tempfile
import shutil
from pathlib import Path

def test_config_loading():
    """测试配置文件加载"""
    print("=== 测试配置文件加载 ===")
    
    try:
        from git_prompt_sync import GitPromptSync
        sync = GitPromptSync()
        
        # 检查基本配置
        assert sync.config is not None, "配置文件加载失败"
        assert 'git_prompt_collection' in sync.config, "缺少git_prompt_collection配置"
        assert 'github_repository' in sync.config['git_prompt_collection'], "缺少github_repository配置"
        
        repo_config = sync.config['git_prompt_collection']['github_repository']
        assert 'owner' in repo_config, "缺少owner配置"
        assert 'repo' in repo_config, "缺少repo配置"
        
        print("✅ 配置文件加载测试通过")
        return True
        
    except Exception as e:
        print(f"❌ 配置文件加载测试失败: {e}")
        return False

def test_directory_mapping():
    """测试目录映射配置"""
    print("\n=== 测试目录映射配置 ===")
    
    try:
        from git_prompt_sync import GitPromptSync
        sync = GitPromptSync()
        
        target_mapping = sync.config['git_prompt_collection'].get('target_mapping', [])
        assert len(target_mapping) > 0, "缺少target_mapping配置"
        
        for mapping in target_mapping:
            assert 'github_path' in mapping, "映射配置缺少github_path"
            assert 'local_path' in mapping, "映射配置缺少local_path"
            assert 'priority' in mapping, "映射配置缺少priority"
        
        print("✅ 目录映射配置测试通过")
        return True
        
    except Exception as e:
        print(f"❌ 目录映射配置测试失败: {e}")
        return False

def test_validation_config():
    """测试验证配置"""
    print("\n=== 测试验证配置 ===")
    
    try:
        from git_prompt_sync import GitPromptSync
        sync = GitPromptSync()
        
        validation_config = sync.config['git_prompt_collection'].get('validation', {})
        assert 'required_files' in validation_config, "缺少required_files配置"
        assert 'min_file_count' in validation_config, "缺少min_file_count配置"
        
        print("✅ 验证配置测试通过")
        return True
        
    except Exception as e:
        print(f"❌ 验证配置测试失败: {e}")
        return False

def test_sync_class_initialization():
    """测试同步类初始化"""
    print("\n=== 测试同步类初始化 ===")
    
    try:
        from git_prompt_sync import GitPromptSync
        
        # 使用临时配置文件测试
        with tempfile.NamedTemporaryFile(mode='w', suffix='.yaml', delete=False) as f:
            f.write("""
git_prompt_collection:
  github_repository:
    owner: "test-owner"
    repo: "test-repo"
    branch: "main"
    base_url: "https://github.com/test-owner/test-repo"
  
  target_mapping:
    - github_path: "prompt_sets/test"
      local_path: "test_local"
      priority: "high"
  
  validation:
    required_files: ["test.md"]
    min_file_count: 1
""")
            temp_config = f.name
        
        sync = GitPromptSync(temp_config)
        
        assert sync.config is not None
        assert sync.github_config is not None
        assert sync.repo_config is not None
        assert sync.repo_config['owner'] == 'test-owner'
        assert sync.repo_config['repo'] == 'test-repo'
        
        # 清理临时文件
        os.unlink(temp_config)
        
        print("✅ 同步类初始化测试通过")
        return True
        
    except Exception as e:
        print(f"❌ 同步类初始化测试失败: {e}")
        if 'temp_config' in locals() and os.path.exists(temp_config):
            os.unlink(temp_config)
        return False

def test_validation_logic():
    """测试验证逻辑"""
    print("\n=== 测试验证逻辑 ===")
    
    try:
        from git_prompt_sync import GitPromptSync
        
        # 创建临时目录和测试文件
        with tempfile.TemporaryDirectory() as temp_dir:
            test_dir = os.path.join(temp_dir, 'test_prompts')
            os.makedirs(test_dir)
            
            # 创建测试文件
            with open(os.path.join(test_dir, 'framework.md'), 'w') as f:
                f.write("# Test Framework")
            with open(os.path.join(test_dir, 'test1.md'), 'w') as f:
                f.write("# Test File 1")
            with open(os.path.join(test_dir, 'test2.md'), 'w') as f:
                f.write("# Test File 2")
            
            # 使用临时配置文件
            with tempfile.NamedTemporaryFile(mode='w', suffix='.yaml', delete=False, encoding='utf-8') as f:
                # 使用原始字符串避免转义问题
                config_content = f'''git_prompt_collection:
  github_repository:
    owner: "test"
    repo: "test"
  
  target_mapping:
    - github_path: "test"
      local_path: "{test_dir.replace(os.sep, '/')}"
      priority: "high"
  
  validation:
    required_files: ["framework.md"]
    min_file_count: 2
'''
                f.write(config_content)
                temp_config = f.name
            
            sync = GitPromptSync(temp_config)
            results = sync.validate_sync()
            
            assert results['total_directories'] == 1
            assert results['validated_directories'] == 1
            assert results['successful_validations'] == 1
            assert len(results['missing_files']) == 0
            assert len(results['invalid_files']) == 0
            
            # 清理
            os.unlink(temp_config)
            
        print("✅ 验证逻辑测试通过")
        return True
        
    except Exception as e:
        print(f"❌ 验证逻辑测试失败: {e}")
        if 'temp_config' in locals() and os.path.exists(temp_config):
            os.unlink(temp_config)
        return False

def main():
    """主测试函数"""
    print("开始测试GitHub提示词集同步功能...\n")
    
    tests = [
        test_config_loading,
        test_directory_mapping,
        test_validation_config,
        test_sync_class_initialization,
        test_validation_logic
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        if test():
            passed += 1
    
    print(f"\n=== 测试结果 ===")
    print(f"通过: {passed}/{total}")
    
    if passed == total:
        print("🎉 所有测试通过！")
        print("\n下一步操作:")
        print("1. 修改 user_rules.yaml 中的GitHub仓库配置")
        print("2. 运行 sync_prompts.bat 进行实际同步")
        print("3. 查看 sync_report.md 获取同步报告")
        return 0
    else:
        print("❌ 部分测试失败，请检查配置")
        return 1

if __name__ == "__main__":
    exit(main())