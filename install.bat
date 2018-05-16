:: 关闭终端回显 
::@echo off

:: 设置环境变量  
python -V
set "err=%errorlevel%"
if "%err%"=="0" (
	echo "python 环境正确..."
) else (
	echo "未找到 python 命令,请设置 python 环境变量 后再次尝试"
	pause
	exit
)  

if exist "%~dp0requirements.txt" (
	pip install -r "%~dp0requirements.txt"
	if "%err%"=="0" (
		echo "python 依赖安装完毕..."
	) else (
		echo "python 依赖安装错误，请检查网络连接。。。"
		pause
		exit
	) 
) else (
	echo "%~dp0requirements.txt 未找到"
	pause
	exit
)

pause