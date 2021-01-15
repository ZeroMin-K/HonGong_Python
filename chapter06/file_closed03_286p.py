try:
    file = open("info.txt", "w")
    exception.occur()
except Exception as e:
    print(e)

finally:
    file.close()

print("Check if file is close")
print("file.closed:", file.closed)