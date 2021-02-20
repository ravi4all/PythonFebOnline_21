x = 45
y = 5

'''
z = x + y
print("Sum is",z)
'''

#walrus operator :=
#print("Sum is",z := x + y)

#print(f"Sum of {x} and {y} is {(z := x + y)}")

print(f"""
Sum is {(z1 := x + y)}
Sub is {(z2 := x - y)}
Div is {(z3 := x / y)}
Mul is {(z4 := x * y)}
""")
