# def calc(x,y):
#     return x + y
#
# output = calc(5,6)
# print("Sum is",output)

def calc(x,y):
    z = x + y, x - y, x / y, x * y
    return z

# output = calc(5,6)
# print(output)

# packing and unpacking

a,b,c,d = calc(5,6)
print(a)
