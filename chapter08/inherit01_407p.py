class Parent:
    def __init__(self):
        self.value = "test"
        print("Parent calss __init()__ method called")
    def test(self):
        print("test() method of Parent class")

class Child(Parent):
    def __init__(self):
        Parent.__init__(self)
        print("Child class __init()__ method called")

child = Child()
child.test()
print(child.value)