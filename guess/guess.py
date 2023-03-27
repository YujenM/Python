import random
def main():
    try:
        user=int(input("choose the level from 1-3: "))
        new_user=level(user)
    except ValueError:
        print("enter integer")
    except UnboundLocalError:
        print("enter number from 1-4")
def level(user):
    
    if user==1:
        number=random.randint(1,10)
    elif user==2:
        number=random.randint(1,100)
    elif user==3:
        number=random.randint(1,1000)
    return number


if __name__=="__main__":
    main()