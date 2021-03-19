def calc():
    x = 12
    y = 6

    def add():
        z = x + y
        print("Sum is",z)

    def sub():
        z = x - y
        print("Sub is",z)

    # add(), sub()
    return add, sub

# output = calc()
# output[0]()
# output[1]()

add, sub = calc()
add()
sub()