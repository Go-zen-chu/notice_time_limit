#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os, sys
import platform
import exceptions
import time
import signal
from datetime import datetime
from dateutil import parser
import schedule

def sigint_handler(signum, frame):
    print 'Finished program via ctrl+c'
    sys.exit()

def notice(title="notice_time_limit", msg="Test"):
    plt = platform.system()
    if plt == "Darwin":
        os.system("osascript -e 'display notification \"{}\" with title \"{}\"'".format(msg, title))
    else:
        raise exceptions.NotImplementedError("Not supported OS **yet**")

def notice_in_workday(date=datetime.today(), title="notice_time_limit", msg="Test"):
    weekday_idx = date.weekday()
    # not in Saturday and Sunday :)
    if weekday_idx not in {6, 7}:
        notice(title, msg)

def notice_end_of_work(date=datetime.today(), end_of_work="18:00"):
    end_dt = parser.parse(end_of_work)
    for notice_time in ["11:00", "13:00", "15:00", "16:00", "17:00", "18:00"]:
        dt = parser.parse(notice_time)
        sub = end_dt - dt
        # call notice_in_workday everyday but notice only in workday
        schedule.every().day.at(notice_time).do(notice_in_workday, date=date, msg="Remain Time: {} hours".format(sub.seconds / 3600))
    print("Start Noticing End Of Work...")
    while True:
        schedule.run_pending()
        time.sleep(30) # check every 30 s

if __name__ == '__main__':
    signal.signal(signal.SIGINT, sigint_handler)
    notice_end_of_work()
