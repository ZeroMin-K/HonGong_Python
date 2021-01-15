list_number = [52, 273, 32, 72, 100]

try:
    number_input = int(input("Input Integer"))
    print("No.{] element: {}".format(number_input, list_number[number_input]))
except ValueError as exception:
    print("input integer")
    print("exception:", exception)
except IndexError as exception:
    print("out of index")
    print("exception:", exception)