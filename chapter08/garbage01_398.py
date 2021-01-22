class Test:
    def __init__(self, name):
        self.name = name
        print("{} - create".format(self.name))
    
    def __del__(self):
        print("{} - deleted".format(self.name))


Test("A")
Test("B")
Test("C")