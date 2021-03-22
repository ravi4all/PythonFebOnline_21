def even(num):
    return num % 2 == 0

# print(even(6))
numbers = 4,2,6,45,5,8,8,12,13,154,432,7,4,7,11,6
# print(list(map(even, numbers)))
print(list(filter(even, numbers)))
