#!/usr/bin/python

heroes= ["Spiderman", "Batman", "Black Panther", "Wonder Woman", "Storm"]

# PART 1
# Print out your favorite character from this list! The output would look something like:
# My favorite character is Black Panther!
fav_hero = input(f"Of these heroes: {', '.join(heroes)}, which is your favorite? ")
print(f"Your favorite character is {fav_hero}!")

# PART 2
# Ask the user to pick a number between 1 and 100.
# Convert the input into an integer.
min_num = 1
max_num = 100
num = int(input(f"Please enter a number between {min_num} and {max_num}: "))
print(f"Your number is: {num}")

nums= [1, -5, 56, 987, 0]

# PART 3
# check out https://docs.python.org/3/library/functions.html or go to Google
# use a built-in function to find which integer in nums is the biggest.
# then, print out that number!
largest_num = max(nums)
print(f"The largest number in nums is {largest_num}")

