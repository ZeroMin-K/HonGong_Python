list_number = [52, 273, 32, 72, 100]

try:
    number_input = int(input("Input integer>"))
    print("No.{} element: {}".format(number_input, list_number[number_input]))
    exce.occur()
except ValueError as exception:
    print("Input integer")
    print(type(exception), exception)
except IndexError as exception:
    print("out of boud")
    print(type(exception), exception)