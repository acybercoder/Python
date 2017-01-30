"""
Things to Remember
Avoid using the time module for translating between different time zones.
Use the datetime built-in module along with the pytz module to reliably convert between times in different time zones.
Always represent time in UTC and do conversions to local time as the final step before presentation.
"""

from time import localtime, strftime
now = 1407694710
local_tuple = localtime(now)
time_format = '%Y-%m-%d %H:%M:%S'
time_str = strftime(time_format, local_tuple)
print(time_str)

from time import mktime, strptime
time_tuple = strptime(time_str, time_format)
utc_now = mktime(time_tuple)
print(utc_now)

parse_format = '%Y-%m-%d %H:%M:%S %z'
depart_sfo = '2014-05-01 15:45:16 -0800'
time_tuple = strptime(depart_sfo, parse_format)
time_str = strftime(time_format, time_tuple)
print(time_str)

parse_format = '%Y-%m-%d %H:%M:%S %Z'
arrival_nyc = '2014-05-01 23:33:24 EDT'
#time_tuple = strptime(arrival_nyc, time_format) #ValueError: unconverted data remains: EDT

print('====datetime====')
from datetime import datetime, timezone
now = datetime(2014, 8, 10, 18, 18, 30)
now_utc = now.replace(tzinfo=timezone.utc)
now_local = now_utc.astimezone()
print(now_local)

time_str = '2014-08-10 11:18:30'
now = datetime.strptime(time_str, time_format)
time_tuple = now.timetuple()
utc_now = mktime(time_tuple)
print(utc_now)

import pytz

arrival_nyc = '2014-05-01 23:33:24'
nyc_dt_naive = datetime.strptime(arrival_nyc, time_format)
eastern = pytz.timezone('US/Eastern')
nyc_dt = eastern.localize(nyc_dt_naive)
utc_dt = pytz.utc.normalize(nyc_dt.astimezone(pytz.utc))

nepal = pytz.timezone('Asia/Katmandu')
nepal_dt = nepal.normalize(utc_dt.astimezone(nepal))
print(nepal_dt)
print(utc_dt)