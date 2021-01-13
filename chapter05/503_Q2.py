numbers = list(range(1, 10+1))

print("print odd number")
print(list(filter(lambda x: x % 2 == 1, numbers)))
print()

print("print over 3 under 7")
print(list(filter(lambda x: 3 <= x < 7, numbers)))
print()

print("power under 50")
print(list(filter(lambda x: x * x < 50, numbers)))