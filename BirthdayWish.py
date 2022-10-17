import datetime

from playsound import playsound

userset = input("set birthday reminder : HH:MM:SS:PM/AM \n")
usrhr = userset[0:2]  # slicing to get HH from user input
usrmm = userset[3:5]  # slicing to get MM from user input
usrss = userset[6:8]  # slicing to get SS from user input
usrtz = userset[9:11].upper()  # slicing to get AM/PM from user input
while True:
    currntm = datetime.datetime.now()
    currhr = currntm.strftime("%I") # extract only HH from current time
    currmm = currntm.strftime("%M") # extract only MM from current time
    currss = currntm.strftime("%S") # extract only SS from current time
    currtz = currntm.strftime("%p") # extract only AM/PM from current time
    if usrtz == currtz:
        if usrhr == currhr:
            if usrmm == currmm:
                if usrss == currss:
                    print("wake up")
                    playsound('audio.mp3')
                    break
