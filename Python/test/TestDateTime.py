import datetime
import time

now = datetime.datetime.now()
print now
print now.year, now.month, now.day, now.hour, now.minute, now.second
print datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

dt_started = datetime.datetime.utcnow()

time.sleep(60)

# do some stuff

dt_ended = datetime.datetime.utcnow()
print((dt_ended - dt_started).total_seconds())
