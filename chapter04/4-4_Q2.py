output = [i for i in range(100) if "{:b}".format(i).count("0") == 1 ]

for i in output:
    print("{}:{}".format(i, "{:b}".format(i)))

print("sum:", sum(output))
