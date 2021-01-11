limit = 10000
i = 1

sum_value = 0
while sum_value < limit:
    sum_value += i
    i += 1
    
print("when adding {}, excced {}, that value is {}".format(i, limit, sum_value))