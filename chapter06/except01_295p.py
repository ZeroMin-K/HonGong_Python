try:
    number_input_a = int(input("Input integer"))

    print("circle radius:", number_input_a)
    print("circle perimeter:", 2 * 3.14 * number_input_a)
    print("circle area:", 3.14 * number_input_a * number_input_a)
except Exception as exception:
    print("type(exception):", type(exception))
    print("exception:", exception)