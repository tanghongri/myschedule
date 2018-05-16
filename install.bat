:: 关闭终端回显 
@echo off	
>nul 2>&1 "%SYSTEMROOT%\system32\cacls.exe" "%SYSTEMROOT%\system32\config\system"  
  
if '%errorlevel%' NEQ '0' (  
echo 请求管理员权限...  
echo Set UAC = CreateObject^("Shell.Application"^) > "%temp%\getadmin.vbs"  
echo UAC.ShellExecute "%~f0", "", "", "runas", 1 >> "%temp%\getadmin.vbs"  
"%temp%\getadmin.vbs"   
exit /B   
)

:: 检查 python 环境  
python -V
if '%errorlevel%' EQU '0' (
	echo [INFO]python 环境正确...
) else (
	echo [ERROR]未找到 python 命令,请设置 python 环境变量 后再次尝试,
	pause
	exit
)  

for /f "delims=" %%i in ('where pythonw') do (set PYTHONPATH=%%i)
echo [INFO]python 路径：%PYTHONPATH%
:: 检查 pip 环境
echo.
pip -V
if '%errorlevel%' EQU '0' (
	echo [INFO]pip 环境正确...
) else (
	echo [ERROR]未找到 pip 命令,请设置 python 环境变量 后再次尝试
	pause
	exit
)

echo.
if exist "%~dp0requirements.txt" (
	echo [INFO]开始安装 python 依赖...
	python -m pip install --upgrade pip
	pip install -r "%~dp0requirements.txt"
	if '%errorlevel%' EQU '0' (
		echo [INFO]python 依赖安装完毕...
	) else (
		echo [ERROR]python 依赖安装错误，请检查网络连接。。。
		pause
		exit
	) 
) else (
	echo [ERROR]%~dp0requirements.txt 未找到
	pause
	exit
)

echo.
echo [INFO]添加开机自启动
reg add "HKLM\Software\Microsoft\Windows\CurrentVersion\Run" /v "myschedule" /t REG_SZ /d "%PYTHONPATH% %~dp0startschedule.py"
pause