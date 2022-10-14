Gkdict= {"up":"lucknow","uk":"dehradun","punjab":"chandigarh","karnataka":"bangalore","goa":"panjim"}
userinput = ""
for key,value in Gkdict.items():
    while userinput != 'Exit':
        userinput = str(input("Which state capital you would like to know ?"))
        usrlwr = userinput.lower()
        if usrlwr in Gkdict.keys():
            print(f"{userinput} " "capital is : "+ str(Gkdict.get(usrlwr)))
            print('Enter "Exit" to end the quiz')
        else:
            print("Sorry no such data found!! Try again")
            print('Enter "Exit" to end the quiz')

print('Congrats!! you have finished the learning')





