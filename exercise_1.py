'''
1. Sum of all n natural numbers
2. Print multiplication table of a number provided by user
'''

n = int(input("Enter a number : "))
for i in range(1,11):
    print(f"{n} x {i} = ",n * i)

sum = 0
for i in range(1,n+1):
    sum = sum + i
print("Sum is",sum)
    
