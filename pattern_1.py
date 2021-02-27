'''
*
**
***
****
*****
'''

'''
for i in range(1,6):
    print('*' * i)
'''

'''
1
12
123
1234
12345
'''

for i in range(5):
    for j in range(i+1):
        print(j+1,end='')
    print()

print('-' * 20)

'''
*****
****
***
**
*
'''
for i in range(5):
    for j in range(5-i,0,-1):
        print('*',end='')
    print()

print('-' * 20)

'''
1
23
456
78910
'''
x = 0
for i in range(4):
    for j in range(i+1):
        #x += 1
        x = x + 1
        print(x,end='')
    print()
















