@echo off

for /f "tokens=2-8 delims=.:/ " %%a in ("%date% %time%") do set DateNtime=%%c-%%a-%%b_%%d-%%e-%%f.%%g

if not exist "./logs" mkdir logs

set LOGFILE=%~dp0logs\%DateNtime%.log
echo BATCH file init > %LOGFILE%

echo Trying to update pip... >> %LOGFILE%
python -m pip install --upgrade pip >> %LOGFILE%

echo Trying to install dependencies... >> %LOGFILE%
pip install -r ./requirements.txt >> %LOGFILE%

echo Running mouse_yoke.py... >> %LOGFILE%
python ./mouse_yoke.py %DateNtime%.log

exit /b 0