# def person(name, age, sal, *address):
#     print("Name is",name)
#     print("Age is",age)
#     print("Salary is",sal)
#     print("Address is",address)
#
# person('Ram',34,45000,'Delhi')
# person('Ram',34,45000,'Delhi','Gurgaon')

def person(name,**details):
    print("Hello",name)
    print(details)

person(name='Ram', age=34, sal=45000, address='Delhi')
person(name='Aman', name_2='Shyam', age=34, sal=35000)