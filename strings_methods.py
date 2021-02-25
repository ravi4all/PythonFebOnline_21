Python 3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:44:55) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> text = "hello world, this is python"
>>> text[0]
'h'
>>> text[0:5]
'hello'
>>> text[-1]
'n'
>>> text.upper()
'HELLO WORLD, THIS IS PYTHON'
>>> text.capitalize()
'Hello world, this is python'
>>> text.title()
'Hello World, This Is Python'
>>> text.casefold()
'hello world, this is python'
>>> "hello" == "Hello"
False
>>> text.casefold() == "Hello world, this is python"
False
>>> text.isalpha()
False
>>> text.isascii()
True
>>> text.islower()
True
>>> text.isupper()
False
>>> text.isnumeric()
False
>>> text.replace('hello', 'bye')
'bye world, this is python'
>>> text
'hello world, this is python'
>>> del text[0]
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    del text[0]
TypeError: 'str' object doesn't support item deletion
>>> text[0] = 'b'
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    text[0] = 'b'
TypeError: 'str' object does not support item assignment
>>> text
'hello world, this is python'
>>> text.replace('python', 'java')
'hello world, this is java'
>>> text
'hello world, this is python'
>>> #text.find(sub, start=0)
>>> text.find('o')
4
>>> text.find('o', 5)
7
>>> text.find('o', 8)
25
>>> text.rfind('o')
25
>>> text.rindex('o')
25
>>> text.split()
['hello', 'world,', 'this', 'is', 'python']
>>> #tokenization - split string into a list of words
>>> text.split(',')
['hello world', ' this is python']
>>> x = ['hello', 'world,', 'this', 'is', 'python']
>>> x
['hello', 'world,', 'this', 'is', 'python']
>>> ' '.join(x)
'hello world, this is python'
>>> '-'.join(x)
'hello-world,-this-is-python'
>>> '#'.join(x)
'hello#world,#this#is#python'
>>> text = "   hello, world   "
>>> text.strip()
'hello, world'
>>> #trimming - remove leading and trailing spaces
>>> text.lstrip()
'hello, world   '
>>> text.rstrip()
'   hello, world'
>>> text.strip()
'hello, world'
>>> text = "###hello, world   "
>>> text.strip()
'###hello, world'
>>> text.strip('#')
'hello, world   '
>>> text = text.strip('#')
>>> text
'hello, world   '
>>> text = text.rstrip()
>>> text
'hello, world'
>>> text = '1234343'
>>> type(text)
<class 'str'>
>>> text.replace(2,5)
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    text.replace(2,5)
TypeError: replace() argument 1 must be str, not int
>>> text.replace('2','5')
'1534343'
>>> text = "hello world, this is python"
>>> len(text)
27
>>> text.center(10)
'hello world, this is python'
>>> text.center(20)
'hello world, this is python'
>>> text.center(27)
'hello world, this is python'
>>> text.center(28)
'hello world, this is python '
>>> text.center(29)
' hello world, this is python '
>>> text.center(39)
'      hello world, this is python      '
>>> text.center(39,'*')
'******hello world, this is python******'
>>> text = text.center(39,'*')
>>> text
'******hello world, this is python******'
>>> text.strip('*')
'hello world, this is python'
>>> text
'******hello world, this is python******'
>>> text = text.strip('*')
>>> text
'hello world, this is python'
>>> text = "HellO"
>>> text.swapcase()
'hELLo'
>>> text.maketrans('!@#$%^&*()')
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    text.maketrans('!@#$%^&*()')
TypeError: if you give only one argument to maketrans it must be a dict
>>> text.maketrans('','','!@#$%^&*()')
{33: None, 64: None, 35: None, 36: None, 37: None, 94: None, 38: None, 42: None, 40: None, 41: None}
>>> table = text.maketrans('','','!@#$%^&*()')
>>> table
{33: None, 64: None, 35: None, 36: None, 37: None, 94: None, 38: None, 42: None, 40: None, 41: None}
>>> text = "Hello world, this is python. Who invented python ??"
>>> text.translate(table)
'Hello world, this is python. Who invented python ??'
>>> table = text.maketrans('','','!@#$%^&*(),.?/')
>>> text.translate(table)
'Hello world this is python Who invented python '
>>> text.zfill(10)
'Hello world, this is python. Who invented python ??'
>>> text.zfill(28)
'Hello world, this is python. Who invented python ??'
>>> len(text)
51
>>> text.zfill(52)
'0Hello world, this is python. Who invented python ??'
>>> text.zfill(59)
'00000000Hello world, this is python. Who invented python ??'
>>> 