import datetime
import time

now = datetime.datetime.now()
print now.year, now.month, now.day, now.hour, now.minute, now.second

dt_started = datetime.datetime.utcnow()

time.sleep(60)

# do some stuff

dt_ended = datetime.datetime.utcnow()
print((dt_ended - dt_started).total_seconds())
