import random

cpu = random.randint(1,100)
count = 0
while True:
    guess = int(input("Enter the number : "))

    if cpu == guess:
        print("Congrats, you guessed the number")
        break
    elif cpu > guess:
        print("Number is smaller")
        count += 1
    elif cpu < guess:
        print("Number is greater")
        count += 1

    if count == 5:
        print("You lose, Number was",cpu)
        break
