try:
    number_input_a = int(input("input integer>"))
except:
    print("not input integer")
else:
    print("circle radius:", number_input_a)
    print("circle perimeter:", 2 * 3.14 * number_input_a)
    print("circle area:", 3.14 * number_input_a * number_input_a)
