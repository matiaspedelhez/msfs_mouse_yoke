@echo off

if not exist "./logs" mkdir logs

for /F "tokens=*" %%i in ('PowerShell -Command "& {Get-Date -Format FileDateTime}"') do (
    SET DATE_TIME=%%i
)

set LOGFILE=%~dp0logs\%DATE_TIME%.log
echo BATCH file init > %LOGFILE%

python --version 2 > nul
if errorlevel 1 goto NOPYTHON

if not exist %~dp0mouse_yoke.py goto NOSCRIPT

echo Trying to update pip... >> %LOGFILE%
python -m pip install --upgrade pip >> %LOGFILE%

echo Trying to install dependencies... >> %LOGFILE%
pip install -r ./requirements.txt >> %LOGFILE%

echo Running mouse_yoke.py... >> %LOGFILE%
python ./mouse_yoke.py %DATE_TIME%.log

exit /b 0

:NOPYTHON
echo Error^: Python is not installed or is not reachable. If you believe you have Python installed, check your PATH settings.
echo FATAL: Python is not installed. >> %LOGFILE%
pause

:NOSCRIPT
echo Error^: mouse_yoke.py is not reachable. Is it in the same path as run.bat?
echo FATAL: mouse_yoke.py is not reachable. >> %LOGFILE%
pause