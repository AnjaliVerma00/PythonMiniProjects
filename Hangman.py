import random
import string

words = ["NIGHT","MARCH","HAPPY"]


def get_valid(words):
    word = random.choice(words) # random choose from list word
    return word

def hangman():
    lives = 5 #chances given to user
    word = get_valid(words)
    uselttr = set() #creating empty set where used letter will be stored
    wrdltr = set(word)
    alpha = set(string.ascii_uppercase) # sting of alphabet
    while len(wrdltr) >0 and lives > 0: #loop will run until the length of word is 0 and user still has chances
        print("You have used : ", ' '.join(uselttr), 'you have', lives ,'lives left' )
        wordlist = [letter if letter in uselttr else '-' for letter in word] # placing - for places that does not match
        print("current word is :", ' '.join(wordlist))
        user = input("Guess the word :").upper()
        if user in alpha - uselttr: # if letter is not already in used letter then add to used letter set
            uselttr.add(user)
            if user in wrdltr: # of letter in word then remove the word from word
                wrdltr.remove(user)
            else:
                lives = lives - 1 # reducing chances when guess is wrong
        elif user in uselttr:
            print("You already used")
        else:
            print("invalid character")

    if lives == 0:
        print("You lost!! correct word is :" , word)
    else:
        print("Hurray!! you won, word is", word)


hangman()
