Python 3.8.8 (tags/v3.8.8:024d805, Feb 19 2021, 13:18:16) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x = [101,102,103,104,105]
>>> names = ['Ram','Shyam','Gopal','Aman','Pooja']
>>> for i, j in x, names:
	print(i,j)

	
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    for i, j in x, names:
ValueError: too many values to unpack (expected 2)
>>> for i, j in zip(x, names):
	print(i,j)

	
101 Ram
102 Shyam
103 Gopal
104 Aman
105 Pooja
>>> zip(x, names)
<zip object at 0x000001FDF56E8800>
>>> list(zip(x, names))
[(101, 'Ram'), (102, 'Shyam'), (103, 'Gopal'), (104, 'Aman'), (105, 'Pooja')]
>>> names = ['Ram','Shyam','Gopal','Aman']
>>> x
[101, 102, 103, 104, 105]
>>> names
['Ram', 'Shyam', 'Gopal', 'Aman']
>>> list(zip(x, names))
[(101, 'Ram'), (102, 'Shyam'), (103, 'Gopal'), (104, 'Aman')]
>>> import itertools
>>> itertools.zip_longest(x,names)
<itertools.zip_longest object at 0x000001FDF56DB950>
>>> list(itertools.zip_longest(x,names))
[(101, 'Ram'), (102, 'Shyam'), (103, 'Gopal'), (104, 'Aman'), (105, None)]
>>> itertools.combinations(x,3)
<itertools.combinations object at 0x000001FDF56DB950>
>>> list(itertools.combinations(x,3))
[(101, 102, 103), (101, 102, 104), (101, 102, 105), (101, 103, 104), (101, 103, 105), (101, 104, 105), (102, 103, 104), (102, 103, 105), (102, 104, 105), (103, 104, 105)]
>>> list(itertools.permutations(x, 3))
[(101, 102, 103), (101, 102, 104), (101, 102, 105), (101, 103, 102), (101, 103, 104), (101, 103, 105), (101, 104, 102), (101, 104, 103), (101, 104, 105), (101, 105, 102), (101, 105, 103), (101, 105, 104), (102, 101, 103), (102, 101, 104), (102, 101, 105), (102, 103, 101), (102, 103, 104), (102, 103, 105), (102, 104, 101), (102, 104, 103), (102, 104, 105), (102, 105, 101), (102, 105, 103), (102, 105, 104), (103, 101, 102), (103, 101, 104), (103, 101, 105), (103, 102, 101), (103, 102, 104), (103, 102, 105), (103, 104, 101), (103, 104, 102), (103, 104, 105), (103, 105, 101), (103, 105, 102), (103, 105, 104), (104, 101, 102), (104, 101, 103), (104, 101, 105), (104, 102, 101), (104, 102, 103), (104, 102, 105), (104, 103, 101), (104, 103, 102), (104, 103, 105), (104, 105, 101), (104, 105, 102), (104, 105, 103), (105, 101, 102), (105, 101, 103), (105, 101, 104), (105, 102, 101), (105, 102, 103), (105, 102, 104), (105, 103, 101), (105, 103, 102), (105, 103, 104), (105, 104, 101), (105, 104, 102), (105, 104, 103)]
>>> for i,item in enumerate(x):
	print(i, item)

	
0 101
1 102
2 103
3 104
4 105
>>> for i,item in enumerate(x, 1):
	print(i, item)

	
1 101
2 102
3 103
4 104
5 105
>>> x
[101, 102, 103, 104, 105]
>>> for i,item in enumerate(zip(x, names), 1):
	print(i, item)

	
1 (101, 'Ram')
2 (102, 'Shyam')
3 (103, 'Gopal')
4 (104, 'Aman')
>>> 