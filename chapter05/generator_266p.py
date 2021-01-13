def test():
    print("function called")
    yield "test"

print("A pass")
test()

print("B pass")
test()
print(test())