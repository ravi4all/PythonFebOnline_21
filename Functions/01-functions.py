# Variables Scope
# Local and Global

# Global Scope
x = 9
y = 4

# Function definition
def add():
    # Local variables
    x = 5
    y = 6
    z = x + y
    print("Sum is",z)

def sub():
    x = 9
    y = 20
    z = x - y
    print("Sub is",z)

# Function calling
add()
print("Mul is",x * y)
sub()
