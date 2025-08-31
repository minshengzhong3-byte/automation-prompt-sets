@echo off
chcp 65001 >nul

echo ========================================
echo    GitHub提示词集自动同步工具
echo ========================================
echo.

echo 正在检查Python环境...
python --version >nul 2>&1
if errorlevel 1 (
    echo 错误: 未找到Python，请先安装Python 3.6+
    pause
    exit /b 1
)

echo 正在检查依赖包...
python -c "import yaml, requests" 2>nul
if errorlevel 1 (
    echo 正在安装所需依赖包...
    pip install pyyaml requests
    if errorlevel 1 (
        echo 错误: 依赖包安装失败
        pause
        exit /b 1
    )
)

echo.
echo 开始同步GitHub提示词集...
echo ========================================

python git_prompt_sync.py

if errorlevel 0 (
    echo.
    echo ========================================
    echo   同步完成！
    echo   查看 sync_report.md 获取详细报告
    echo ========================================
) else (
    echo.
    echo ========================================
    echo   同步过程中出现错误
    echo   查看 git_prompt_sync.log 获取详细信息
    echo ========================================
)

echo.
pause