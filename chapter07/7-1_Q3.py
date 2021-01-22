import os

output = os.listdir('.')
print('os.listdir():', output)
print()

for path in output:
    if os.path.isdir(path):
        print("Folder:", path)
    else:
        print("File:", path)
