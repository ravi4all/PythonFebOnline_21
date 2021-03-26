file = open('file_1.txt')

# data = file.read()
# print(data)

# will start reading file from 20th character
# file.seek(20)
# data = file.read(8)

# data = file.readline()

data = file.readlines()
print(data)

# 3. Close File
file.close()