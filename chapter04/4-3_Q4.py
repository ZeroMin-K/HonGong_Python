max_value = 0
a = 0
b = 0

#for i in range(100):
#    j = 100 - i 

#    if (i * j) > max_value:
#        max_value = i * j
#        a = i
#        b = j

for i in range(1, 100 // 2 + 1):
    j = 100 -i
    current = i * j
    if max_value < current:
        a = i
        b = j
        max_value = current


print("max case: {} * {} = {}".format(a, b, max_value))