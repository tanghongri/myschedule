:: �ر��ն˻��� 
@echo off	
>nul 2>&1 "%SYSTEMROOT%\system32\cacls.exe" "%SYSTEMROOT%\system32\config\system"  
  
if '%errorlevel%' NEQ '0' (  
echo �������ԱȨ��...  
echo Set UAC = CreateObject^("Shell.Application"^) > "%temp%\getadmin.vbs"  
echo UAC.ShellExecute "%~f0", "", "", "runas", 1 >> "%temp%\getadmin.vbs"  
"%temp%\getadmin.vbs"   
exit /B   
)

:: ��� python ����  
python -V
if '%errorlevel%' EQU '0' (
	echo [INFO]python ������ȷ...
) else (
	echo [ERROR]δ�ҵ� python ����,������ python �������� ���ٴγ���,
	pause
	exit
)  

for /f "delims=" %%i in ('where pythonw') do (set PYTHONPATH=%%i)
echo [INFO]python ·����%PYTHONPATH%
:: ��� pip ����
echo.
pip -V
if '%errorlevel%' EQU '0' (
	echo [INFO]pip ������ȷ...
) else (
	echo [ERROR]δ�ҵ� pip ����,������ python �������� ���ٴγ���
	pause
	exit
)

echo.
if exist "%~dp0requirements.txt" (
	echo [INFO]��ʼ��װ python ����...
	python -m pip install --upgrade pip
	pip install -r "%~dp0requirements.txt"
	if '%errorlevel%' EQU '0' (
		echo [INFO]python ������װ���...
	) else (
		echo [ERROR]python ������װ���������������ӡ�����
		pause
		exit
	) 
) else (
	echo [ERROR]%~dp0requirements.txt δ�ҵ�
	pause
	exit
)

echo.
echo [INFO]��ӿ���������
reg add "HKLM\Software\Microsoft\Windows\CurrentVersion\Run" /v "myschedule" /t REG_SZ /d "%PYTHONPATH% %~dp0startschedule.py"
pause