# write creates the file if file do not exists
# if file already exists then it overwrites the file
# file = open('file_2.txt', 'w')
# data = "Hello world"
# file.write(data)
# file.close()

# file = open('file_2.txt', 'a')
# data = "\nBye World"
# file.write(data)
# file.close()

# file = open('file_2.txt','w')
# data = ['Hello World\n','Bye World']
# file.writelines(data)
# file.close()

# x - mode
# write creates the file if file do not exists
# if file already exists then it gives error
file = open('file_3.txt','x')
data = 'This is file handling demo'
file.write(data)
file.close()
