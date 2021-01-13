counter = 0

def fibonacci(n):
    print("calculate fibonacci({})".format(n))
    global counter
    counter += 1

    if n == 1:
        return 1
    if n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

fibonacci(10)
print("---")
print("fibonacci(10) count of calculation:{}".format(counter))