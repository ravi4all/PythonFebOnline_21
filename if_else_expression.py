x = 6
y = 8
z = 10

'''
if x % 2 == 0:print("Even")
else:print("Odd")
'''

ans = "Even" if x % 2 == 0 else "Odd"
print(ans)

ans = "X" if x > y and x > z else "Y" if y > x and y > z else "Z"
print(ans,"is greatest")
