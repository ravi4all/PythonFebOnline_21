def calc(x, y, opr):
    z = x + opr + y
    result = eval(z)
    print("Result is",result)

print("""
Press 1 for Add
Press 2 for Sub
Press 3 for Div
Press 4 for Mul
""")

ch = int(input("Enter your choice : "))

num_1 = input("Enter first number : ")
num_2 = input("Enter second number : ")

# operations = [add, sub, div, mul]
# operations[ch - 1](num_1, num_2)

operations = {
    1 : '+',
    2 : '-',
    3 : '/',
    4 : '*'
}
opr = operations.get(ch)
calc(num_1, num_2, opr)
