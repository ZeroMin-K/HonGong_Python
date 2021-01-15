try:
    file = open("info.txt", "w")

    exception.occur()

    file.close()
except Exception as e:
    print(e)

print("Check if file is closed")
print("file.closed:", file.closed)