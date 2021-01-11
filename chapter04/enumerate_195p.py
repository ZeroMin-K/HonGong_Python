example_list = ["elementA", "elementB", "elementC"]

print("# simple print")
print(example_list)
print()

print("# print using enumerate() ")
print(enumerate(example_list))
print()

print("# print using list()")
print(list(enumerate(example_list)))
print()

print("# combine with repetition")
for i, value in enumerate(example_list):
    print("no.{} element is {}".format(i, value))
