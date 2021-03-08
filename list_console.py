Python 3.8.8 (tags/v3.8.8:024d805, Feb 19 2021, 13:18:16) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> data = []
>>> type(data)
<class 'list'>
>>> data = list()
>>> type(data)
<class 'list'>
>>> data = [2,1,3,5,6,3,5,67]
>>> data = [2,1,3,5,6,3,5,67,123.32,34.5,'python']
>>> data[0]
2
>>> data[-1]
'python'
>>> data[0:4]
[2, 1, 3, 5]
>>> data[0:10:2]
[2, 3, 6, 5, 123.32]
>>> data = []
>>> data.append(12)
>>> data
[12]
>>> data.append(10)
>>> data
[12, 10]
>>> data.append(15)
>>> data.append(25)
>>> data.append(2)
>>> data
[12, 10, 15, 25, 2]
>>> data.append(21,26,33,32,17)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    data.append(21,26,33,32,17)
TypeError: append() takes exactly one argument (5 given)
>>> data + 21,26,33,32,17
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    data + 21,26,33,32,17
TypeError: can only concatenate list (not "int") to list
>>> data + [21,26,33,32,17]
[12, 10, 15, 25, 2, 21, 26, 33, 32, 17]
>>> data
[12, 10, 15, 25, 2]
>>> data.append([21,26,33,32,17])
>>> data
[12, 10, 15, 25, 2, [21, 26, 33, 32, 17]]
>>> del data[-1]
>>> data
[12, 10, 15, 25, 2]
>>> data.extend([21,26,33,32,17])
>>> data
[12, 10, 15, 25, 2, 21, 26, 33, 32, 17]
>>> data.insert(1,100)
>>> data
[12, 100, 10, 15, 25, 2, 21, 26, 33, 32, 17]
>>> data[1] = 200
>>> data
[12, 200, 10, 15, 25, 2, 21, 26, 33, 32, 17]
>>> data[1:3] = 5
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    data[1:3] = 5
TypeError: can only assign an iterable
>>> data[1:3] = 5,6
>>> data
[12, 5, 6, 15, 25, 2, 21, 26, 33, 32, 17]
>>> data.pop()
17
>>> data
[12, 5, 6, 15, 25, 2, 21, 26, 33, 32]
>>> data.pop(4)
25
>>> data
[12, 5, 6, 15, 2, 21, 26, 33, 32]
>>> data.remove(2)
>>> data
[12, 5, 6, 15, 21, 26, 33, 32]
>>> data.extend([11,13,3,34,14,12,5,26,12])
>>> data
[12, 5, 6, 15, 21, 26, 33, 32, 11, 13, 3, 34, 14, 12, 5, 26, 12]
>>> data.count(3)
1
>>> data.count(12)
3
>>> data.index(11)
8
>>> data.index(12)
0
>>> data.index(12,1)
13
>>> data.index(12,14)
16
>>> data[::-1]
[12, 26, 5, 12, 14, 34, 3, 13, 11, 32, 33, 26, 21, 15, 6, 5, 12]
>>> sorted(data)
[3, 5, 5, 6, 11, 12, 12, 12, 13, 14, 15, 21, 26, 26, 32, 33, 34]
>>> sorted(data, reverse=True)
[34, 33, 32, 26, 26, 21, 15, 14, 13, 12, 12, 12, 11, 6, 5, 5, 3]
>>> data
[12, 5, 6, 15, 21, 26, 33, 32, 11, 13, 3, 34, 14, 12, 5, 26, 12]
>>> data.sort()
>>> data
[3, 5, 5, 6, 11, 12, 12, 12, 13, 14, 15, 21, 26, 26, 32, 33, 34]
>>> data = ['python',12,12.5]
>>> sorted(data)
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    sorted(data)
TypeError: '<' not supported between instances of 'int' and 'str'
>>> for item in data:
	print(item)

	
python
12
12.5
>>> data[0]
'python'
>>> data[1]
12
>>> for i in range(len(data)):
	print(i, data[i])

	
0 python
1 12
2 12.5
>>> for i, item in enumerate(data):
	print(i, item)

	
0 python
1 12
2 12.5
>>> for i, item in enumerate(data, start=1):
	print(i, item)

	
1 python
2 12
3 12.5
>>> even = []
>>> for i in range(51):
	if i % 2 == 0:
		even.append(i)

		
>>> even
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50]
>>> even = [for i in range(1,10)]
SyntaxError: invalid syntax
>>> even = [i for i in range(1,10)]
>>> even
[1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> even = [i for i in range(1,51) if i % 2 == 0]
>>> even
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50]
>>> even = [(i,j) for i in range(1,11) for j in range(1,11)]
>>> even
[(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (1, 9), (1, 10), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7), (2, 8), (2, 9), (2, 10), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7), (3, 8), (3, 9), (3, 10), (4, 1), (4, 2), (4, 3), (4, 4), (4, 5), (4, 6), (4, 7), (4, 8), (4, 9), (4, 10), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6), (5, 7), (5, 8), (5, 9), (5, 10), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6), (6, 7), (6, 8), (6, 9), (6, 10), (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6), (7, 7), (7, 8), (7, 9), (7, 10), (8, 1), (8, 2), (8, 3), (8, 4), (8, 5), (8, 6), (8, 7), (8, 8), (8, 9), (8, 10), (9, 1), (9, 2), (9, 3), (9, 4), (9, 5), (9, 6), (9, 7), (9, 8), (9, 9), (9, 10), (10, 1), (10, 2), (10, 3), (10, 4), (10, 5), (10, 6), (10, 7), (10, 8), (10, 9), (10, 10)]
>>> data = [(i,j) for i in range(1,11) for j in range(1,5) if i == j ]
>>> data
[(1, 1), (2, 2), (3, 3), (4, 4)]
>>> 