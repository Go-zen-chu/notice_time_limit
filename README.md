# NoticeTimeLimit

## About
Simple script for noticing time limit in Desktop Notification.

## Supported Function
- End of work notification

## Install
```
virtualenv env
source env/bin/activate
pip install -r requirements.txt
```

## Run
```
python notice_time_limit.py &
```

## Stop
```
# if you are running in background
pkill -f "python notice_time_limit.py"
```
