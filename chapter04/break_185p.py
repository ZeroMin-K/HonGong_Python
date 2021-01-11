i = 0

while True:
    print("{} repetition".format(i))
    i = i+1

    input_text = input(">exit?:")
    if input_text in ["y", "Y"]:
        print("stop repetition")
        break