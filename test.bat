@echo off
echo ========================================
echo 自动签到系统 - 本地测试
echo ========================================
echo.
echo 正在安装依赖...
pip install -r requirements.txt
echo.
echo 正在安装 Playwright 浏览器...
playwright install chromium
echo.
echo 启动签到测试...
python signin.py
echo.
pause
