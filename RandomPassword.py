import random
import string
import numpy as np


def getdata():
    alpha1 = string.ascii_lowercase
    alpha2 = string.ascii_uppercase
    num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    symb = ['!', '@', '#', '$', '%', '^', '&', '*']
    rand1 = random.choice(alpha1)
    rand2 = random.choice(alpha2)
    rand3 = random.choice(symb)
    rand4 = str(random.choice(num))
    paswrd = str(rand1 + rand2 + rand3 + rand4)
    if rand1 in paswrd and rand3 in paswrd and rand4 in paswrd and rand2 in paswrd:
        rand1 = random.choice(alpha1)
        rand3 = random.choice(symb)
        rand4 = random.choice(num)
        newpass = paswrd+rand1+rand2+rand3+str(rand4)

    print("Your new password is : ", newpass)
getdata()
