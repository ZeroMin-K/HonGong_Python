number = input("input integer<")
last_character = number[-1]

if last_character in "02468":
    print("it is even number")

if last_character in "13579":
    print("it is odd number")