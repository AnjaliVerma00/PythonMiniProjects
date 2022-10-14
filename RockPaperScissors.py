# r>s,s>p,p>r
import random
# main function to get user input and return values
def mgame():
    user = input(" What;s you chouce? r for rock, p for paper, s for scissors : ")
    comptr= random.choice(['r','p,''s'])
    if user == comptr:
        return ("Tie")
    if play(user,comptr):
        return "You won!"
    return "You lost!"

#below code to check who will win copmptr or user
def play(user,comptr):
    if (user == 'r' and comptr == 's') or (user == 's' and comptr == 'p') or (user == 'p' and comptr == 'r'):
        return True


print(mgame())