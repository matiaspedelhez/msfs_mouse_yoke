@echo off

if not exist "./logs" mkdir logs

set date=%date:~10,4%_%date:~7,2%_%date:~4,2%
set time=%time:~0,2%_%time:~3,2%_%time:~6,2%
set date_time=%date%-%time%
set LOGFILE=%~dp0logs\%date_time%.log
echo BATCH file init > %LOGFILE%

echo Trying to update pip... >> %LOGFILE%
python -m pip install --upgrade pip >> %LOGFILE%

echo Trying to install dependencies... >> %LOGFILE%
pip install -r ./requirements.txt >> %LOGFILE%

echo Running mouse_yoke.py... >> %LOGFILE%
python ./mouse_yoke.py %date_time%.log

exit /b 0