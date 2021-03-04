from datetime import datetime

chat = True
while chat:
    #chat application
    msg = input("Enter your message : ")

    if msg == "hello" or msg == "hi" or msg == "hey" or msg == "hi there":
        print("Hello User")
    elif msg == "date":
        d = datetime.now().date()
        print(d.strftime('%d/%m/%y'))
    elif msg == "time":
        t = datetime.now().time()
        print(t.strftime('%H:%M:%S, %p'))
    elif msg == "bye":
        print("Bye User")
        chat = False
    else:
        print("I don't understand")
