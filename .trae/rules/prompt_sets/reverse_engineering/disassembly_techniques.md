# 反汇编与反编译技术指南

## 🔧 反汇编基础

### 反汇编原理
```prompt
反汇编核心概念：
1. 机器码到汇编指令的转换
2. 指令解码与语义分析
3. 控制流图(CFG)构建
4. 数据流分析(DFA)
5. 符号执行与路径分析
6. 反汇编算法：线性扫描 vs 递归下降
```

### 指令集架构
```prompt
主流架构指令集：
1. x86/x64: CISC架构，变长指令
2. ARM: RISC架构，定长指令
3. MIPS: RISC架构，流水线优化
4. PowerPC: RISC架构，嵌入式系统
5. RISC-V: 开源RISC架构
6. 特殊架构：AVR、8051、MSP430
```

## 🎯 反汇编工具链

### 专业反汇编工具
```prompt
反汇编工具对比：
1. IDA Pro: 交互式反汇编，F5反编译
2. Ghidra: NSA开源工具，反编译能力强
3. Radare2: 命令行工具，脚本化支持
4. Binary Ninja: 现代界面，API丰富
5. Hopper: macOS专用，界面友好
6. Cutter: Radare2的GUI前端
```

### 自动化分析脚本
```python
# 反汇编分析框架
import capstone
import pefile
import struct
from typing import List, Dict, Any

class DisassemblyAnalyzer:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.pe = None
        self.md = None
        self.instructions = []
        self.functions = {}
        
    def load_binary(self):
        """加载二进制文件"""
        try:
            self.pe = pefile.PE(self.file_path)
            
            # 根据架构选择反汇编引擎
            if self.pe.FILE_HEADER.Machine == 0x8664:  # x64
                self.md = capstone.Cs(capstone.CS_ARCH_X86, capstone.CS_MODE_64)
            elif self.pe.FILE_HEADER.Machine == 0x14c:  # x86
                self.md = capstone.Cs(capstone.CS_ARCH_X86, capstone.CS_MODE_32)
            elif self.pe.FILE_HEADER.Machine == 0x1c0:  # ARM
                self.md = capstone.Cs(capstone.CS_ARCH_ARM, capstone.CS_MODE_ARM)
                
            self.md.detail = True
            return True
        except Exception as e:
            print(f"Error loading binary: {e}")
            return False
            
    def disassemble_section(self, section_name: str = '.text'):
        """反汇编指定节区"""
        if not self.pe:
            return []
            
        for section in self.pe.sections:
            if section.Name.decode().rstrip('\x00') == section_name:
                section_data = section.get_data()
                base_addr = section.VirtualAddress + self.pe.OPTIONAL_HEADER.ImageBase
                
                instructions = []
                for insn in self.md.disasm(section_data, base_addr):
                    instructions.append({
                        'address': insn.address,
                        'mnemonic': insn.mnemonic,
                        'op_str': insn.op_str,
                        'bytes': insn.bytes.hex(),
                        'size': insn.size
                    })
                    
                return instructions
                
        return []
        
    def find_functions(self):
        """识别函数边界"""
        if not self.pe:
            return {}
            
        functions = {}
        
        # 1. 通过符号表查找
        if hasattr(self.pe, 'DIRECTORY_ENTRY_EXPORT'):
            for exp in self.pe.DIRECTORY_ENTRY_EXPORT.symbols:
                if exp.name:
                    functions[exp.address] = {
                        'name': exp.name.decode(),
                        'type': 'export'
                    }
                    
        # 2. 通过入口点识别
        ep = self.pe.OPTIONAL_HEADER.AddressOfEntryPoint
        if ep:
            functions[ep + self.pe.OPTIONAL_HEADER.ImageBase] = {
                'name': 'entry_point',
                'type': 'entry'
            }
            
        # 3. 通过调用指令识别
        # 查找call指令的目标地址
        call_targets = set()
        for insn in self.disassemble_section():
            if insn['mnemonic'] == 'call':
                # 解析call目标地址
                target = self.parse_call_target(insn['op_str'])
                if target:
                    call_targets.add(target)
                    
        for target in call_targets:
            if target not in functions:
                functions[target] = {
                    'name': f'sub_{target:x}',
                    'type': 'call_target'
                }
                
        return functions
        
    def parse_call_target(self, op_str: str) -> int:
        """解析call指令的目标地址"""
        try:
            # 移除0x前缀并转换为整数
            if op_str.startswith('0x'):
                return int(op_str, 16)
            return None
        except:
            return None
            
    def analyze_control_flow(self, start_addr: int) -> Dict[str, Any]:
        """分析控制流图"""
        cfg = {
            'nodes': [],
            'edges': [],
            'basic_blocks': []
        }
        
        # 实现基本块识别算法
        # 1. 识别指令边界
        # 2. 构建基本块
        # 3. 分析控制流转移
        
        return cfg
        
    def find_strings(self) -> List[Dict[str, Any]]:
        """查找字符串引用"""
        strings = []
        
        if not self.pe:
            return strings
            
        for section in self.pe.sections:
            if section.Name.decode().rstrip('\x00') in ['.rdata', '.data']:
                section_data = section.get_data()
                
                # 查找ASCII字符串
                import re
                ascii_strings = re.findall(b'[\x20-\x7e]{4,}', section_data)
                
                for s in ascii_strings:
                    offset = section_data.find(s)
                    address = section.VirtualAddress + offset + self.pe.OPTIONAL_HEADER.ImageBase
                    
                    strings.append({
                        'address': address,
                        'string': s.decode('ascii', errors='ignore'),
                        'type': 'ascii'
                    })
                    
        return strings

# 高级反汇编分析器
class AdvancedDisassembler:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.analyzer = DisassemblyAnalyzer(file_path)
        
    def analyze_obfuscation(self):
        """分析代码混淆技术"""
        obfuscation_patterns = {
            'junk_code': [
                'nop', 'mov eax, eax', 'add eax, 0'
            ],
            'control_flow': [
                'jmp', 'call', 'ret'
            ],
            'string_encryption': [
                'xor', 'add', 'sub'
            ]
        }
        
        # 检测混淆模式
        detected_patterns = []
        
        return detected_patterns
        
    def reconstruct_functions(self):
        """函数重构与恢复"""
        functions = {}
        
        # 1. 函数序言检测
        prologue_patterns = [
            b'\x55\x8b\xec',  # push ebp; mov ebp, esp
            b'\x48\x83\xec',  # sub rsp, imm
        ]
        
        # 2. 函数尾声检测
        epilogue_patterns = [
            b'\x5d\xc3',      # pop ebp; ret
            b'\x48\x83\xc4',  # add rsp, imm
        ]
        
        return functions
        
    def generate_pseudo_code(self, function_addr: int) -> str:
        """生成伪代码"""
        # 简化的伪代码生成
        pseudo_code = f"""
        // Function at 0x{function_addr:x}
        int function_{function_addr:x}(int arg1, int arg2) {{
            int result = 0;
            
            // 反汇编指令转换为高级语言
            if (arg1 > 0) {{
                result = arg1 + arg2;
            }} else {{
                result = arg1 - arg2;
            }}
            
            return result;
        }}
        """
        
        return pseudo_code
```

## 🔄 反编译技术

### 反编译原理
```prompt
反编译技术要点：
1. 控制流分析：识别循环、条件语句
2. 数据流分析：变量使用与定义
3. 类型恢复：结构体、类、数组
4. 高级结构：switch、异常处理
5. 语义等价：低级到高级转换
6. 可读性优化：变量命名、注释添加
```

### 反编译工具集成
```python
# 反编译工具集成
import subprocess
import json
import os

class DecompilerEngine:
    def __init__(self, binary_path: str):
        self.binary_path = binary_path
        self.decompiled_code = {}
        
    def use_ghidra(self, output_dir: str = None):
        """使用Ghidra反编译"""
        if not output_dir:
            output_dir = os.path.dirname(self.binary_path)
            
        # Ghidra反编译命令
        cmd = [
            'ghidraRun',
            'analyzeHeadless',
            output_dir,
            'TempProject',
            '-import',
            self.binary_path,
            '-postScript',
            'DecompileScript.java'
        ]
        
        try:
            result = subprocess.run(cmd, capture_output=True, text=True)
            return result.stdout
        except Exception as e:
            return f"Ghidra execution failed: {e}"
            
    def use_retdec(self):
        """使用RetDec反编译"""
        cmd = [
            'retdec-decompiler',
            self.binary_path,
            '--output',
            f"{self.binary_path}.c"
        ]
        
        try:
            result = subprocess.run(cmd, capture_output=True, text=True)
            
            if os.path.exists(f"{self.binary_path}.c"):
                with open(f"{self.binary_path}.c", 'r') as f:
                    return f.read()
                    
        except Exception as e:
            return f"RetDec execution failed: {e}"
            
    def extract_high_level_info(self) -> Dict[str, Any]:
        """提取高级信息"""
        info = {
            'functions': [],
            'strings': [],
            'imports': [],
            'exports': []
        }
        
        # 使用radare2提取信息
        try:
            cmd = ['rabin2', '-I', self.binary_path]
            result = subprocess.run(cmd, capture_output=True, text=True)
            info['binary_info'] = result.stdout
            
            cmd = ['rabin2', '-s', self.binary_path]
            result = subprocess.run(cmd, capture_output=True, text=True)
            info['symbols'] = result.stdout
            
            cmd = ['rabin2', '-z', self.binary_path]
            result = subprocess.run(cmd, capture_output=True, text=True)
            info['strings'] = result.stdout
            
        except Exception as e:
            info['error'] = str(e)
            
        return info
```

## 🔍 调试与动态分析

### 调试器集成
```python
# 调试器集成框架
import frida
import sys

class DynamicAnalyzer:
    def __init__(self, target_process: str):
        self.target_process = target_process
        self.session = None
        
    def attach_process(self):
        """附加到目标进程"""
        try:
            self.session = frida.attach(self.target_process)
            return True
        except Exception as e:
            print(f"Failed to attach: {e}")
            return False
            
    def inject_javascript(self, js_code: str):
        """注入JavaScript代码"""
        if not self.session:
            return None
            
        script = self.session.create_script(js_code)
        
        def on_message(message, data):
            print(f"Message: {message}")
            
        script.on('message', on_message)
        script.load()
        return script
        
    def trace_function_calls(self, function_name: str):
        """跟踪函数调用"""
        js_code = f"""
        var targetFunction = Module.findExportByName(null, "{function_name}");
        if (targetFunction) {
            Interceptor.attach(targetFunction, {
                onEnter: function(args) {
                    console.log("Called {function_name}");
                    console.log("Arguments:", args);
                },
                onLeave: function(retval) {
                    console.log("Return value:", retval);
                }
            });
        }
        """
        
        return self.inject_javascript(js_code)
        
    def memory_dump(self, address: int, size: int):
        """内存转储"""
        js_code = f"""
        var baseAddress = ptr("{hex(address)}");
        var dump = baseAddress.readByteArray({size});
        console.log(hexdump(dump, {{ offset: 0, length: {size}, header: true }}));
        """
        
        return self.inject_javascript(js_code)
```

## 📊 分析结果模板

### 反汇编报告模板
```markdown
# 反汇编分析报告

## 二进制文件信息
- 文件路径: {binary_path}
- 文件大小: {file_size} bytes
- 架构: {architecture}
- 入口点: {entry_point}
- 编译时间: {compile_time}

## 节区分析
| 节区名称 | 虚拟地址 | 虚拟大小 | 原始大小 | 特征 |
|----------|----------|----------|----------|------|
| .text    | {text_va} | {text_vsize} | {text_rsize} | {text_flags} |
| .data    | {data_va} | {data_vsize} | {data_rsize} | {data_flags} |
| .rdata   | {rdata_va} | {rdata_vsize} | {rdata_rsize} | {rdata_flags} |

## 函数分析
### 导出函数
```{exported_functions}```

### 导入函数
```{imported_functions}```

### 识别函数
```{identified_functions}```

## 字符串分析
### ASCII字符串
```{ascii_strings}```

### Unicode字符串
```{unicode_strings}```

## 控制流图
```{control_flow_graph}```

## 反编译结果
```{decompiled_code}```

## 安全分析
### 潜在漏洞
```{vulnerabilities}```

### 混淆检测
```{obfuscation_detection}```

### 反调试技术
```{anti_debugging}```
```

### 函数分析报告
```markdown
# 函数详细分析报告

## 函数基本信息
- 函数地址: 0x{function_address:x}
- 函数名称: {function_name}
- 调用约定: {calling_convention}
- 参数数量: {parameter_count}
- 栈帧大小: {stack_frame_size}

## 参数分析
| 参数 | 类型 | 用途 | 来源 |
|------|------|------|------|
| arg1 | {type1} | {purpose1} | {source1} |
| arg2 | {type2} | {purpose2} | {source2} |

## 返回值
- 类型: {return_type}
- 含义: {return_meaning}

## 伪代码
```{pseudo_code}```

## 调用关系
### 调用此函数的函数
```{callers}```

### 此函数调用的函数
```{callees}```

## 数据流分析
### 全局变量使用
```{global_variables}```

### 字符串引用
```{string_references}```

### 系统调用
```{system_calls}```
```

---
**分析类型:** 反汇编与反编译
**版本:** 1.0.0
**继承:** 逆向工程框架