# 二进制程序分析指南

## 🔍 二进制文件结构解析

### PE文件分析（Windows）
```prompt
PE文件结构分析：
1. DOS头检查：MZ标识、e_lfanew偏移
2. PE头解析：Signature、FileHeader、OptionalHeader
3. 节区表分析：.text/.data/.rsrc/.rdata各节特征
4. 导入表解析：依赖DLL与API函数列表
5. 导出表检查：对外提供的接口函数
6. 资源节提取：图标、版本信息、对话框资源
```

### ELF文件分析（Linux）
```prompt
ELF文件结构分析：
1. ELF头检查：魔数、架构类型、字节序
2. 程序头表：PT_LOAD段、PT_DYNAMIC段
3. 节区头表：.text/.data/.bss/.rodata特征
4. 动态链接信息：DT_NEEDED依赖、DT_SYMTAB符号表
5. 重定位信息：DT_REL/DT_RELA重定位表
6. 字符串表分析：符号名称、节区名称
```

### Mach-O文件分析（macOS）
```prompt
Mach-O文件结构分析：
1. 魔数检查：0xFEEDFACF（64位）标识
2. 头部信息：CPU类型、文件类型、加载命令数
3. 加载命令：LC_SEGMENT_64、LC_DYLD_INFO_ONLY
4. 段节分析：__TEXT/__DATA/__LINKEDIT段
5. 符号表：本地符号、外部符号、调试符号
6. 代码签名：LC_CODE_SIGNATURE验证
```

## 🔧 反汇编与反编译技术

### 反汇编策略
```prompt
反汇编分析流程：
1. 入口点定位：程序执行起始地址
2. 函数识别：prologue/epilogue模式匹配
3. 控制流图：基本块划分与跳转关系
4. 调用图构建：函数间调用关系
5. 字符串引用：常量字符串与函数关联
6. API调用分析：系统调用与库函数使用
```

### 反编译技术
```prompt
反编译还原技术：
1. 高级语言结构：循环、条件、switch语句
2. 数据结构识别：数组、结构体、类定义
3. 算法模式：排序、搜索、加密算法
4. 虚函数表：C++类层次结构
5. 异常处理：try-catch结构识别
6. 模板实例化：泛型代码还原
```

## 🛠️ 动态分析技术

### 调试器使用
```prompt
动态调试策略：
1. 断点设置：函数入口、API调用、关键地址
2. 内存监控：堆栈跟踪、变量值变化
3. 寄存器监控：参数传递、返回值分析
4. 调用栈跟踪：函数调用路径
5. 内存转储：运行时数据结构
6. 输入输出监控：文件、网络、注册表操作
```

### 沙箱分析
```prompt
沙箱环境分析：
1. 文件系统监控：创建、修改、删除文件
2. 网络活动：DNS查询、TCP/UDP连接
3. 注册表操作：键值读写、权限修改
4. 进程行为：子进程创建、线程操作
5. 内存行为：内存分配、代码注入
6. 持久化机制：启动项、服务安装
```

## 📊 协议与通信分析

### 网络协议解析
```prompt
协议分析技术：
1. 流量捕获：Wireshark/tcpdump抓包
2. 协议识别：特征码、端口、握手过程
3. 数据格式：TLV结构、二进制协议
4. 加密算法：密钥交换、数据加密
5. 认证机制：挑战响应、令牌验证
6. 状态管理：会话保持、心跳机制
```

### 文件格式逆向
```prompt
文件格式分析：
1. 魔数识别：文件类型标识符
2. 结构定义：头部、数据块、索引
3. 压缩算法：压缩方法、参数设置
4. 加密保护：加密算法、密钥管理
5. 版本兼容：格式版本演进
6. 校验机制：CRC、哈希、签名验证
```

## 🎯 分析工具与脚本

### 自动化分析脚本
```python
# 二进制文件信息提取脚本
import pefile
import lief

class BinaryAnalyzer:
    def __init__(self, filepath):
        self.filepath = filepath
        self.binary = None
        
    def analyze_pe(self):
        """PE文件分析"""
        pe = pefile.PE(self.filepath)
        
        # 提取基本信息
        info = {
            'arch': pe.FILE_HEADER.Machine,
            'sections': len(pe.sections),
            'imports': len(pe.DIRECTORY_ENTRY_IMPORT) if hasattr(pe, 'DIRECTORY_ENTRY_IMPORT') else 0,
            'exports': len(pe.DIRECTORY_ENTRY_EXPORT.symbols) if hasattr(pe, 'DIRECTORY_ENTRY_EXPORT') else 0
        }
        return info
        
    def analyze_elf(self):
        """ELF文件分析"""
        elf = lief.parse(self.filepath)
        
        info = {
            'arch': elf.header.machine_type,
            'entry_point': hex(elf.entrypoint),
            'sections': len(elf.sections),
            'symbols': len(elf.symbols)
        }
        return info
```

### 反汇编脚本
```python
# Capstone反汇编示例
from capstone import *

class Disassembler:
    def __init__(self, arch, mode):
        self.md = Cs(arch, mode)
        
    def disassemble(self, code, base_addr):
        """反汇编二进制代码"""
        instructions = []
        for insn in self.md.disasm(code, base_addr):
            instructions.append({
                'address': hex(insn.address),
                'mnemonic': insn.mnemonic,
                'op_str': insn.op_str,
                'bytes': insn.bytes.hex()
            })
        return instructions
        
    def find_functions(self, instructions):
        """识别函数边界"""
        functions = []
        for insn in instructions:
            if insn['mnemonic'] == 'push' and 'ebp' in insn['op_str']:
                # 函数开始
                functions.append(insn['address'])
        return functions
```

## 📋 分析报告模板

### 二进制分析报告
```markdown
# 二进制程序分析报告

## 文件信息
- 文件路径: {filepath}
- 文件大小: {filesize}
- 文件类型: {filetype}
- 编译时间: {compile_time}
- 编译器: {compiler_info}

## 结构分析
### 文件头信息
```{header_info}```

### 节区分布
```{section_layout}```

### 导入函数
```{import_functions}```

### 导出函数
```{export_functions}```

## 代码分析
### 反汇编结果
```{disassembly_output}```

### 函数识别
```{function_list}```

### 字符串提取
```{string_extraction}```

## 安全评估
### 潜在风险
```{security_risks}```

### 行为特征
```{behavior_analysis}```
```

---
**分析类型:** 二进制程序逆向
**版本:** 1.0.0
**继承:** 逆向工程框架