#!usr/bin/env python3

# MysteryDish
# Sam Breece

#Foods: pizza, pho, paella, curry, tacos, sushi, spaghetti, hamburger

import random 
from dishes import dishes

max_guesses = 10

def main():
    play = explain_rules()
    play_game(play)

def play_game(play):
    while play:
        mystery_dish = random.choice(dishes)
        guess_properties(mystery_dish)
        play = guess_mystery_dish(mystery_dish) 

def explain_rules():
    print(f"To win this game, you must determine the mystery dish by making guesses about its properties.\nAfter {max_guesses} opportunities to gather information, you must guess the mystery dish in one try. ")
    
    #return if user wants to play
    return True if input("Are you up for the challenge?(yes/no) \n> ").lower() == "yes" else False

def guess_properties(mystery_dish): 
    guesses = 0
    while guesses < max_guesses:
        guesses += 1
        print(f"Current guess: {guesses}.")
    
        # What property of the food would you like to guess? (type(2), ingredients(4), colors(3), country of origin(1))
        while True:
            #update this to have properties and their quantity come from a list
            property = input(f"What propery of the dish would you like to guess? \
                \nOptions: \
                \nType, ingredients, colors, temperature when served, country of origin \
                \nIf you're ready to guess early, input 'guess'. \n> ").lower()
    
            #validate the user's input is from the list, otherwise tell them it's invalid and make them choose again
            #if property in list of properties, break 
            if property in mystery_dish.keys():
                # let them guess property
                property_guess = input(f"Guess about the dishes' {property}.\n> ").lower()
                if property_guess in mystery_dish[property]:
                    print("Correct!")
                else:
                    print("Wrong!")
                #print remaining number of guesses
                print(f"Guesses remaining: {max_guesses - guesses}.")        
                break
            elif property == "guess":
                print("Wow, looks like you're ready to guess early!")
                guesses = max_guesses
                break
            else: 
                print("You can't guess about that property!")
        
            #handle guessing property, decide how those output strings should look
            #should i let them duplicate guesses? decide this
        
            

def guess_mystery_dish(mystery_dish):
    #let user guess the mystery dish
    final_guess = input("The time has come. Guess the mystery food. \n> ").lower()
    
    #check answer
    if final_guess == mystery_dish:
        print("Congratulations! You won!")
    else:
        print(f"You lose, and the mystery dish dissappears into the ether, nameless.  \
        \nDays later, it comes to you in a dream. It was {mystery_dish['name']}.")
    
    #return if user wants to play again
    return True if input("Do you want to play again?(yes/no) \n> ").lower() == "yes" else False   

if __name__ == "__main__":
    main()
