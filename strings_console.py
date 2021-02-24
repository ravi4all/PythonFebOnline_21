Python 3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:44:55) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> text = "hello world"
>>> text[0]
'h'
>>> text[7]
'o'
>>> len(text)
11
>>> text[10]
'd'
>>> text[-1]
'd'
>>> text[0:4]
'hell'
>>> text[4:8]
'o wo'
>>> text[4:10]
'o worl'
>>> text[:]
'hello world'
>>> #text[start:stop], text[index:pos], text[lowerbound:upperbound]
>>> text[4:0]
''
>>> #text[start:stop:step = +1]
>>> text[0:4]
'hell'
>>> text[4:0:-1]
'olle'
>>> text[0:]
'hello world'
>>> text[:6]
'hello '
>>> text[0:100]
'hello world'
>>> text[11]
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    text[11]
IndexError: string index out of range
>>> text[0:10:2]
'hlowr'
>>> text[-1:-4:-1]
'dlr'
>>> text[-4:-1]
'orl'
>>> text[::-1]
'dlrow olleh'
>>> id(text)
1926160126576
>>> chr
<built-in function chr>
>>> ord
<built-in function ord>
>>> chr(97)
'a'
>>> chr(65)
'A'
>>> chr(98)
'b'
>>> chr(197)
'Å'
>>> chr(191)
'¿'
>>> ord('z')
122
>>> ord('Z')
90
>>> ord('+)
    
SyntaxError: EOL while scanning string literal
>>> ord('+')
43
>>> ord('@')
64
>>> ord('a')
97
>>> ord('b')
98
>>> chr(10)
'\n'
>>> chr(11)
'\x0b'
>>> chr(12)
'\x0c'
>>> ord('a')
97
>>> bin(ord('a'))
'0b1100001'
>>> bin(ord('c'))
'0b1100011'
>>> bin(ord('z'))
'0b1111010'
>>> bin(1)
'0b1'
>>> bin(0)
'0b0'
>>> bin(10)
'0b1010'
>>> bin(100)
'0b1100100'
>>> bin(1000)
'0b1111101000'
>>> bin(97)
'0b1100001'
>>> dir(text)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> text
'hello world'
>>> text.upper()
'HELLO WORLD'
>>> text.capitalize()
'Hello world'
>>> text.title()
'Hello World'
>>> text.swapcase()
'HELLO WORLD'
>>> text.lower()
'hello world'
>>> text.startswith('Hello')
False
>>> text.startswith('hello')
True
>>> text.startswith('h')
True
>>> text.startswith('h',1)
False
>>> text.endswith('?')
False
>>> text.endswith('!')
False
>>> text.endswith('.')
False
>>> text.endswith('d')
True
>>> text.index('o')
4
>>> text.count('o')
2
>>> text.index('o',0)
4
>>> text.index('o',5)
7
>>> text.index('z')
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    text.index('z')
ValueError: substring not found
>>> text.find('o')
4
>>> text.find('o',5)
7
>>> text.find('z')
-1
>>> 