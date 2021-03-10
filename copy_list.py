Python 3.8.8 (tags/v3.8.8:024d805, Feb 19 2021, 13:18:16) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> data = [3,4,4,2,4,6,7,4]
>>> data_1 = data
>>> data_1[0] = 30
>>> data
[30, 4, 4, 2, 4, 6, 7, 4]
>>> data_1
[30, 4, 4, 2, 4, 6, 7, 4]
>>> data_1 is data
True
>>> data[:]
[30, 4, 4, 2, 4, 6, 7, 4]
>>> data
[30, 4, 4, 2, 4, 6, 7, 4]
>>> data_2 = data[:]
>>> data is data_1
True
>>> data is data_2
False
>>> data == data_1
True
>>> data == data_2
True
>>> data_2[0] = 300
>>> data_2
[300, 4, 4, 2, 4, 6, 7, 4]
>>> data
[30, 4, 4, 2, 4, 6, 7, 4]
>>> data_1
[30, 4, 4, 2, 4, 6, 7, 4]
>>> data_3 = data.copy()
>>> #Shallow Copy
>>> data = [2,1,4,65,6,[4,2,4,6,7]]
>>> data_1 = data.copy()
>>> data_1 is data
False
>>> data_1[-1]
[4, 2, 4, 6, 7]
>>> data_1[-1][0] = 10
>>> data_1
[2, 1, 4, 65, 6, [10, 2, 4, 6, 7]]
>>> data
[2, 1, 4, 65, 6, [10, 2, 4, 6, 7]]
>>> data[-1]
[10, 2, 4, 6, 7]
>>> data[-1][0]
10
>>> data_1[0]
2
>>> data[0]
2
>>> data_1[0] = 200
>>> data_1
[200, 1, 4, 65, 6, [10, 2, 4, 6, 7]]
>>> data
[2, 1, 4, 65, 6, [10, 2, 4, 6, 7]]
>>> data_1[-1][0] = 100
>>> data_1
[200, 1, 4, 65, 6, [100, 2, 4, 6, 7]]
>>> data
[2, 1, 4, 65, 6, [100, 2, 4, 6, 7]]
>>> import copy
>>> data_4 = copy.deepcopy()
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    data_4 = copy.deepcopy()
TypeError: deepcopy() missing 1 required positional argument: 'x'
>>> data_4 = copy.deepcopy(data)
>>> data_4
[2, 1, 4, 65, 6, [100, 2, 4, 6, 7]]
>>> data
[2, 1, 4, 65, 6, [100, 2, 4, 6, 7]]
>>> data_4[-1]
[100, 2, 4, 6, 7]
>>> data_4[-1][0] = 10
>>> data_4
[2, 1, 4, 65, 6, [10, 2, 4, 6, 7]]
>>> data
[2, 1, 4, 65, 6, [100, 2, 4, 6, 7]]
>>> 