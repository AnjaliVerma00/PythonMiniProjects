
weight = float(input("Your weight in kg: "))
height = float(input("Your height cm:"))
height = height/100
BMI = weight / (height * height)
print("Your BMI is :",BMI)
if BMI <=16:
    print("your are underweight")
elif BMI <=25:
    print("you are healthy")
elif BMI <=30:
    print("you are overweight")
else:
    print("enter valid details")