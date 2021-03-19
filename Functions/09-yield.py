def counter():
    x = 0
    while x <= 10:
        x += 1
        yield x

count = counter()

print(next(count))
print(next(count))
print("*" * 50)

for i in count:
    print(i)
