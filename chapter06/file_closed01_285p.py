try:
    file = open("info.txt", "w")
    file.close()
except Exception as e:
    print(e)

print("Check file is closed")
print("file.closed:", file.closed)