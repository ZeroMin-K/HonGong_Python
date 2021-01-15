try:
    file = open("info.txt", "w")
    exception.occur()
except Exception as e:
    print(e)

file.close()
print("check if file is close")
print("file.closed:", file.closed)