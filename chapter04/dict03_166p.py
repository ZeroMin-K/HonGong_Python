dictionary = {
    "name" : "mango",
    "type" : "sugar"
}

print("before adding element:", dictionary)

del dictionary["name"]
del dictionary["type"]

print("after deleting element:", dictionary)