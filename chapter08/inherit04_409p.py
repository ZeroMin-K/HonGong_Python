class CustomException(Exception):
    def __init__(self, message, value):
        Exception.__init__(self)
        self.message = message
        self.value = value
    
    def __str__(self):
        return self.message

    def print(self):
        print("Error info")
        print("mesage:", self.message)
        print("value:", self.value)

try: 
    raise CustomException("Not reason", 273)
except CustomException as e:
    e.print()