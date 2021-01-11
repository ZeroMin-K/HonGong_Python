number = int(input("input integer>"))

if number % 2 == 0:
    print((
        "input string is {} \n"
        "{} is even number"
    ).format(number, number))
else:
    print((
        "input string is {} \n"
        "{} is odd number"
    ).format(number, number))