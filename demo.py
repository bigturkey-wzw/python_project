import time
import calendar

localtime = time.asctime(time.localtime(time.time()))
print(localtime)

cal = calendar.month(2021, 10)
print(cal)