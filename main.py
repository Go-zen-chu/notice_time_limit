#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import platform
import exceptions
import time
from datetime import datetime
from dateutil import parser
import schedule

def notice(msg="Test"):
    plt = platform.system()
    if plt == "Darwin":
        os.system("osascript -e 'display notification \"{}\"'".format(msg))
    else:
        raise exceptions.NotImplementedError("Not supported OS **yet**")

def notice_end_of_work(date=datetime.today()):
    weekday_idx = date.weekday()
    # not in Saturday and Sunday :)
    if weekday_idx not in {6, 7}:
        end_of_work = "18:00"
        end_dt = parser.parse(end_of_work)
        for notice_time in ["11:00", "13:00", "15:00", "16:00", "17:00", "18:00"]:
            dt = parser.parse(notice_time)
            sub = end_dt - dt
            schedule.every().day.at(notice_time).do(notice, "Remain Time: {} hours".format(sub.seconds / 3600))
        print("Start Noticing End Of Work...")
        while True:
            schedule.run_pending()
            time.sleep(30) # check every 30 s

if __name__ == '__main__':
    notice_end_of_work()
