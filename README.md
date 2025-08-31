# IDE自动化编程提示词集系统

## 📖 概述

这是一个专为IDE环境设计的自动化编程提示词集系统，支持多种开发类型和完整的开发流程。系统通过智能提示词采集和身份切换机制，为AI编程助手提供精准的上下文指导。

## 🏗️ 系统架构

### 开发类型支持
- **程序开发 (Program Development)** - 通用软件开发项目
- **网站开发 (Web Development)** - Web应用和网站建设  
- **工具开发 (Tool Development)** - 开发工具和实用程序

### 开发阶段
每个开发类型都包含四个标准阶段：
1. **需求分析 (Requirements Analysis)** - 收集和分析项目需求
2. **计划 (Planning)** - 制定项目计划和架构设计
3. **开发 (Development)** - 编写和实现代码
4. **测试 (Testing)** - 验证代码功能和性能

## 📁 文件结构

```
trae_rules/
├── prompt_sets/                 # 提示词集目录
│   ├── core/                    # 核心基础提示词
│   ├── identities/              # 身份专属提示词
│   ├── program_development/     # 程序开发提示词
│   │   ├── framework.md        # 框架定义
│   │   ├── requirements_analysis.md
│   │   ├── planning.md
│   │   ├── development.md
│   │   └── testing.md
│   ├── web_development/        # 网站开发提示词
│   └── tool_development/       # 工具开发提示词
├── project_rules.md            # 动态规则文件
└── last_status.json           # 状态备份

user_rules.yaml                # 用户配置规则
```

## ⚙️ 配置说明

### user_rules.yaml 核心配置

#### 1. 提示词采集规则
```yaml
prompt_collection:
  target_directories:
    - "trae_rules/prompt_sets/core/"
    - "trae_rules/prompt_sets/identities/"
    - "trae_rules/prompt_sets/program_development/"
    - "trae_rules/prompt_sets/web_development/"
    - "trae_rules/prompt_sets/tool_development/"
```

#### 2. 开发类型定义
```yaml
development_types:
  program_development:
    description: "程序开发 - 通用软件开发项目"
    stages: ["requirements_analysis", "planning", "development", "testing"]
    default_identity: "developer"
```

#### 3. 身份管理
支持五种专业身份：
- **代码分析师 (Code Analyst)** - 分析代码结构和逻辑
- **架构师 (Architect)** - 设计解决方案和架构  
- **代码审查员 (Code Reviewer)** - 执行代码审查和静态分析
- **开发者 (Developer)** - 编写和修改代码
- **测试员 (QA Tester)** - 验证代码功能和稳定性

## 🚀 使用流程

### 1. 初始化系统
系统自动扫描提示词集目录，加载核心基础规则。

### 2. 选择开发类型
根据项目类型选择相应的开发路径：
- 程序开发 → `program_development`
- 网站建设 → `web_development`  
- 工具开发 → `tool_development`

### 3. 按阶段推进
每个开发类型都遵循标准阶段流程：
1. **需求分析阶段** → 架构师身份
2. **计划阶段** → 架构师身份  
3. **开发阶段** → 开发者身份
4. **测试阶段** → 测试员身份

### 4. 智能提示词采集
系统根据当前阶段和身份自动采集相关提示词：
- 核心基础提示词
- 身份专属提示词  
- 开发类型提示词
- 阶段特定提示词

### 5. 动态规则更新
采集的提示词自动合并到 `project_rules.md`，为AI编程助手提供实时指导。

## 🔧 IDE集成特性

### 开发环境功能
- ✅ 代码自动生成
- ✅ 智能代码补全  
- ✅ 实时语法验证
- ✅ 集成调试支持

### 测试环境功能  
- ✅ 测试用例生成
- ✅ 自动化测试执行
- ✅ 代码覆盖率分析
- ✅ 性能监控

### 部署功能
- ✅ 构建自动化
- ✅ 依赖管理  
- ✅ 容器化支持
- ✅ 云平台集成

## 📊 质量保障

### 代码规范
- 命名规范检查
- 代码格式化
- 文档要求
- 错误处理规范

### 开发流程
- 版本控制集成
- 代码审查流程  
- 持续集成
- 自动化测试

### 质量指标
- 静态代码分析
- 安全漏洞扫描  
- 性能测试
- 可访问性测试

## 🔄 工作流程示例

### 程序开发项目
```
1. 选择开发类型: program_development
2. 阶段: requirements_analysis → 身份: architect
3. 采集: core + architect + program_development + requirements_analysis
4. 阶段: planning → 身份: architect  
5. 采集: core + architect + program_development + planning
6. 阶段: development → 身份: developer
7. 采集: core + developer + program_development + development
8. 阶段: testing → 身份: qa_tester
9. 采集: core + qa_tester + program_development + testing
```

### 网站开发项目
```
1. 选择开发类型: web_development
2. 阶段: requirements_analysis → 身份: architect
3. 采集: core + architect + web_development + requirements_analysis
4. 阶段: planning → 身份: architect
5. 采集: core + architect + web_development + planning  
6. 阶段: development → 身份: developer
7. 采集: core + developer + web_development + development
8. 阶段: testing → 身份: qa_tester
9. 采集: core + qa_tester + web_development + testing
```

## 📝 自定义扩展

### 添加新的开发类型
1. 在 `trae_rules/prompt_sets/` 创建新目录
2. 创建相应的阶段文件:
   - `framework.md` - 框架定义
   - `requirements_analysis.md` - 需求分析
   - `planning.md` - 计划阶段
   - `development.md` - 开发阶段  
   - `testing.md` - 测试阶段

3. 在 `user_rules.yaml` 中添加开发类型配置

### 修改阶段流程
在 `user_rules.yaml` 的 `stages` 部分调整阶段定义和身份映射。

## 🎯 最佳实践

1. **保持提示词简洁** - 每个提示词文件专注于特定领域
2. **遵循命名规范** - 使用一致的命名约定
3. **定期更新** - 根据技术发展更新提示词内容  
4. **测试验证** - 确保提示词在实际项目中有效
5. **文档完善** - 为每个提示词提供清晰的说明和示例

## 🔍 故障排除

### 常见问题

1. **提示词未加载**
   - 检查 `user_rules.yaml` 中的目录配置
   - 验证文件路径是否正确

## 🌐 GitHub提示词集同步功能

### 自动同步功能
系统支持从GitHub仓库自动拉取提示词集，确保提示词始终保持最新状态。

### 使用方法

#### 1. 一键同步
运行批处理文件自动同步所有配置的提示词集：
```bash
sync_prompts.bat
```

#### 2. 手动同步
使用Python脚本进行更精细的控制：
```bash
python git_prompt_sync.py
```

### 配置说明
在 `user_rules.yaml` 中配置GitHub同步规则：

```yaml
git_prompt_collection:
  github_repository:
    owner: "your-username"
    repo: "automated-prompt-sets"
    branch: "main"
    base_url: "https://github.com/your-username/automated-prompt-sets"
  
  target_mapping:
    - github_path: "prompt_sets/program_development"
      local_path: "trae_rules/prompt_sets/program_development"
      priority: "high"
    - github_path: "prompt_sets/web_development"
      local_path: "trae_rules/prompt_sets/web_development"
      priority: "medium"
    - github_path: "prompt_sets/tool_development"
      local_path: "trae_rules/prompt_sets/tool_development"
      priority: "medium"
    - github_path: "prompt_sets/core"
      local_path: "trae_rules/prompt_sets/core"
      priority: "high"
    - github_path: "prompt_sets/identities"
      local_path: "trae_rules/prompt_sets/identities"
      priority: "high"

  pull_strategy:
    primary_method: "git_clone_or_pull"
    fallback_method: "curl_download"
    retry_count: 3
    timeout_seconds: 300

  file_filter:
    include_patterns: ["*.md", "*.yaml", "*.yml", "*.json"]
    exclude_patterns: ["*.tmp", "*.bak", "*.log"]
    max_file_size_mb: 10

  validation:
    required_files: ["framework.md"]
    min_file_count: 3
    checksum_validation: true

  monitoring:
    enable: true
    check_interval_hours: 24
    notify_on_failure: true
    log_level: "info"
```

### 同步策略

#### Git同步 (首选)
- 使用 `git clone --sparse` 进行高效克隆
- 支持增量更新和分支切换
- 自动处理.gitignore规则

#### CURL下载 (备用)
- 当Git不可用时使用HTTP下载
- 支持大文件断点续传
- 自动重试机制

### 验证机制
同步完成后自动验证：
- 文件完整性检查
- 必需文件验证
- 文件数量检查
- 校验和验证

### 监控功能
- 定时检查更新
- 失败通知
- 详细日志记录
- 性能监控

### 报告生成
每次同步后生成详细报告：
- 同步时间统计
- 成功/失败目录列表
- 问题详情
- 性能指标

报告文件: `sync_report.md`

### 集成到开发流程

#### 项目初始化时
```bash
# 首次拉取所有提示词集
sync_prompts.bat
```

#### 日常开发中
```bash
# 定期检查更新
python git_prompt_sync.py
```

#### CI/CD集成
```yaml
# 在CI流水线中添加同步步骤
- name: Sync Prompt Sets
  run: python git_prompt_sync.py
```

### 故障排除

#### 同步失败
1. 检查网络连接
2. 验证GitHub仓库权限
3. 查看 `git_prompt_sync.log` 日志

#### 文件验证错误
1. 检查必需文件是否存在
2. 验证文件格式
3. 查看同步报告详情

#### 性能问题
1. 调整超时设置
2. 优化网络配置
3. 使用镜像仓库

2. **身份切换失败**  
   - 确认身份定义文件存在
   - 检查身份映射配置

3. **阶段推进异常**
   - 验证阶段定义配置
   - 检查阶段顺序是否正确

## 📞 支持

如有问题或建议，请参考：
- 查看 `user_rules.yaml` 配置说明
- 检查各提示词文件的格式规范
- 验证目录结构和文件权限

---
**版本:** 1.0.0  
**更新日期:** 2024-01-01  
**状态:** 生产就绪