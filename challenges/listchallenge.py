#!/usr/bin/env python3

heroes= ["Spiderman", "Batman", "Black Panther", "Wonder Woman", "Storm"]

# PART 1
# Print out your favorite character from this list! The output would look something like:
# My favorite character is Black Panther!
print(f"Part 1: My favorite character is {heroes[3]}")

# PART 2
# Ask the user to pick a number between 1 and 100.
# Convert the input into an integer.

MAX_VALUE = 100
MIN_VALUE = 0
user_num = -1

while True:
    user_num = input("Choose a number between 0 and 100 (inclusive): ")
    if user_num.isnumeric() and (int(user_num) >= MIN_VALUE and int(user_num) <= MAX_VALUE):
        user_num = int(user_num)
        break
    else:
        print(f"Invalid input: {user_num}. Please try again.")

nums= [1, -5, 56, 987, 0]

# PART 3
# check out https://docs.python.org/3/library/functions.html or go to Google
# use a built-in function to find which integer in nums is the biggest.
# then, print out that number!
print(f"Largest element is: {max(nums)}")
