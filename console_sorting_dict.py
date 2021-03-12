Python 3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:44:55) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
====== RESTART: F:\Batches\Feb\PythonOnlineFebMorning\dict_exercise_2.py =====
Enter your search : sports shoes
Sports Shoes Puma 3400
>>> 
====== RESTART: F:\Batches\Feb\PythonOnlineFebMorning\dict_exercise_2.py =====
Enter your search : sports shoes
Name : Sports Shoes
Brand : Puma
Price : 3400
>>> 
====== RESTART: F:\Batches\Feb\PythonOnlineFebMorning\dict_exercise_2.py =====
Enter your search : iphone
Traceback (most recent call last):
  File "F:\Batches\Feb\PythonOnlineFebMorning\dict_exercise_2.py", line 24, in <module>
    condition = to_search in products[i].values().lower()
AttributeError: 'dict_values' object has no attribute 'lower'
>>> 
====== RESTART: F:\Batches\Feb\PythonOnlineFebMorning\dict_exercise_2.py =====
Enter your search : apple
Name : Apple Iphone 11
Brand : Apple
Price : 98000
Name : Macbook Pro
Brand : Apple
Price : 128000
>>> 
====== RESTART: F:\Batches\Feb\PythonOnlineFebMorning\dict_exercise_2.py =====
Enter your search : shoes
Name : Sports Shoes
Brand : Puma
Price : 3400
**************************************************
Name : Puma Shoes
Brand : Puma
Price : 2070
**************************************************
Name : Adidas Sports Shoes
Brand : Adidas
Price : 1900
**************************************************
>>> 
====== RESTART: F:\Batches\Feb\PythonOnlineFebMorning\dict_exercise_2.py =====
Enter your search : shoes
Name : Sports Shoes
Brand : Puma
Price : 3400
**************************************************
Name : Puma Shoes
Brand : Puma
Price : 2070
**************************************************
Name : Adidas Sports Shoes
Brand : Adidas
Price : 1900
**************************************************
>>> results
[{'p_name': 'Sports Shoes', 'brand': 'Puma', 'Category': 'Shoes', 'price': 3400}, {'p_name': 'Puma Shoes', 'brand': 'Puma', 'Category': 'Shoes', 'price': 2070}, {'p_name': 'Adidas Sports Shoes', 'brand': 'Adidas', 'Category': 'Shoes', 'price': 1900}]
>>> x = [1,2,3,2,2,4,4,2]
>>> sorted(x)
[1, 2, 2, 2, 2, 3, 4, 4]
>>> x = [['Ram','Aman','Sumit','Kunal'],[43,33,25,40]]
>>> sorted(x)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    sorted(x)
TypeError: '<' not supported between instances of 'int' and 'str'
>>> x = [['Ram',43],['Shyam',33],['Aman',25],['Kunal',40]]
>>> sorted(x)
[['Aman', 25], ['Kunal', 40], ['Ram', 43], ['Shyam', 33]]
>>> x = [{'name':'Ram','age':34},{'name':'Aman','age':40},{'name':'Sumit','age':35}]
>>> x
[{'name': 'Ram', 'age': 34}, {'name': 'Aman', 'age': 40}, {'name': 'Sumit', 'age': 35}]
>>> sorted(x)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    sorted(x)
TypeError: '<' not supported between instances of 'dict' and 'dict'
>>> sorted(x, key='age')
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    sorted(x, key='age')
TypeError: 'str' object is not callable
>>> def return_name(data):
	return data['name']

>>> def return_age(data):
	return data['age']

>>> x[0]
{'name': 'Ram', 'age': 34}
>>> return_name(x)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    return_name(x)
  File "<pyshell#13>", line 2, in return_name
    return data['name']
TypeError: list indices must be integers or slices, not str
>>> return_name(x[0])
'Ram'
>>> return_name(x[1])
'Aman'
>>> return_name(x[2])
'Sumit'
>>> sorted(x, key=return_name)
[{'name': 'Aman', 'age': 40}, {'name': 'Ram', 'age': 34}, {'name': 'Sumit', 'age': 35}]
>>> sorted(x, key=return_age)
[{'name': 'Ram', 'age': 34}, {'name': 'Sumit', 'age': 35}, {'name': 'Aman', 'age': 40}]
>>> 
====== RESTART: F:\Batches\Feb\PythonOnlineFebMorning\dict_exercise_2.py =====
Enter your search : shoes
Name : Sports Shoes
Brand : Puma
Price : 3400
**************************************************
Name : Puma Shoes
Brand : Puma
Price : 2070
**************************************************
Name : Adidas Sports Shoes
Brand : Adidas
Price : 1900
**************************************************
Filter Products : Yes | No ? no
>>> 
====== RESTART: F:\Batches\Feb\PythonOnlineFebMorning\dict_exercise_2.py =====
Enter your search : shoes
Name : Sports Shoes
Brand : Puma
Price : 3400
**************************************************
Name : Puma Shoes
Brand : Puma
Price : 2070
**************************************************
Name : Adidas Sports Shoes
Brand : Adidas
Price : 1900
**************************************************
Filter Products : Yes | No ? yes

    1. High to Low
    2. Low to High

Enter your choice : 1
Traceback (most recent call last):
  File "F:\Batches\Feb\PythonOnlineFebMorning\dict_exercise_2.py", line 50, in <module>
    sorted(x, key=return_price, reverse=True)
NameError: name 'x' is not defined
>>> 
====== RESTART: F:\Batches\Feb\PythonOnlineFebMorning\dict_exercise_2.py =====
Enter your search : shoes
Name : Sports Shoes
Brand : Puma
Price : 3400
**************************************************
Name : Puma Shoes
Brand : Puma
Price : 2070
**************************************************
Name : Adidas Sports Shoes
Brand : Adidas
Price : 1900
**************************************************
Filter Products : Yes | No ? yes

    1. High to Low
    2. Low to High

Enter your choice : 1
Name : Sports Shoes
Brand : Puma
Price : 3400
**************************************************
Name : Puma Shoes
Brand : Puma
Price : 2070
**************************************************
Name : Adidas Sports Shoes
Brand : Adidas
Price : 1900
**************************************************
>>> 
===== RESTART: F:/Batches/Feb/PythonOnlineFebMorning/movie_rec_system.py =====
>>> scores
{'action': 0.3076923076923077, 'comedy': 0.14285714285714285, 'drama': 0.23076923076923078, 'thriller': 0.14285714285714285, 'horror': 0.0}
>>> 
===== RESTART: F:/Batches/Feb/PythonOnlineFebMorning/movie_rec_system.py =====
>>> scores
{'action': 0.31, 'comedy': 0.14, 'drama': 0.23, 'thriller': 0.14, 'horror': 0.0}
>>> max(scores)
'thriller'
>>> 