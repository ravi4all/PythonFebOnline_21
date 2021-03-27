import io
try:
    file = open('file_1.txt','w')
    file.write("Hello world")
    data = file.read()
    print(data)
except io.UnsupportedOperation:
    print("Cannot read/write file")
except FileExistsError:
    print("File Already Exists ")
finally:
    print("File closed")
    file.close()
