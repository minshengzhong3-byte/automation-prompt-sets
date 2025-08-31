# GitHub提示词集同步功能使用指南

## 📖 概述

本指南详细介绍了如何配置和使用GitHub提示词集自动同步功能。该功能允许您从GitHub仓库自动拉取最新的提示词集，确保您的开发环境始终使用最新的提示词。

## 🚀 快速开始

### 1. 安装依赖
确保您的系统已安装以下依赖：
- Python 3.6+
- Git
- pip (Python包管理器)

### 2. 一键安装依赖
运行以下命令自动安装所需Python包：
```bash
pip install pyyaml requests
```

### 3. 配置GitHub仓库
编辑 `user_rules.yaml` 文件，修改GitHub仓库配置：

```yaml
git_prompt_collection:
  github_repository:
    owner: "your-actual-username"     # 修改为您的GitHub用户名
    repo: "your-actual-repo"          # 修改为您的仓库名
    branch: "main"                    # 分支名称
    base_url: "https://github.com/your-actual-username/your-actual-repo"
```

### 4. 运行同步
使用以下任一方法进行同步：

#### 方法一：一键同步（推荐）
```bash
sync_prompts.bat
```

#### 方法二：Python脚本
```bash
python git_prompt_sync.py
```

## ⚙️ 详细配置说明

### GitHub仓库配置
```yaml
git_prompt_collection:
  github_repository:
    owner: "your-username"           # GitHub用户名或组织名
    repo: "repository-name"         # 仓库名称
    branch: "main"                   # 分支名称（默认：main）
    base_url: "https://github.com/your-username/repository-name"
```

### 目录映射配置
```yaml
target_mapping:
  - github_path: "prompt_sets/program_development"
    local_path: ".trae/rules/prompt_sets/program_development"
    priority: "high"                # 优先级：high/medium/low
  
  - github_path: "prompt_sets/web_development"
    local_path: ".trae/rules/prompt_sets/web_development"
    priority: "medium"
  
  - github_path: "prompt_sets/tool_development"
    local_path: ".trae/rules/prompt_sets/tool_development"
    priority: "medium"
  
  - github_path: "prompt_sets/core"
    local_path: ".trae/rules/prompt_sets/core"
    priority: "high"
  
  - github_path: "prompt_sets/identities"
    local_path: ".trae/rules/prompt_sets/identities"
    priority: "high"
```

### 同步策略配置
```yaml
pull_strategy:
  primary_method: "git_clone_or_pull"  # 首选方法：git克隆或拉取
  fallback_method: "curl_download"    # 备用方法：HTTP下载
  retry_count: 3                       # 重试次数
  timeout_seconds: 300                # 超时时间（秒）
```

### 文件过滤规则
```yaml
file_filter:
  include_patterns: ["*.md", "*.yaml", "*.yml", "*.json"]  # 包含的文件类型
  exclude_patterns: ["*.tmp", "*.bak", "*.log"]            # 排除的文件类型
  max_file_size_mb: 10                                       # 最大文件大小（MB）
```

### 验证配置
```yaml
validation:
  required_files: ["framework.md"]  # 必需文件列表
  min_file_count: 3                  # 最小文件数量
  checksum_validation: true         # 是否启用校验和验证
```

### 监控配置
```yaml
monitoring:
  enable: true                      # 启用监控
  check_interval_hours: 24         # 检查间隔（小时）
  notify_on_failure: true          # 失败时通知
  log_level: "info"                # 日志级别：debug/info/warning/error
```

## 🔧 高级功能

### 1. 自定义目录映射
您可以添加任意数量的目录映射：
```yaml
target_mapping:
  - github_path: "your/custom/path"
    local_path: "your/local/path"
    priority: "high"
```

### 2. 多仓库支持
通过创建多个配置节支持多个GitHub仓库：
```yaml
# 主仓库
git_prompt_collection:
  github_repository:
    owner: "main-owner"
    repo: "main-repo"
  # ... 其他配置

# 备用仓库  
git_prompt_collection_backup:
  github_repository:
    owner: "backup-owner"
    repo: "backup-repo"
  # ... 其他配置
```

### 3. 条件同步
基于条件决定是否同步：
```yaml
conditional_sync:
  enabled: true
  conditions:
    - "file_age_hours > 24"    # 文件超过24小时未更新
    - "network_available"      # 网络可用
    - "disk_space_gb > 1"     # 磁盘空间大于1GB
```

## 🛠️ 集成到开发流程

### 项目初始化脚本
```bash
#!/bin/bash
# init_project.sh

echo "正在初始化项目..."

# 同步提示词集
echo "同步GitHub提示词集..."
python git_prompt_sync.py

# 验证同步结果
if [ $? -eq 0 ]; then
    echo "提示词集同步成功"
else
    echo "提示词集同步失败，使用本地缓存"
fi

echo "项目初始化完成"
```

### CI/CD集成示例
```yaml
# GitHub Actions
ame: Sync Prompt Sets
on:
  schedule:
    - cron: '0 0 * * *'  # 每天午夜运行
  workflow_dispatch:     # 手动触发

jobs:
  sync-prompts:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v3
        
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.9'
          
      - name: Install dependencies
        run: pip install pyyaml requests
        
      - name: Sync prompt sets
        run: python git_prompt_sync.py
        
      - name: Upload sync report
        uses: actions/upload-artifact@v3
        with:
          name: sync-report
          path: sync_report.md
```

### Docker集成
```dockerfile
FROM python:3.9-slim

# 安装依赖
RUN pip install pyyaml requests

# 复制同步脚本
COPY git_prompt_sync.py .
COPY user_rules.yaml .

# 设置入口点
ENTRYPOINT ["python", "git_prompt_sync.py"]
```

## 🔍 故障排除

### 常见问题及解决方案

#### 1. 网络连接问题
```bash
# 测试GitHub连接
ping github.com

# 测试API访问
curl -I https://api.github.com
```

#### 2. 权限问题
```bash
# 检查文件权限
ls -la .trae/rules/prompt_sets/

# 修复权限
chmod -R 755 .trae/rules/
```

#### 3. 依赖问题
```bash
# 重新安装依赖
pip uninstall pyyaml requests
pip install pyyaml requests
```

#### 4. 配置错误
```bash
# 验证YAML语法
python -c "import yaml; yaml.safe_load(open('user_rules.yaml'))"

# 检查配置路径
ls -la .trae/rules/prompt_sets/
```

### 日志分析

查看详细日志：
```bash
# 查看实时日志
tail -f git_prompt_sync.log

# 搜索错误信息
grep -i error git_prompt_sync.log

# 查看同步统计
grep -i "同步完成" git_prompt_sync.log
```

### 性能优化

#### 1. 启用缓存
```yaml
caching:
  enabled: true
  cache_dir: "./cache"
  max_cache_size_mb: 100
  cleanup_interval_hours: 24
```

#### 2. 并行下载
```yaml
performance:
  parallel_downloads: 5
  connection_timeout: 30
  download_timeout: 60
```

#### 3. 增量同步
```yaml
incremental_sync:
  enabled: true
  check_modified_only: true
  preserve_local_changes: false
```

## 📊 监控和报告

### 同步报告
每次同步后生成 `sync_report.md`，包含：
- 同步时间统计
- 成功/失败目录列表
- 问题详情
- 性能指标
- 建议和改进措施

### 状态监控
```bash
# 查看最后一次同步状态
cat sync_report.md

# 检查同步频率
find . -name "sync_report.md" -mtime -1

# 监控磁盘使用
du -sh .trae/rules/prompt_sets/
```

### 告警配置
```yaml
alerting:
  enabled: true
  webhook_url: "https://your-webhook-url"
  notify_on:
    - "sync_failure"
    - "validation_error"
    - "performance_issue"
  min_severity: "warning"
```

## 🔄 自动化工作流

### 定期同步
使用cron定时任务：
```bash
# 每天凌晨2点同步
0 2 * * * cd /path/to/your/project && python git_prompt_sync.py

# 每周一凌晨3点同步
0 3 * * 1 cd /path/to/your/project && python git_prompt_sync.py
```

### 事件触发同步
```bash
# 项目启动时同步
./sync_prompts.bat

# 代码变更时同步
git pull && python git_prompt_sync.py

# 手动触发同步
python git_prompt_sync.py --force
```

### 回滚机制
```bash
# 备份当前提示词集
cp -r .trae/rules/prompt_sets/ .trae/rules/prompt_sets_backup_$(date +%Y%m%d_%H%M%S)

# 恢复备份
cp -r .trae/rules/prompt_sets_backup_20230801_120000/ .trae/rules/prompt_sets/
```

## 🎯 最佳实践

1. **定期更新** - 设置每天自动同步，确保提示词最新
2. **版本控制** - 对本地修改的提示词进行版本管理
3. **备份策略** - 定期备份重要的提示词集
4. **监控告警** - 设置同步失败告警
5. **性能优化** - 根据网络状况调整超时和重试参数
6. **安全考虑** - 使用HTTPS和验证下载文件的完整性

## 📝 更新日志

### v1.0.0 (2024-01-01)
- 初始版本发布
- 支持Git和HTTP两种同步方式
- 完整的验证和监控功能
- 详细的报告生成

## 🤝 贡献指南

欢迎提交Issue和Pull Request来改进这个功能！

## 📞 支持

如果您遇到问题，请：
1. 查看 `git_prompt_sync.log` 日志文件
2. 检查 `sync_report.md` 同步报告
3. 提交Issue到GitHub仓库

---

**最后更新:** 2024-01-01  
**版本:** 1.0.0  
**状态:** 正式发布