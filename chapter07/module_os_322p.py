import os
print("current os:", os.name)
print("current folder:", os.getcwd())
print("element in folder:", os.listdir())

os.mkdir("hello")
os.rmdir("hello")

with open("original.txt", "w") as file:
    file.write("hello")
os.rename("original.txt", "new.txt")

os.remove("new.txt")

os.system("dir")