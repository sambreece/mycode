#!usr/bin/env python3

# MysteryDish
# Sam Breece

#Foods: pizza, pho, paella, curry, tacos, sushi, spaghetti, hamburger

import random 
from dishes import dishes

max_guesses = 10
guesses = 0

def main():
    play = explain_rules()
    play_game(play)

def play_game(play):
    while play:
        mystery_dish = random.choice(dishes)
        guess_properties(mystery_dish)
        guess_mystery_dish(mystery_dish)
        play = guess_mystery_dish(mystery_dish) 

def explain_rules(mystery_dish):
    print(f"To win this game, you must determine the mystery dish by making guesses about its properties. After {max_guesses} guesses, you must guess the mystery dish in one try. ")
    
    #return if user wants to play
    return True if input("Are you up for the challenge?(yes/no) \n>").lower() == "yes" else False

def guess_properties(mystery_dish): 
    while guesses < max_guesses:
        guesses += 1
        print(f"Current guess: {guesses}")
    
        # What property of the food would you like to guess? (type(2), main ingredients(4), colors(3), country of origin(1))
        while True:
            #update this to have properties and their quantity come from a list
            property = input(f"What propery of the dish would you like to guess? \
                \nOptions: \
                \nType (2), main ingredients (4), colors (2), temperature when served (1), country of origin (1) \n> ")
    
            #validate the user's input is from the list, otherwise tell them it's invalid and make them choose again
                #if property in list of properties, break 
        
        #handle guessing property, decide how those output strings should look
        #should i let them duplicate guesses? decide this
        
        #print remaining number of guesses
        
            

def guess_mystery_dish(mystery_dish):
    #let user guess the mystery dish
    final_guess = input("The time has come. Guess the mystery food. \n>").lower()
    
    #check answer
    if final_guess == mystery_dish:
        print("Congratulations! You won!")
    else:
        print(f"You lose, and the mystery dish dissappears into the ether, nameless. \n \
        Days later, it comes to you in a dream. It was {mystery_dish['name']}.")
    
    #return if user wants to play again
    return True if input("Do you want to play again?(yes/no) \n>").lower() == "yes" else False   
