import random
from playsound import playsound, PlaysoundException
import time
userinput = 'Y'
while userinput == 'Y':
    userchoice = random.randint(1,6)
    comuterchoice = random.randint(1,6)
    if userchoice > comuterchoice:
        print("You won!! you got", userchoice ,"computer got" , comuterchoice)
    else:
        print("Sorry you loose!! you got", userchoice, "computer got", comuterchoice)

    userinput = input("Do you want to play again ? Y/N : ").upper()

print("Thankyou!!")