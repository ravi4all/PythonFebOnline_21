from datetime import datetime
import webbrowser

helloIntent = ["hi", "hello", "hey", "hi there", "hello there"]
dateIntent = ["tell me date", "date please", "date", "today's date"]
timeIntent = ["time", "tell me time", "time please", "current time"]

chat = True
while chat:
    #chat application
    msg = input("Enter your message : ")
    msg = msg.lower()

    if msg in helloIntent:
        print("Hello User")
    elif msg in dateIntent:
        d = datetime.now().date()
        print(d.strftime('%d/%m/%y'))
    elif msg in timeIntent:
        t = datetime.now().time()
        print(t.strftime('%H:%M:%S, %p'))
    elif msg.startswith('open'):
        web = msg.split()[-1]
        webbrowser.open(web+'.com')
    elif msg == "bye":
        print("Bye User")
        chat = False
    else:
        print("I don't understand")
