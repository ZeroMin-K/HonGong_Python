list_input_a = ["52", "273", "32", "SPY", "103"]

list_number = []

for item in list_input_a:
    try:
        float(item)
        list_number.append(item)
    except:
        pass


print("numbers in {} is ".format(list_input_a))
print("{}".format(list_number))