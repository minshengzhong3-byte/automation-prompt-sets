# 静态审查研究路径框架

## 🎯 路径定义

**研究类型:** 静态审查 (Static Review)
**主要目标:** 自动化代码质量审查、安全漏洞检测和最佳实践验证
**适用阶段:** 代码审查阶段、质量保证阶段

## 📋 核心审查维度

### 1. 代码质量审查
```prompt
代码质量审查要点：
1. 编码规范检查：命名规范、格式标准、注释要求
2. 复杂度分析：圈复杂度、认知复杂度评估
3. 重复代码检测：代码克隆和重复模式识别
4. 可维护性评估：代码可读性和维护难度
5. 测试覆盖率验证：单元测试和集成测试覆盖
```

### 2. 安全漏洞扫描
```prompt
安全审查规则：
1. 常见漏洞检测：SQL注入、XSS、CSRF、SSRF等
2. 依赖安全扫描：第三方库漏洞和许可证检查
3. 配置安全检查：安全配置最佳实践验证
4. 身份认证审查：认证和授权机制安全性
5. 数据安全验证：数据加密和隐私保护措施
```

### 3. 最佳实践验证
```prompt
最佳实践验证：
1. 设计模式验证：架构和设计模式合规性
2. 性能优化建议：潜在性能问题识别
3. 错误处理审查：异常处理和恢复机制
4. 日志记录验证：日志格式和安全审计
5. 文档完整性：代码注释和技术文档检查
```

## 🔧 审查工具集

### 静态分析函数
```prompt
function performStaticAnalysis(codebase, rules) {
  // 执行全面的静态代码分析
  // 应用编码规范和质量规则
  // 检测安全漏洞和潜在问题
  // 生成详细的审查报告
}
```

### 安全扫描函数
```prompt
function scanSecurityVulnerabilities(dependencies, config) {
  // 扫描第三方依赖的安全漏洞
  // 检查安全配置和最佳实践
  // 识别潜在的安全风险
  // 提供修复建议和优先级
}
```

### 质量评估函数
```prompt
function assessCodeQuality(metrics, standards) {
  // 评估代码质量指标
  // 比较行业标准和最佳实践
  // 识别质量改进机会
  // 生成质量评分报告
}
```

## 📊 输出物标准

### 静态审查报告
```markdown
# 静态审查报告 - {项目名称}

## 审查摘要
- 审查时间: {timestamp}
- 审查文件数: {file_count}
- 问题总数: {issue_count}
- 安全漏洞数: {vulnerability_count}

## 代码质量分析
### 规范符合度
- 编码规范符合率: {compliance_rate}%
- 主要规范问题: {main_violations}
- 重复代码比例: {duplication_rate}%

### 复杂度指标
- 平均圈复杂度: {avg_complexity}
- 高复杂度方法: {high_complexity_methods}
- 认知复杂度超标: {cognitive_complexity_issues}

## 安全审查结果
### 漏洞统计
- 高危漏洞: {critical_vulnerabilities}
- 中危漏洞: {medium_vulnerabilities}
- 低危漏洞: {low_vulnerabilities}

### 依赖安全
- 漏洞依赖包: {vulnerable_dependencies}
- 许可证问题: {license_issues}
- 过期依赖: {outdated_dependencies}

## 改进建议
### 优先级修复
```{priority_fixes}```

### 最佳实践建议
```{best_practice_recommendations}```
```

### 问题清单
```yaml
code_issues:
  - id: issue_001
    type: security
    severity: high
    description: SQL注入漏洞
    location: src/controllers/user.js:45
    fix: 使用参数化查询
    
  - id: issue_002
    type: quality  
    severity: medium
    description: 圈复杂度过高
    location: src/utils/processor.js:78-120
    fix: 重构为多个小函数
    
  - id: issue_003
    type: best_practice
    severity: low
    description: 缺少错误处理
    location: src/services/api.js:32
    fix: 添加try-catch块
```

## ⚡ 审查流程

### 阶段1: 全面扫描
1. 执行自动化静态分析
2. 收集代码质量指标
3. 识别安全漏洞和风险

### 阶段2: 问题分类  
1. 按严重程度分类问题
2. 确定修复优先级
3. 分配责任人和时间表

### 阶段3: 详细报告
1. 生成结构化审查报告
2. 提供具体修复建议
3. 制定改进计划

### 阶段4: 跟踪验证
1. 跟踪问题修复进度
2. 验证修复效果
3. 更新审查状态

## 📈 质量指标

- **审查覆盖率:** 100% 代码文件
- **问题检出率:** > 95% 潜在问题
- **误报率:** < 5%
- **审查效率:** 大型项目 < 1小时

## 🔄 与其他路径集成

### 与代码分析集成
- 静态审查基于代码分析结果
- 共享技术栈和架构信息

### 与模式匹配集成  
- 识别代码中的反模式实例
- 提供模式改进建议

### 与通用研究集成
- 集成行业最佳实践
- 共享质量标准和规范

---
**研究路径:** 静态审查
**版本:** 1.0.0
**继承:** 核心基础框架
**相关身份:** 代码审查员、质量保证工程师