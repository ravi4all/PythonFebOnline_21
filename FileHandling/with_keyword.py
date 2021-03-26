# file = open('file_2.txt', 'r')
# data = file.read()
# print(data)
# file.close()

with open('file_2.txt') as file:
    data = file.read()
    print(data)
