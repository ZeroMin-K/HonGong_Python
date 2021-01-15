list_number = [52, 372, 32, 72, 100]

try:
    number_input = int(input("Input integer>"))
    print("No.{} element: {}".format(number_input, list_number[number_input]))
except Exception as exception:
    print("type(exception):", type(exception))
    print("exception:", exception) 