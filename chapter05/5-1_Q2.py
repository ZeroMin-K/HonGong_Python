def mul(*values):
    sum = 1

    for value in values:
        sum = sum * value
    
    return sum
        
print(mul(5, 7, 9, 10))