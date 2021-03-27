try:
    num_1 = int(input("Enter first number : "))
    num_2 = int(input("Enter second number : "))

    a = num_1 + num_2
    print("Sum is", a)

    b = num_1 - num_2
    print("Sub is", b)

    c = num_1 / num_2
    print("Div is", c)

    d = num_1 * num_2
    print("Mul is", d)
except ZeroDivisionError:
    print("Cannot divide by Zero")
except ValueError:
    print("Invalid Input, Please Enter a valid number")
except BaseException as ex:
    print("Some Error...",ex)
