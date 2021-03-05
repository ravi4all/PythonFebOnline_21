Python 3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:44:55) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
========== RESTART: F:\Batches\Feb\PythonOnlineFebMorning\chat_3.py ==========
Enter your message : bye
Bye User
>>> import webbrowser
>>> msg = "open facebook"
>>> msg.startswith("open")
True
>>> msg.split()
['open', 'facebook']
>>> msg.split()[-1]
'facebook'
>>> web = msg.split()[-1]
>>> 
========== RESTART: F:\Batches\Feb\PythonOnlineFebMorning\chat_3.py ==========
Enter your message : hi
Hello User
Enter your message : hello
Hello User
Enter your message : open facebook
Enter your message : bye
Bye User
>>> import os
>>> os.listdir()
['chat_1.py', 'chat_2.py', 'chat_3.py', 'data_types.png', 'data_types_console.py', 'date_time_console.py', 'exercise_1.py', 'fib_series.py', 'guess_the_number.py', 'if_else_1.py', 'if_else_expression.py', 'loops_turtle.py', 'loop_2.py', 'loop_3.py', 'max_of_3.py', 'pattern_1.py', 'pattern_2.py', 'prime_number.py', 'prime_number_2.py', 'range_function.py', 'stone_paper_scissor.py', 'strings_console.py', 'strings_methods.py', 'strings_notes.txt', 'while_intro.py']
>>> os.getcwd()
'F:\\Batches\\Feb\\PythonOnlineFebMorning'
>>> os.chdir('C:\Users\ASUS PC\Videos')
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
>>> 'c:\new\asus\random'
'c:\new\x07sus\random'
>>> 'c:\\new\\asus\\random'
'c:\\new\\asus\\random'
>>> 'c:/new/asus/random'
'c:/new/asus/random'
>>> r'c:\new\asus\random'
'c:\\new\\asus\\random'
>>> os.chdir(r'C:\Users\ASUS PC\Videos')
>>> os.listdir()
['Captures', 'desktop.ini', 'video_1.mp4', 'video_1.wmv', 'video_2.wmv', 'video_3.wmv']
>>> videos = os.listdir()
>>> import random
>>> os.startfile(random.choice(videos))
>>> os.startfile(random.choice(videos))
>>> intente = ["hi", "hello", "hey", "hi there", "hello there"]
>>> msg = "hey"
>>> msg == intente
False
>>> for item in intente:
	if msg == item:
		print(True)
		break

	
True
>>> #Membership operator - in not in
>>> msg in intente
True
>>> msg = "Hey"
>>> msg in intente
False
>>> x = [1,2,2,4,4,2,2,5]
>>> x[0]
1
>>> x[4]
4
>>> x[3]
4
>>> for i in range(len(x)):
	print(x[i])

	
1
2
2
4
4
2
2
5
>>> for item in x:
	print(item)

	
1
2
2
4
4
2
2
5
>>> 