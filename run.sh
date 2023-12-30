#!/bin/bash

if [ ! -d "./logs" ]; then
  mkdir logs
fi

DATE_TIME=$(date +%F_%H-%M-%S)
LOGFILE="${HOME}/logs/$DATE_TIME.log"
echo "BATCH file init" > "$LOGFILE"

python --version 2 > /dev/null
if [ $? -ne 0 ]; then
  echo "No Python installed" >> "$LOGFILE"
  exit 1
fi

if [ ! -f "./mouse_yoke.py" ]; then
  echo "Can't find mouse_yoke.py" >> "$LOGFILE"
  exit 1
fi

echo "Trying to update pip..." >> "$LOGFILE"
pip install --upgrade pip >> "$LOGFILE"

echo "Trying to install dependencies..." >> "$LOGFILE"
pip install -r ./requirements.txt >> "$LOGFILE"

echo "Running mouse_yoke.py..." >> "$LOGFILE"
python ./mouse_yoke.py "$DATE_TIME.log"
