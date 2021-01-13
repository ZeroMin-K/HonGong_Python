def test():
    print("A pass")
    yield 1
    print("B pass")
    yield 2
    print("C pass")

output = test()

print("D pass")
a = next(output)
print(a)

print("E pass")
b = next(output)
print(b)

next(output)