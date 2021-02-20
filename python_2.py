Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x = 2
>>> y = 12
>>> print(x + y)
14
>>> print x + y
14
>>> print("Sum is",x+y)
('Sum is', 14)
>>> print "Sum is",x+y
Sum is 14
>>> input("Enter your age : ")
Enter your age : 20
20
>>> input("Enter your name : ")
Enter your name : Ram

Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    input("Enter your name : ")
  File "<string>", line 1, in <module>
NameError: name 'Ram' is not defined
>>> raw_input("Enter your name : ")
Enter your name : Ram
'Ram'
>>> str(input("Enter your name : "))
Enter your name : Ram

Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    str(input("Enter your name : "))
  File "<string>", line 1, in <module>
NameError: name 'Ram' is not defined
>>> play = True
>>> True = False
>>> print(play)
True
>>> play = True
>>> print(play)
False
>>> game = True
>>> if game == True:
	print("Let's play")

	
Let's play
>>> True = False
>>> game = True
>>> if game == True:
	print("Let's play")
else:
	print("Exit Game")

	
Let's play
>>> if game:
	print("Let's play")
else:
	print("Exit Game")

	
Exit Game
>>> 12 / 7
1
>>> 12 / float(7)
1.7142857142857142
>>> 
