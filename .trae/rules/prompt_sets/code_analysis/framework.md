# 代码分析研究路径框架

## 🎯 路径定义

**研究类型:** 代码分析 (Code Analysis)
**主要目标:** 深入分析代码结构、逻辑流程和技术实现
**适用阶段:** 分析阶段、技术评估阶段

## 📋 核心分析维度

### 1. 结构分析
```prompt
结构分析要点：
1. 文件组织结构和模块划分
2. 包/命名空间的组织方式
3. 依赖关系和导入结构
4. 代码分层和架构模式
5. 配置文件和资源管理
```

### 2. 逻辑分析
```prompt
逻辑分析规则：
1. 控制流分析（条件、循环、异常处理）
2. 数据流跟踪（变量传递、状态变更）
3. 算法复杂度分析
4. 业务逻辑完整性
5. 边界条件处理
```

### 3. 技术分析
```prompt
技术分析重点：
1. 核心技术栈和版本
2. 第三方库和依赖
3. 性能关键代码段
4. 安全相关实现
5. 可扩展性和维护性
```

## 🔧 分析工具集

### 静态分析函数
```prompt
function performStaticAnalysis(codebase) {
  // 执行静态代码分析
  // 识别代码质量和规范问题
  // 检测潜在bug和安全漏洞
  // 生成静态分析报告
}
```

### 复杂度分析函数
```prompt
function analyzeComplexity(codeFiles) {
  // 计算代码复杂度指标
  // 识别高复杂度模块
  // 评估可维护性得分
  // 提供简化建议
}
```

### 依赖分析函数
```prompt
function analyzeDependencies(project) {
  // 分析项目依赖关系
  // 识别循环依赖和版本冲突
  // 评估依赖健康度
  // 提供依赖优化建议
}
```

## 📊 输出物标准

### 代码分析报告
```markdown
# 代码分析报告 - {项目名称}

## 分析摘要
- 分析时间: {timestamp}
- 分析文件数: {file_count}
- 总代码行数: {loc}
- 主要编程语言: {languages}

## 结构分析结果
### 文件组织结构
```{file_structure}```

### 模块依赖图
```{dependency_graph}```

## 技术栈分析
### 核心框架
- {framework_1}: {version}
- {framework_2}: {version}

### 主要依赖库
```{dependencies_list}```

## 代码质量评估
### 复杂度指标
- 平均圈复杂度: {avg_complexity}
- 最大圈复杂度: {max_complexity}
- 高复杂度文件: {high_complexity_files}

### 规范符合度
- 编码规范符合率: {compliance_rate}%
- 主要规范问题: {main_violations}
```

### 技术要点清单
```yaml
technical_insights:
  - id: insight_001
    category: architecture
    description: 微服务架构实现
    confidence: 0.95
    impact: high
    
  - id: insight_002
    category: performance
    description: 数据库查询优化点
    confidence: 0.88
    impact: medium
    
  - id: insight_003
    category: security
    description: 身份验证实现方式
    confidence: 0.92
    impact: high
```

## ⚡ 分析流程

### 阶段1: 初步扫描
1. 收集代码库基本信息
2. 识别主要技术栈
3. 建立初步结构认识

### 阶段2: 深度分析  
1. 重点分析核心模块
2. 深入理解业务逻辑
3. 识别关键技术实现

### 阶段3: 综合评估
1. 评估代码质量
2. 分析架构合理性
3. 识别改进机会

### 阶段4: 报告生成
1. 整理分析结果
2. 生成结构化报告
3. 提供 actionable 建议

## 📈 质量指标

- **分析覆盖率:** > 90% 核心代码
- **准确率:** > 85% 技术识别
- **完整性:** 覆盖所有重要维度
- **时效性:** 大型项目 < 2小时

## 🔄 与其他路径集成

### 与静态审查集成
- 代码分析结果为静态审查提供上下文
- 共享技术栈和架构信息

### 与模式匹配集成  
- 识别代码中的设计模式实例
- 提供模式应用评估

### 与通用研究集成
- 共享技术趋势分析
- 集成最佳实践建议

---
**研究路径:** 代码分析
**版本:** 1.0.0
**继承:** 核心基础框架
**相关身份:** 代码分析师、架构师