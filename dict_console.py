Python 3.8.8 (tags/v3.8.8:024d805, Feb 19 2021, 13:18:16) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> d = {}
>>> type(d)
<class 'dict'>
>>> d = {}
>>> 
>>> d = {'name':'Ram', 'age':50,'dept':'IT'}
>>> d
{'name': 'Ram', 'age': 50, 'dept': 'IT'}
>>> d[0]
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    d[0]
KeyError: 0
>>> d['name']
'Ram'
>>> d['age']
50
>>> d['dept']
'IT'
>>> len(d)
3
>>> d.keys()
dict_keys(['name', 'age', 'dept'])
>>> d.values()
dict_values(['Ram', 50, 'IT'])
>>> d.items()
dict_items([('name', 'Ram'), ('age', 50), ('dept', 'IT')])
>>> d['sal'] = 45000
>>> d
{'name': 'Ram', 'age': 50, 'dept': 'IT', 'sal': 45000}
>>> d['name'] = 'Raman'
>>> d
{'name': 'Raman', 'age': 50, 'dept': 'IT', 'sal': 45000}
>>> del d['sal']
>>> d
{'name': 'Raman', 'age': 50, 'dept': 'IT'}
>>> d['sal']
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    d['sal']
KeyError: 'sal'
>>> d.get('name')
'Raman'
>>> d.get('sal')
>>> d.get('sal', 'Not Available')
'Not Available'
>>> d.get('name', 'Not Available')
'Raman'
>>> d.get('sal', 'Not Available')
'Not Available'
>>> data = {"names":['Ram', 'Shyam', 'Aman'], 'dept' : ['IT','HR','IT']}
>>> data['names']
['Ram', 'Shyam', 'Aman']
>>> data['dept']
['IT', 'HR', 'IT']
>>> data['names'][0]
'Ram'
>>> data['names'][1]
'Shyam'
>>> data['names'][2]
'Aman'
>>> data['dept'][0] = 'HR'
>>> data
{'names': ['Ram', 'Shyam', 'Aman'], 'dept': ['HR', 'HR', 'IT']}
>>> data = {'name': 'Raman', 'age': 50, 'dept': 'IT', 'sal': 45000}
>>> for item in data:
	print(item)

	
name
age
dept
sal
>>> for item in data.values():
	print(item)

	
Raman
50
IT
45000
>>> for item in data:
	print(data[item])

	
Raman
50
IT
45000
>>> for item in data:
	print(item, ":", data[item])

	
name : Raman
age : 50
dept : IT
sal : 45000
>>> 
======= RESTART: F:/Batches/Feb/PythonOnlineFebMorning/dict_exercise.py ======
>>> 
======= RESTART: F:/Batches/Feb/PythonOnlineFebMorning/dict_exercise.py ======
John : Football
Harry : Football
>>> 
======= RESTART: F:/Batches/Feb/PythonOnlineFebMorning/dict_exercise.py ======
Tom : 78
Shawn : 88
Harry : 76
>>> 
====== RESTART: F:/Batches/Feb/PythonOnlineFebMorning/dict_exercise_2.py =====
Enter your search : apple iphone
>>> 
====== RESTART: F:/Batches/Feb/PythonOnlineFebMorning/dict_exercise_2.py =====
Enter your search : adidas
>>> name = 'JBL Headphones bluetooth'
>>> search = 'jbl headphones'
>>> search == name
False
>>> 