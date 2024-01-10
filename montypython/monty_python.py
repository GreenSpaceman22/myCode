#!/usr/bin/env python3

def main():

    round = 0
    answer = " "
    
    while round<3 and answer != "Brian":
        round = round + 1
        print('Finish the movie title: "Monty Python\'s The Life of _____"')
        answer = input("You're guess: ")
        answer = answer.capitalize()

        if answer == "Brian":
            print("Correct!")
            break
        elif round == 3:
            print("Sorry, the answer was Brian.")
            break
        else:
            print("Sorry! try again.")

main()
