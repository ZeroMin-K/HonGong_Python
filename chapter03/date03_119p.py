import datetime

now = datetime.datetime.now()

if 3 <= now.month <= 5:
    print("current {}month. spring".format(now.month))

if 6<= now.month <= 8:
    print("current {}month. summer".format(now.month))

if 9 <= now.month <= 11:
    print("current {}month. fall".format(now.month))

if now.month == 12 or 1 <= now.month <= 2:
    print("current {}month. winter".format(now.month))