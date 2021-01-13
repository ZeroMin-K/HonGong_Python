def call_10_times(func):
    for i in range(10):
        func()

def print_hello():
    print("Hello")

call_10_times(print_hello)