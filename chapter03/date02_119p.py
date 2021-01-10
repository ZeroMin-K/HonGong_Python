import datetime

now = datetime.datetime.now()

if now.hour <12:
    print("current time is {} hour, AM".format(now.hour))


if now.hour >=12:
    print("current time is {} hour, PM".format(now.hour))