import random
quiz = {"fastest animal ? ":"cheetah","giraffe tounge color ? ":"purple","mamal that fly ? ":"bat","animal eats only bamboo ? ":"panda"}
userinput2 = ''
score = 0
while userinput2 != 'n' and len(quiz) > 0:
    chances = 5
    userinput1 = ''
    user = ''
    question = random.choice(list(quiz.keys()))
    print(question)
    while chances > 0 and userinput1 != 'n' and user != quiz.get(question):
        print(f"Your have {chances} lives left")
        user = input("enter your answer :").lower()
        if user == quiz.get(question):
            print("correct")
            score = score +1
        else:
            print("wrong")
            chances = chances -1
            userinput1 = input("You want to try again Y/N :").lower()
            if chances == 0:
                print("You loose,correct answer is",quiz.get(question) )
    userinput2 = input("you want to try another quiz ? y/n :")
    del quiz[question]


print("Game ended,your score is : ", score)
