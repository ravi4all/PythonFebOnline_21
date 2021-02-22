Python 3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:44:55) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x = 12
>>> y = 2
>>> type(x)
<class 'int'>
>>> x = 12.55
>>> type(x)
<class 'float'>
>>> x = "hello"
>>> type(x)
<class 'str'>
>>> x = 'hello'
>>> type(x)
<class 'str'>
>>> x = """hello"""
>>> type(x)
<class 'str'>
>>> text = "hello world"
>>> print(text)
hello world
>>> text = 'hello "world"'
>>> print(text)
hello "world"
>>> text = "hello "world""
SyntaxError: invalid syntax
>>> text = "hello \"world\""
>>> print(text)
hello "world"
>>> #escape character
>>> text = "hello\nworld"
>>> print(text)
hello
world
>>> text = "hello\tworld"
>>> print(text)
hello	world
>>> text = "hello\nworld"
>>> text = "hello'\n'world"
>>> print(text)
hello'
'world
>>> text = "hello\\nworld"
>>> print(text)
hello\nworld
>>> path = "C:\Users\ASUS PC\Saved Games"
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
>>> path = "C:\new\total\asus\next"
>>> print(path)
C:
ew	otalsus
ext
>>> path = "C:\\new\\total\\asus\\next"
>>> print(path)
C:\new\total\asus\next
>>> path = r"C:\new\total\asus\next"
>>> print(path)
C:\new\total\asus\next
>>> #raw string
>>> msg = "hello how are you ?"
>>> msg.encode()
b'hello how are you ?'
>>> msg = "हैलो, कैसे हो ?"
>>> msg.encode()
b'\xe0\xa4\xb9\xe0\xa5\x88\xe0\xa4\xb2\xe0\xa5\x8b, \xe0\xa4\x95\xe0\xa5\x88\xe0\xa4\xb8\xe0\xa5\x87 \xe0\xa4\xb9\xe0\xa5\x8b ?'
>>> text = msg.encode()
>>> type(text)
<class 'bytes'>
>>> text.decode()
'हैलो, कैसे हो ?'
>>> game = True
>>> type(game)
<class 'bool'>
>>> msg = "hello how are you ?"
>>> msg = "hello hw are you ?"
>>> msg[0]
'h'
>>> del msg[0]
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    del msg[0]
TypeError: 'str' object doesn't support item deletion
>>> msg[0] = 'x'
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    msg[0] = 'x'
TypeError: 'str' object does not support item assignment
>>> x = 10
>>> id(x)
3222225644112
>>> id(10)
3222225644112
>>> id(11)
3222225644144
>>> id(12)
3222225644176
>>> type(x)
<class 'int'>
>>> x = "hello"
>>> type(x)
<class 'str'>
>>> x = 10
>>> type(x)
<class 'int'>
>>> x = 10.343
>>> type(x)
<class 'float'>
>>> import sys
>>> sys.getsizeof(x)
24
>>> x
10.343
>>> x = 12
>>> type(x)
<class 'int'>
>>> sys.getsizeof(x)
28
>>> x = "hello"
>>> type(x)
<class 'str'>
>>> sys.getsizeof(x)
54
>>> 