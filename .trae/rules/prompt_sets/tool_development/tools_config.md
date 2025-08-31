# 技术工具配置指南

**继承：** 核心基础层
**用途：** 提供具体的技术工具配置和最佳实践

## 代码质量工具配置

### 1. JavaScript/TypeScript 工具链

#### ESLint 配置
```json
{
  "extends": [
    "eslint:recommended",
    "@typescript-eslint/recommended",
    "plugin:prettier/recommended"
  ],
  "plugins": ["@typescript-eslint", "prettier"],
  "rules": {
    "no-console": "warn",
    "no-unused-vars": "error",
    "prefer-const": "error",
    "no-var": "error",
    "eqeqeq": "error",
    "curly": "error",
    "no-eval": "error",
    "no-implied-eval": "error",
    "no-new-func": "error",
    "no-script-url": "error"
  }
}
```

#### Prettier 配置
```json
{
  "semi": true,
  "trailingComma": "es5",
  "singleQuote": true,
  "printWidth": 80,
  "tabWidth": 2,
  "useTabs": false
}
```

#### TypeScript 配置
```json
{
  "compilerOptions": {
    "strict": true,
    "noImplicitAny": true,
    "noImplicitReturns": true,
    "noImplicitThis": true,
    "noUnusedLocals": true,
    "noUnusedParameters": true
  }
}
```

### 2. Python 工具链

#### Pylint 配置
```ini
[MASTER]
disable=C0114,C0116

[MESSAGES CONTROL]
disable=C0303,W0621,R0903,C0103

[FORMAT]
max-line-length=100
indent-string='    '

[DESIGN]
max-args=5
max-attributes=7
max-bool-expr=5
max-branches=12
max-locals=15
max-parents=7
max-public-methods=20
max-returns=6
max-statements=50

[SIMILARITIES]
min-similarity-lines=4
ignore-comments=yes
ignore-docstrings=yes
ignore-imports=yes
```

#### Black 配置
```toml
[tool.black]
line-length = 100
target-version = ['py38']
include = '\.pyi?$'
extend-exclude = '''
/(
  # directories
  \.eggs
  | \.git
  | \.hg
  | \.mypy_cache
  | \.tox
  | \.venv
  | _build
  | buck-out
  | build
  | dist
)/
'''
```

#### MyPy 配置
```toml
[tool.mypy]
python_version = "3.8"
warn_return_any = true
warn_unused_configs = true
disallow_untyped_defs = true
disallow_incomplete_defs = true
check_untyped_defs = true
disallow_untyped_decorators = true
no_implicit_optional = true
warn_redundant_casts = true
warn_unused_ignores = true
warn_no_return = true
warn_unreachable = true
strict_equality = true
```

### 3. Java 工具链

#### Checkstyle 配置
```xml
<?xml version="1.0"?>
<!DOCTYPE module PUBLIC
  "-//Checkstyle//DTD Checkstyle Configuration 1.3//EN"
  "https://checkstyle.org/dtds/configuration_1_3.dtd">

<module name="Checker">
  <property name="charset" value="UTF-8"/>
  <property name="severity" value="warning"/>
  
  <module name="TreeWalker">
    <module name="AvoidNestedBlocks"/>
    <module name="EmptyBlock"/>
    <module name="LeftCurly"/>
    <module name="NeedBraces"/>
    <module name="RightCurly"/>
    <module name="EmptyStatement"/>
    <module name="EqualsHashCode"/>
    <module name="HiddenField">
      <property name="ignoreSetter" value="true"/>
      <property name="ignoreConstructorParameter" value="true"/>
    </module>
    <module name="IllegalInstantiation"/>
    <module name="InnerAssignment"/>
    <module name="MagicNumber"/>
    <module name="MissingSwitchDefault"/>
    <module name="MultipleVariableDeclarations"/>
    <module name="SimplifyBooleanExpression"/>
    <module name="SimplifyBooleanReturn"/>
    <module name="FinalClass"/>
    <module name="HideUtilityClassConstructor"/>
    <module name="InterfaceIsType"/>
    <module name="VisibilityModifier"/>
    <module name="ArrayTypeStyle"/>
    <module name="FinalParameters"/>
    <module name="TodoComment"/>
    <module name="UpperEll"/>
  </module>
</module>
```

#### PMD 规则配置
```xml
<?xml version="1.0"?>
<ruleset name="Custom Rules"
         xmlns="http://pmd.sourceforge.net/ruleset/2.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://pmd.sourceforge.net/ruleset/2.0.0
         https://pmd.sourceforge.net/ruleset_2_0_0.xsd">

  <description>
    Custom rules for code quality
  </description>

  <rule name="ExcessiveClassLength"
        message="The class {0} is too long ({1} lines)."
        class="net.sourceforge.pmd.rules.design.ExcessiveClassLength">
    <priority>3</priority>
    <properties>
      <property name="minimum" value="1000"/>
    </properties>
  </rule>

  <rule name="ExcessiveMethodLength"
        message="The method {0} is too long ({1} lines)."