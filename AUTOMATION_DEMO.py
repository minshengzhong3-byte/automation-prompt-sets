#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
IDE自动化编程完整流程演示
模拟各个阶段自动化动态更新project_rules和身份切换
"""

import os
import time
import json
import yaml
from pathlib import Path
from datetime import datetime

class AutomationDemo:
    """自动化流程演示类"""
    
    def __init__(self):
        self.current_stage = "requirements_analysis"
        self.current_identity = "architect"
        self.progress = 0
        self.project_rules_path = "trae_rules/project_rules.md"
        self.status_path = "trae_rules/last_status.json"
        
        # 阶段定义
        self.stages = [
            "requirements_analysis",
            "planning", 
            "development",
            "testing",
            "deployment",
            "documentation"
        ]
        
        # 身份映射
        self.identity_mapping = {
            "requirements_analysis": "architect",
            "planning": "architect",
            "development": "developer", 
            "testing": "qa_tester",
            "deployment": "architect",
            "documentation": "architect"
        }
        
        # 确保目录存在
        os.makedirs("trae_rules", exist_ok=True)
        os.makedirs("trae_rules/prompt_sets", exist_ok=True)
        os.makedirs("trae_rules/prompt_sets/core", exist_ok=True)
        os.makedirs("trae_rules/prompt_sets/identities", exist_ok=True)
        
    def initialize_prompt_sets(self):
        """初始化提示词集"""
        print("🔄 初始化提示词集...")
        
        # 创建核心基础提示词
        core_prompts = {
            "framework.md": "# 核心基础框架\n\n## 状态管理\n- 实时跟踪任务进度\n- 自动保存和恢复状态\n- 错误处理和重试机制\n\n## 流程控制\n- 阶段自动推进\n- 身份智能切换\n- 规则动态更新",
            "error_handling.md": "# 错误处理规则\n\n## 异常策略\n- 技术失败：重试3次\n- 提示词加载失败：使用备用提示词\n- 系统错误：保存状态，提供恢复"
        }
        
        for filename, content in core_prompts.items():
            with open(f"trae_rules/prompt_sets/core/{filename}", "w", encoding="utf-8") as f:
                f.write(content)
        
        # 创建身份提示词
        identity_prompts = {
            "architect.md": "# 架构师身份\n\n## 职责\n- 设计解决方案和架构\n- 制定技术规范\n- 评估技术风险\n\n## 技能要求\n- 系统设计能力\n- 技术决策能力\n- 风险评估能力",
            "developer.md": "# 开发者身份\n\n## 职责\n- 编写和修改代码\n- 实现功能模块\n- 代码调试和优化\n\n## 技能要求\n- 编程语言精通\n- 算法和数据结构\n- 调试和优化",
            "qa_tester.md": "# 测试员身份\n\n## 职责\n- 验证代码功能\n- 执行测试用例\n- 报告缺陷问题\n\n## 技能要求\n- 测试用例设计\n- 缺陷跟踪\n- 质量评估"
        }
        
        for filename, content in identity_prompts.items():
            with open(f"trae_rules/prompt_sets/identities/{filename}", "w", encoding="utf-8") as f:
                f.write(content)
        
        print("✅ 提示词集初始化完成")
    
    def update_project_rules(self):
        """更新project_rules.md"""
        print(f"📝 更新项目规则 - 阶段: {self.current_stage}, 身份: {self.current_identity}")
        
        # 读取当前提示词
        core_prompts = self._read_prompts("trae_rules/prompt_sets/core")
        identity_prompts = self._read_prompts(f"trae_rules/prompt_sets/identities")
        
        # 构建规则内容
        rules_content = f"""# 🚀 智能协调引擎 - 项目规则文件

## 📊 当前状态
- **模式:** program_development  
- **身份:** {self.current_identity}
- **阶段:** {self.current_stage}
- **进度:** {self.progress}%
- **任务:** {self._get_stage_description()}

## 🎯 已加载提示词

### 核心基础层
{self._format_prompts(core_prompts, 'core')}

### 身份专属层
{self._format_prompts(identity_prompts, 'identities')}

## 🔄 自动化流程

### 阶段进度
{self._generate_progress_bar()}

### 下一步行动
{self._get_next_action()}

## 📋 采集统计
- **总提示词文件:** {len(core_prompts) + len(identity_prompts)}
- **最后更新时间:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
- **运行状态:** 正常

---
**自动化引擎版本:** 1.0.0  
**最后更新:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
"""
        
        # 写入文件
        with open(self.project_rules_path, "w", encoding="utf-8") as f:
            f.write(rules_content)
        
        print("✅ 项目规则更新完成")
    
    def save_status(self):
        """保存当前状态"""
        status = {
            "current_stage": self.current_stage,
            "current_identity": self.current_identity,
            "progress": self.progress,
            "last_updated": datetime.now().isoformat(),
            "stages": self.stages,
            "identity_mapping": self.identity_mapping
        }
        
        with open(self.status_path, "w", encoding="utf-8") as f:
            json.dump(status, f, indent=2, ensure_ascii=False)
        
        print("💾 状态已保存")
    
    def load_status(self):
        """加载保存的状态"""
        if os.path.exists(self.status_path):
            with open(self.status_path, "r", encoding="utf-8") as f:
                status = json.load(f)
            
            self.current_stage = status.get("current_stage", "requirements_analysis")
            self.current_identity = status.get("current_identity", "architect")
            self.progress = status.get("progress", 0)
            
            print("📂 状态已加载")
            return True
        return False
    
    def switch_stage(self, next_stage):
        """切换到下一个阶段"""
        if next_stage in self.stages:
            print(f"🔄 切换阶段: {self.current_stage} → {next_stage}")
            self.current_stage = next_stage
            self.current_identity = self.identity_mapping.get(next_stage, "architect")
            self.update_project_rules()
            self.save_status()
            return True
        return False
    
    def simulate_work(self):
        """模拟工作进度"""
        stage_progress = {
            "requirements_analysis": 20,
            "planning": 40, 
            "development": 70,
            "testing": 90,
            "deployment": 95,
            "documentation": 100
        }
        
        self.progress = stage_progress.get(self.current_stage, 0)
        
        print(f"👨‍💻 模拟工作 - 阶段: {self.current_stage}")
        print(f"  身份: {self.current_identity}")
        print(f"  进度: {self.progress}%")
        
        # 模拟工作耗时
        time.sleep(2)
        
        self.update_project_rules()
        self.save_status()
    
    def run_complete_workflow(self):
        """运行完整的工作流程"""
        print("🎬 开始完整自动化流程演示")
        print("=" * 50)
        
        # 初始化
        self.initialize_prompt_sets()
        
        # 遍历所有阶段
        for stage in self.stages:
            print(f"\n📋 开始阶段: {stage}")
            print("-" * 30)
            
            # 切换到当前阶段
            self.switch_stage(stage)
            
            # 模拟工作
            self.simulate_work()
            
            # 显示当前规则状态
            self.show_current_status()
            
            print("-" * 30)
            time.sleep(1)
        
        print("\n🎉 自动化流程演示完成！")
        print("=" * 50)
    
    def show_current_status(self):
        """显示当前状态"""
        if os.path.exists(self.project_rules_path):
            with open(self.project_rules_path, "r", encoding="utf-8") as f:
                content = f.read()
            
            # 提取关键信息
            lines = content.split('\n')
            status_line = next((line for line in lines if '当前状态' in line), "")
            
            print(f"📊 当前状态: {status_line}")
    
    def _read_prompts(self, directory):
        """读取指定目录的提示词文件"""
        prompts = {}
        if os.path.exists(directory):
            for file in os.listdir(directory):
                if file.endswith('.md'):
                    with open(os.path.join(directory, file), "r", encoding="utf-8") as f:
                        prompts[file] = f.read()
        return prompts
    
    def _format_prompts(self, prompts, category):
        """格式化提示词显示"""
        if not prompts:
            return "- 暂无提示词"
        
        result = []
        for filename, content in prompts.items():
            # 提取第一行作为描述
            first_line = content.split('\n')[0] if content else "No description"
            result.append(f"- **{filename}**: {first_line}")
        
        return '\n'.join(result)
    
    def _get_stage_description(self):
        """获取阶段描述"""
        descriptions = {
            "requirements_analysis": "需求分析阶段，使用架构师身份收集和分析需求",
            "planning": "计划阶段，使用架构师身份制定项目计划",
            "development": "开发阶段，使用开发者身份编写代码",
            "testing": "测试阶段，使用测试员身份验证功能",
            "deployment": "部署阶段，使用架构师身份进行部署",
            "documentation": "文档阶段，使用架构师身份整理文档"
        }
        return descriptions.get(self.current_stage, "未知阶段")
    
    def _generate_progress_bar(self):
        """生成进度条"""
        total_width = 20
        filled_width = int(self.progress / 100 * total_width)
        bar = "█" * filled_width + "░" * (total_width - filled_width)
        return f"[{bar}] {self.progress}%"
    
    def _get_next_action(self):
        """获取下一步行动"""
        current_index = self.stages.index(self.current_stage) if self.current_stage in self.stages else -1
        
        if current_index < len(self.stages) - 1:
            next_stage = self.stages[current_index + 1]
            next_identity = self.identity_mapping.get(next_stage, "architect")
            return f"准备切换到 {next_stage} 阶段，身份将变为 {next_identity}"
        else:
            return "所有阶段已完成，任务结束"

def main():
    """主函数"""
    demo = AutomationDemo()
    
    # 尝试加载保存的状态
    if not demo.load_status():
        print("🆕 未找到保存的状态，开始新流程")
    
    # 运行完整流程
    demo.run_complete_workflow()
    
    # 显示最终结果
    print("\n📋 最终项目规则文件:")
    print("=" * 50)
    if os.path.exists(demo.project_rules_path):
        with open(demo.project_rules_path, "r", encoding="utf-8") as f:
            print(f.read())
    
    print("\n🎯 演示完成！您可以:")
    print("1. 查看 trae_rules/project_rules.md 了解动态规则")
    print("2. 查看 trae_rules/last_status.json 了解状态保存")
    print("3. 运行 python AUTOMATION_DEMO.py 再次演示")

if __name__ == "__main__":
    main()