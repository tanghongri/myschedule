:: �ر��ն˻��� 
::@echo off

:: ���û�������  
python -V
set "err=%errorlevel%"
if "%err%"=="0" (
	echo "python ������ȷ..."
) else (
	echo "δ�ҵ� python ����,������ python �������� ���ٴγ���"
	pause
	exit
)  

if exist "%~dp0requirements.txt" (
	pip install -r "%~dp0requirements.txt"
	if "%err%"=="0" (
		echo "python ������װ���..."
	) else (
		echo "python ������װ���������������ӡ�����"
		pause
		exit
	) 
) else (
	echo "%~dp0requirements.txt δ�ҵ�"
	pause
	exit
)

pause