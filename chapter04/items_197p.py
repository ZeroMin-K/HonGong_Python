example_dictionary = {
    "keyA":"dataA",
    "keyB":"dataB",
    "keyC":"dataC"
}

print("# item() function of dictionary")
print("items():", example_dictionary.items())
print()

print("# combine repetition and items() function of dictionary")

for key, element in example_dictionary.items():
    print("dictionary[{}] = {}".format(key, element))