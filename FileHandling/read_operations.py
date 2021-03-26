# 1. open file
# by default file opens in read mode
file = open('file_1.txt', 'r')

# 2. Read File
data = file.read()
print(data)

# 3. Close File
file.close()