class CustomException(Exception):
    def __init__(self):
        Exception.__init__(self)
        print("My Error")
    def __str__(self):
        return "Error occured"

raise CustomException