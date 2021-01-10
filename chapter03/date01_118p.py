import datetime

# calculate current time
now = datetime.datetime.now()

# print
print("{}year {}month {}day {}hour {}minute {} second".format(
    now.year,
    now.month,
    now.day,
    now.hour,
    now.minute,
    now.second
))