#!/usr/bin/env python3
"""Number guessing game! User has 5 chances to guess a number between 1 and 100!"""
import random


def main():
    num= random.randint(1,100)

    rounds= 0
    guess= int(input("Guess a number between 1 and 100\n>"))
    
    while rounds < 5 and guess != num:
        # COOL CODE ALERT: what is the purpose of the next four lines?
       
        guess= int(guess)

        if guess > num:
            print("Too high!")
            rounds = rounds + 1
            guess= int(input("Guess a number between 1 and 100\n>"))
        if guess < num:
            print("Too low!")
            rounds = rounds + 1
            guess = int(input("Guess a number between 1 and 100\n>"))
        else:
            print("Correct!")
             

main()

