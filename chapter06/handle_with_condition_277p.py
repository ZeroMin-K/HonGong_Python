user_input_a = input("input integer>")

if user_input_a.isdigit():
    number_input_a = int(user_input_a)
    print("circle radius:", number_input_a)
    print("circle perimeter", 2 * 3.14 * number_input_a)
    print("circle area:", 3.14 * number_input_a * number_input_a)
else:
    print("input integer!")