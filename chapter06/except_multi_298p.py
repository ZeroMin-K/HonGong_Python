list_number = [52, 273, 32, 72, 100]

try:
    number_input = int(input("Input integer>"))
    print("no.{} element:{}".format(number_input, list_number[number_input]))
except ValueError:
    print("Input integer")
except IndexError:
    print("index is out of bound")