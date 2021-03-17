# Variable Length Arguments
def add(*x):
    # print(x)
    count = 0
    for i in x:
        count += i
    print("Sum is",count)

add(4,5)
add(3,5,6,7)
add(23,45,5,7,4,4,7)
add(12,11,4,2,4,2,12,45,56)
