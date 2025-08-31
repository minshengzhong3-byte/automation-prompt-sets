#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
逆向开发程序演示脚本
展示如何使用新配置的逆向工程提示词集进行程序分析
"""

import os
import sys
import json
import time
from typing import Dict, List, Any

class ReverseEngineeringDemo:
    """逆向工程演示类"""
    
    def __init__(self):
        self.current_mode = "reverse_engineering"
        self.current_identity = "reverse_engineer"
        self.progress = 0
        self.analysis_results = {}
        
    def start_demo(self):
        """启动逆向工程演示"""
        print("🚀 逆向开发程序演示启动")
        print("=" * 50)
        
        # 1. 加载逆向工程提示词
        self.load_reverse_engineering_prompts()
        
        # 2. 模拟二进制文件分析
        self.analyze_binary_file()
        
        # 3. 模拟网络协议分析
        self.analyze_network_protocol()
        
        # 4. 生成逆向分析报告
        self.generate_analysis_report()
        
        print("=" * 50)
        print("✅ 逆向工程演示完成")
        
    def load_reverse_engineering_prompts(self):
        """加载逆向工程提示词"""
        print("📥 加载逆向工程提示词集...")
        
        prompts = {
            "framework": "逆向工程研究路径框架",
            "binary_analysis": "二进制文件结构解析",
            "protocol_analysis": "网络协议逆向分析",
            "disassembly": "反汇编与反编译技术"
        }
        
        for name, description in prompts.items():
            print(f"   ✅ 已加载: {description}")
            time.sleep(0.5)
            
        self.progress = 25
        
    def analyze_binary_file(self):
        """模拟二进制文件分析"""
        print("\n🔍 开始二进制文件分析...")
        
        # 模拟PE文件分析
        pe_analysis = {
            "file_info": {
                "path": "sample.exe",
                "size": "2.5MB",
                "architecture": "x64",
                "compile_time": "2024-01-15 14:30:00"
            },
            "sections": [
                {"name": ".text", "size": "1.2MB", "entropy": 6.8},
                {"name": ".data", "size": "0.8MB", "entropy": 5.2},
                {"name": ".rdata", "size": "0.3MB", "entropy": 4.9},
                {"name": ".reloc", "size": "0.2MB", "entropy": 3.1}
            ],
            "imports": [
                "kernel32.dll!CreateFileW",
                "kernel32.dll!ReadFile",
                "kernel32.dll!WriteFile",
                "advapi32.dll!RegOpenKeyExW",
                "wininet.dll!InternetOpenW"
            ],
            "strings": [
                "C:\\Users\\%s\\AppData\\Local\\",
                "Software\\Microsoft\\Windows\\CurrentVersion\\Run",
                "http://example.com/update",
                "Authorization: Bearer %s"
            ]
        }
        
        self.analysis_results["binary"] = pe_analysis
        self.progress = 50
        
        print("   ✅ PE结构分析完成")
        print("   ✅ 导入函数识别完成")
        print("   ✅ 字符串提取完成")
        
    def analyze_network_protocol(self):
        """模拟网络协议分析"""
        print("\n🌐 开始网络协议分析...")
        
        # 模拟HTTP协议分析
        protocol_analysis = {
            "protocol": "HTTP/1.1",
            "port": 80,
            "encryption": "TLS 1.2",
            "endpoints": [
                "GET /api/v1/status",
                "POST /api/v1/data",
                "PUT /api/v1/config"
            ],
            "authentication": "Bearer Token",
            "data_format": "JSON",
            "compression": "gzip"
        }
        
        self.analysis_results["protocol"] = protocol_analysis
        self.progress = 75
        
        print("   ✅ 协议识别完成")
        print("   ✅ 数据格式分析完成")
        print("   ✅ 认证机制分析完成")
        
    def generate_analysis_report(self):
        """生成逆向分析报告"""
        print("\n📊 生成逆向分析报告...")
        
        report = {
            "summary": {
                "analysis_type": "逆向工程分析",
                "target": "sample.exe",
                "duration": "45分钟",
                "confidence": "85%"
            },
            "findings": [
                {
                    "category": "网络通信",
                    "finding": "程序包含HTTP客户端功能",
                    "severity": "信息",
                    "details": "发现与example.com的通信"
                },
                {
                    "category": "持久化",
                    "finding": "注册表启动项修改",
                    "severity": "警告",
                    "details": "在Run键下创建启动项"
                },
                {
                    "category": "文件操作",
                    "finding": "AppData目录文件读写",
                    "severity": "信息",
                    "details": "访问用户配置目录"
                }
            ],
            "recommendations": [
                "进一步分析网络通信数据包",
                "检查注册表操作的具体内容",
                "验证文件操作的合法性"
            ]
        }
        
        self.analysis_results["report"] = report
        self.progress = 100
        
        # 保存报告
        with open("reverse_engineering_report.json", "w", encoding="utf-8") as f:
            json.dump(report, f, indent=2, ensure_ascii=False)
            
        print("   ✅ 报告已保存: reverse_engineering_report.json")
        
    def show_capabilities(self):
        """展示逆向开发能力"""
        print("\n🛠️ 逆向开发程序能力展示")
        print("=" * 40)
        
        capabilities = [
            "✅ 二进制文件格式解析 (PE/ELF/Mach-O)",
            "✅ 反汇编与反编译技术",
            "✅ 网络协议逆向分析",
            "✅ 动态分析与调试",
            "✅ 加密算法识别",
            "✅ 恶意代码检测",
            "✅ 漏洞分析框架",
            "✅ 自动化分析脚本"
        ]
        
        for cap in capabilities:
            print(f"   {cap}")
            
    def run_interactive_demo(self):
        """运行交互式演示"""
        print("\n🎯 交互式逆向工程演示")
        print("选择要演示的功能:")
        
        options = {
            "1": ("二进制分析", self.demo_binary_analysis),
            "2": ("协议分析", self.demo_protocol_analysis),
            "3": ("反汇编", self.demo_disassembly),
            "4": ("动态调试", self.demo_dynamic_debugging),
            "5": ("完整流程", self.demo_full_workflow)
        }
        
        for key, (name, _) in options.items():
            print(f"   {key}. {name}")
            
        choice = input("\n请输入选项 (1-5): ").strip()
        
        if choice in options:
            options[choice][1]()
        else:
            print("❌ 无效选项")
            
    def demo_binary_analysis(self):
        """演示二进制分析"""
        print("\n🔍 二进制文件分析演示")
        print("-" * 30)
        
        sample_data = {
            "filename": "malware_sample.exe",
            "md5": "d41d8cd98f00b204e9800998ecf8427e",
            "sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
            "size": "1.8MB",
            "sections": [
                {"name": ".text", "address": "0x1000", "size": "0x80000"},
                {"name": ".data", "address": "0x81000", "size": "0x20000"},
                {"name": ".rsrc", "address": "0xA1000", "size": "0x10000"}
            ]
        }
        
        print(f"📁 文件: {sample_data['filename']}")
        print(f"📏 大小: {sample_data['size']}")
        print(f"🔐 MD5: {sample_data['md5']}")
        print(f"🔐 SHA256: {sample_data['sha256']}")
        print("\n📊 节区信息:")
        
        for section in sample_data['sections']:
            print(f"   {section['name']}: {section['address']} - {section['size']}")
            
    def demo_protocol_analysis(self):
        """演示协议分析"""
        print("\n🌐 网络协议分析演示")
        print("-" * 30)
        
        # 模拟HTTP流量分析
        http_request = """
GET /api/data HTTP/1.1
Host: target.example.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64)
Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...
Content-Type: application/json

{"action": "get_user_data", "user_id": 12345}
        """.strip()
        
        print("📤 捕获的HTTP请求:")
        print(http_request)
        print("\n🔍 分析结果:")
        print("   ✅ 协议: HTTP/1.1")
        print("   ✅ 方法: GET")
        print("   ✅ 路径: /api/data")
        print("   ✅ 认证: JWT Bearer Token")
        print("   ✅ 数据格式: JSON")
        
    def demo_disassembly(self):
        """演示反汇编"""
        print("\n⚙️ 反汇编演示")
        print("-" * 30)
        
        # 模拟x64汇编代码
        assembly_code = """
0x1000:  push   rbp
0x1001:  mov    rbp, rsp
0x1004:  sub    rsp, 0x20
0x1008:  mov    [rbp-0x8], rdi
0x100c:  mov    [rbp-0x10], rsi
0x1010:  mov    rax, [rbp-0x8]
0x1014:  add    rax, [rbp-0x10]
0x1018:  leave  
0x1019:  ret    
        """.strip()
        
        print("📜 反汇编结果:")
        print(assembly_code)
        print("\n📝 伪代码:")
        print("""
long long add_numbers(long long a, long long b) {
    return a + b;
}
        """.strip())
        
    def demo_dynamic_debugging(self):
        """演示动态调试"""
        print("\n🐛 动态调试演示")
        print("-" * 30)
        
        # 模拟调试会话
        debug_session = [
            "[+] 附加到进程 PID 1234",
            "[+] 设置断点: 0x7FF612345678",
            "[+] 命中断点",
            "[+] 寄存器状态:",
            "    RAX: 0x1234567890ABCDEF",
            "    RBX: 0x0000000000000000",
            "    RCX: 0x00007FF612345678",
            "[+] 内存转储: 0x7FF600000000",
            "    00 01 02 03 04 05 06 07 08 09 0A 0B 0C 0D 0E 0F"
        ]
        
        for line in debug_session:
            print(line)
            
    def demo_full_workflow(self):
        """演示完整逆向工程流程"""
        print("\n🔄 完整逆向工程流程")
        print("-" * 30)
        
        workflow_steps = [
            "1️⃣ 样本收集与分类",
            "2️⃣ 静态分析 (PE结构、字符串、导入表)",
            "3️⃣ 动态分析 (行为监控、网络流量)",
            "4️⃣ 反汇编与反编译",
            "5️⃣ 协议逆向分析",
            "6️⃣ 漏洞挖掘与利用",
            "7️⃣ 特征提取与检测",
            "8️⃣ 报告生成与分享"
        ]
        
        for step in workflow_steps:
            print(f"   {step}")
            time.sleep(0.3)

def main():
    """主函数"""
    demo = ReverseEngineeringDemo()
    
    # 基础演示
    demo.start_demo()
    
    # 展示能力
    demo.show_capabilities()
    
    # 交互式演示
    try:
        demo.run_interactive_demo()
    except KeyboardInterrupt:
        print("\n\n👋 演示已中断")

if __name__ == "__main__":
    main()