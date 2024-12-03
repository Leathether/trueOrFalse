import random

def generate_random():
    return random.randint(0,1)

def guess_fun():
    guess = input("Guess if we want true or false (0, or 1):  ")
    return int(guess)
    
randy = generate_random()

def check():

    if guess_fun() == randy:
        print("you win!!")
    else: 
        print("Try again")
        check()

check()