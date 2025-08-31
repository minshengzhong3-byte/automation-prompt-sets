# 智能协调引擎 - 项目规则文件

## 🚀 核心配置

**当前状态:**
- 模式: program_development (基于对话识别)
- 身份: architect
- 进度: 0%
- 任务: 等待第一句对话触发需求分析阶段

## 📋 分层规则体系

### 1. 核心基础层 (继承所有模式)
- **位置:** `.trae/rules/prompt_sets/core/`
- **包含:** 状态管理、流程控制、异常处理

### 2. 研究类型层
- **Code Analysis:** `.trae/rules/prompt_sets/code_analysis/framework.md`
- **Static Review:** `.trae/rules/prompt_sets/static_review/framework.md`
- **Pattern Matching:** `.trae/rules/prompt_sets/pattern_matching/framework.md`
- **General:** `.trae/rules/prompt_sets/general_research/framework.md`

### 3. 阶段特定层
- **继承:** 核心基础 + 研究类型 + 阶段专属

## 👥 身份角色定义

| 身份角色 | 职责描述 | 提示词位置 |
|----------|----------|------------|
| **🔍 代码分析师** | 分析代码结构和逻辑 | `.trae/rules/prompt_sets/identities/code_analyst.md` |
| **🎯 架构师** | 设计解决方案和架构 | `.trae/rules/prompt_sets/identities/architect.md` |
| **🔧 代码审查员** | 执行代码审查和静态分析 | `.trae/rules/prompt_sets/identities/code_reviewer.md` |
| **💻 开发者** | 编写和修改代码 | `.trae/rules/prompt_sets/identities/developer.md` |
| **✅ 测试员** | 验证代码功能和稳定性 | `.trae/rules/prompt_sets/identities/qa_tester.md` |

## 🔄 身份切换机制

**切换流程:**
1. 检测身份切换事件
2. 扫描 `.trae/rules/prompt_sets/` 目录
3. 加载：核心基础 + 当前身份 + 当前路径 + 当前阶段
4. 合并到本规则文件
5. 更新状态日志

## 📥 提示词采集流程

**已加载提示词:**
- ✅ `core/framework.md` - 核心基础框架
- ✅ `core/error_handling.md` - 错误处理规则
- ✅ `identities/code_analyst.md` - 代码分析师身份
- ✅ `identities/architect.md` - 架构师身份
- ✅ `identities/developer.md` - 开发者身份
- ✅ `identities/code_reviewer.md` - 代码审查员身份
- ✅ `identities/qa_tester.md` - 测试员身份
- ✅ `identities/reverse_engineer.md` - 逆向工程师身份
- ✅ `code_analysis/framework.md` - 代码分析研究路径
- ✅ `pattern_matching/framework.md` - 模式匹配框架
- ✅ `program_development/requirements_analysis.md` - 程序开发需求分析
- ✅ `program_development/planning.md` - 程序开发计划
- ✅ `program_development/development.md` - 程序开发执行
- ✅ `program_development/testing.md` - 程序开发测试
- ✅ `tool_development/tools_config.md` - 技术工具配置指南
- ✅ `reverse_engineering/framework.md` - 逆向工程框架
- ✅ `reverse_engineering/binary_analysis.md` - 二进制文件分析
- ✅ `reverse_engineering/protocol_analysis.md` - 网络协议分析
- ✅ `reverse_engineering/disassembly_techniques.md` - 反汇编技术

**采集时机:**
- 身份角色切换时
- 研究阶段推进时
- 技术方案变更时
- 遇到技术突破时
- 第一句对话触发时

**采集逻辑:**
```
1. 等待对话触发（第一句对话或特定指令）
2. 扫描提示词集目录
3. 选择相关提示词文件
4. 读取并解析内容
5. 智能合并去重
6. 更新本规则文件
7. 记录采集日志
```

## 📊 阶段流程

| 阶段 | 身份角色 | 交接产物 | 完成标准 | 进度检查点 |
|------|----------|----------|----------|------------|
| **需求分析** | 架构师 | 需求规格说明书<br>功能清单<br>用户故事地图 | 所有功能需求明确<br>技术可行性确认<br>项目范围确定 | 需求收集完成50%<br>需求分析完成80%<br>需求评审通过 |
| **计划设计** | 架构师 | 技术架构设计文档<br>开发计划时间表<br>技术选型报告 | 架构设计完成<br>开发任务分解<br>技术风险识别 | 架构设计完成60%<br>技术方案确定<br>开发计划制定完成 |
| **开发实现** | 开发者 | 可运行的程序代码<br>单元测试用例<br>技术文档 | 核心功能实现<br>代码质量达标<br>单元测试通过 | 开发环境搭建完成<br>核心模块开发完成50%<br>整体功能开发完成80% |
| **测试验证** | 测试员 | 测试报告<br>缺陷清单<br>性能测试结果 | 所有测试用例执行完成<br>关键缺陷修复<br>性能指标达标 | 测试用例设计完成<br>功能测试完成70%<br>回归测试通过 |
| **逆向工程** | 逆向工程师 | 逆向分析报告<br>技术细节文档<br>修复建议 | 文件格式识别完成<br>协议结构解析完成<br>漏洞类型确认 | 文件头分析完成<br>协议字段识别50%<br>漏洞验证通过 |

## 🗂️ 文件结构

```
项目根目录/
├── .trae/
│   └── rules/
│       ├── project_rules.md      # 本文件
│       ├── last_status.json      # 状态备份
│       └── prompt_sets/          # 提示词集
│           ├── core/                 # 核心基础
│           ├── identities/           # 身份专属
│           ├── code_analysis/        # 代码分析路径
│           ├── program_development/  # 程序开发路径
│           ├── web_development/      # 网站开发路径
│           ├── tool_development/     # 工具开发路径
│           ├── static_review/        # 静态审查路径
│           ├── pattern_matching/     # 模式匹配路径
│           ├── reverse_engineering/  # 逆向工程路径
│           └── general_research/     # 通用研究
├── src/                          # 源代码
├── docs/                         # 技术文档
├── tools/                        # 工具集
├── data/                         # 研究数据
└── output/                       # 输出结果
```

## ⚠️ 错误处理

**异常策略:**
- 技术失败：重试3次，切换路径
- 提示词加载失败：使用备用提示词
- 系统错误：保存状态，提供恢复

**进度监控:**
- 实时状态更新
- 里程碑检查
- 风险预警

---
**最后更新:** 2025-08-30 23:42
**版本:** 1.0.0
**状态:** 激活