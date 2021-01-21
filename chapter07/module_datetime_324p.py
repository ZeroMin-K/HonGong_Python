import datetime

now = datetime.datetime.now()
print(now.year,"year")
print(now.month, "month")
print(now.day, "day")
print(now.hour, "hour")
print(now.minute,"minute")
print(now.second,"second")
print()

output_a = now.strftime("%Y.%m.%d %H:%M:%S")
output_b = "{}year {}month {} day {} hour {} minute {} second". format(now.year, \
    now.month,\
    now.day,\
    now.hour,\
    now.minute,\
    now.second)
output_c = now.strftime("%Y{} %m{} %d{} %H{} %M{} %S{}").format(*"년월일시분초")
print(output_a)
print(output_b)
print(output_c)
print()