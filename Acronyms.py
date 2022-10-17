userinput = input("enter the Phrase :")
word = userinput.split()
print(word)
Acronym = ''
for i in word:
    Acronym += i[0]
print("Acronym is :", Acronym.upper())