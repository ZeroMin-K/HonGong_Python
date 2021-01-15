try:
    number_input_a = int(input("Input integer>"))

    print("circle radius:", number_input_a)
    print("circle perimeter:", number_input_a)
    print("circle area:", number_input_a)
except:
    print("Input integer!!")
else:
    print("not exception")
finally:
    print("Program finished")
