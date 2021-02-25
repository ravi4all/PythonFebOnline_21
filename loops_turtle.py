Python 3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:44:55) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import turtle
>>> t = turtle.Pen()
>>> t.shape('turtle')
>>> t.forward(100)
>>> t.left(90)
>>> t.forward(100)
>>> t.left(90)
>>> t.forward(100)
>>> t.left(90)
>>> t.forward(100)
>>> t.left(90)
>>> t.reset()
>>> for i in range(4):
	t.forward(100)
	t.left(90)

	
>>> t.reset()
>>> for i in range(4):
	print(i)

	
0
1
2
3
>>> for i in range(40):
	t.forward(4 * i)
	t.left(45)

	
>>> t.reset()
>>> for i in range(30):
	t.circle(4 * i)
	t.left(45)

	
>>> 