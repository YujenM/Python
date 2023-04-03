import random
try:
    user=int(input("choose the level from 1-3: "))
    if user==1:
        number=random.randint(1,10)
    elif user==2:
        number=random.randint(1,100)
    elif user==3:
        number=random.randint(1,1000)
    while True:
        guess = int(input("Guess the number: "))
        if guess == number:
            print("Whoraay!")
            break
        elif guess < number:
            print("Too small")
        else:
            print("Too large")
except ValueError:
    print("enter integer")
except UnboundLocalError:
    print("enter number from 1-4")



