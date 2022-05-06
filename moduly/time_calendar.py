import time
print(time.time())
print(time.localtime())
import calendar
print(calendar.month(1996,9))
calendar.setfirstweekday(6)
print(calendar.month(1996,9))
print('2000 is leap: ', calendar.isleap(2000))
print(calendar.calendar(2019))