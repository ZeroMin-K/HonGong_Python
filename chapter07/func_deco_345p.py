def test(function):
    def wrapper():
        print("greeting start")
        function()
        print("greeting end")
    return wrapper


@test
def hello():
    print("hello")

hello()