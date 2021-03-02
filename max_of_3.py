x = 8
y = 9
z = 12

'''
if x > y:
    if x > z:
        print("X is greatest...")
elif y > x:
    if y > z:
        print("Y is greatest...")
else:
    print("Z is greatest")
'''

if x > y and x > z:
    print("X is greatest...")
elif y > x and y > z:
    print("Y is greatest...")
elif z > x and z > y:
    print("Z is greatest")
else:
    print("All are equal")






