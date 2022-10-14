list1 = ["-",'*','+','/',"%"]
qstn = ''
nqstn = ''
while nqstn != 'n':
        num1 = int(input("enter first number : "))
        num2 = int(input("enter Second number : "))
        opertor  = str(input ("What you want to perform ? "))
        if opertor == list1[0]:
            print(list1[0])
            print(f"Your output for {num1} {list1[0]} {num2} is {num1-num2}")
        elif opertor == list1[1]:
            print(f"Your output for {num1} {list1[0]} {num2} is {num1*num2}")
        elif opertor == list1[2]:
            print(f"Your output for {num1} {list1[0]} {num2} is {num1+num2}")
        elif opertor == list1[3]:
            print(f"Your output for {num1} {list1[0]} {num2} is {num1/num2}")
        elif opertor == list1[4]:
            print(f"Your output for {num1} {list1[0]} {num2} is {num1%num2}")
        else:
            print("Invalid operation")
        #qstn =  str(input("do you want to continue ?Y/N"))
        #nqstn = str(qstn.lower())
        while nqstn != 'n' or nqstn != 'y':
            qstn = str(input("do you want to continue ?Y/N"))
            nqstn = str(qstn.lower())
            print("please enter correct data")
            if nqstn == 'n' or nqstn == 'y':
                break
        #continue
print("Thankyou")
