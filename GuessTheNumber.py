import random

def rand(x):
    randnum = random.randint(1, x)
    user = 0
    while user != randnum:
        user = int(input(f'Guess the number b/w 1 to {x}: '))
        if(user == randnum):
            print("Horry!! Your guess is right")
        else:
            print("oops!! try again")

rand(10)