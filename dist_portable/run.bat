@echo off
title 鼠标助手便携版
:: 切换到脚本所在目录
cd /d "%~dp0"

echo 正在启动...
:: 直接调用同级目录下的 python_env 里的 python 运行
.\python_env\python.exe main.py

pause