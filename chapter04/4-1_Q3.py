numbers = [273, 103, 5, 32, 65, 9, 72, 800, 99]

for number in numbers:
    if number % 2 == 0:
        print("{} is even number".format(number))
    else:
        print("{} is odd number".format(number))
print()

for number in numbers:
    print("{} is {} digits".format(number, len(str(number))))

