#for each iteration of i, j will execute 5 times
'''
for i in range(5):
    for j in range(5):
        print(f"i = {i}, j = {j}")

print('-' * 50)
'''

'''
*****
*****
*****
*****
*****
'''
for i in range(5):
    for j in range(5):
        print('*',end='')
    print()

print('-' * 20)

'''
*
**
***
****
*****
'''

for i in range(5):
    for j in range(i+1):
        print(i+1,end='')
    print()

'''
i = 0
j = i + 1 = 1
i = 1
j = i + 1 = 2
i = 2
j = i + 1 = 3
i = 3
j = i + 1 = 4
i = 4
j = i + 1 = 5
'''









