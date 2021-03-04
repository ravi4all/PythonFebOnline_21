#prime number
num = 17

prime = False
for i in range(2,num):
    if num % i == 0:
        #print("Not Prime")
        prime = False
        break
    else:
        prime = True
        #print("Prime")

if prime:
    print("Prime")
else:
    print("Not Prime")
