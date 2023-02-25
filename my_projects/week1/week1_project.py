#!usr/bin/env python3

# MysteryDish
# Sam Breece

import random
from os import system, name
from dishes import dishes

max_guesses = 10

def main():
    clear()
    play = explain_rules()
    play_game(play)

def play_game(play):
    while play:
        mystery_dish = random.choice(dishes)
        guess_properties(mystery_dish)
        play = guess_mystery_dish(mystery_dish) 

def explain_rules():
    #diplay rules:
    print(f"To win this game, you must determine the mystery dish by making guesses about its properties.\
        \nBe careful: duplicate guesses will count against you. \
        \nAfter {max_guesses} opportunities to gather information, you must guess the mystery dish in one try. ")
    
    #return if user wants to play
    return True if input("Are you up for the challenge?(yes/no) \n> ").lower() == "yes" else False

def guess_properties(mystery_dish): 
    num_guesses = 0
    guessable_properties = list(mystery_dish.keys())
    guessable_properties.remove('name')
    previous_guesses =[]
    while num_guesses < max_guesses:
        num_guesses += 1
        display_guesses(num_guesses, previous_guesses)
        while True:
            #ask user what property they want to guess 
            property = input(f"\nWhat propery of the dish would you like to guess? \
                \nOptions: {', '.join(guessable_properties)}\
                \nIf you're ready to guess early, input 'guess'. \n> ").lower()
    
            if property in mystery_dish.keys():
                # let user guess property
                property_guess = input(display_property_message(property)).lower()
                #keep country names capitalized
                if property == "origin":
                    property_guess = property_guess.capitalize()

                #check guess
                if property_guess in mystery_dish[property]:
                    status = "correct"
                else:
                    status = "incorrect"
                previous_guesses.append({"property": property, "guess":property_guess,
                                         "status":status})
                break
            elif property == "guess":
                num_guesses = max_guesses
                break
            else: 
                print("You can't guess about that property!")


def display_guesses(num_guesses, previous_guesses):
    clear()
    #display previous guesses 
    if num_guesses == 1:
        print(f"Current guess: {num_guesses}")
    else:
        incorrect_guesses = []
        print("Correct guesses:")
        
        #print correct guesses
        for guess in previous_guesses:
            if guess["status"] == "correct":
                print("\t" + guess["property"]+" : "+guess["guess"])
            else:
                incorrect_guesses.append(guess)
        #if none, print none
        if len(incorrect_guesses) == len(previous_guesses):
            print("\tnone")
        
        #print incorrect guesses
        print("Incorrect guesses:")
        for guess in incorrect_guesses:
            print("\t" + guess["property"]+" : "+guess["guess"])
        #if none, print none
        if len(incorrect_guesses) == 0:
            print("\tnone")
            
        #print overall guess counts 
        print(f"\nCurrent guess: {num_guesses} | Guesses remaining after current: {max_guesses - num_guesses}")
    

def display_property_message(property):
    if property == "first letter":
        message = "Guess the first letter of the mystery dish. \n> "
    elif property == "ingredients":
        message = "Guess the main ingredients. Only the top three ingredients are considered correct. \n> "
    elif property == "colors": 
        message = "Guess the main color of the dish. Only the top two colors are considered correct. \n> "
    elif property == "temperature":
        message = "Guess the temperature of the dish when served. Options: hot, cold, room temperature \n> "
    elif property == "origin":
        message = "Guess the country of origin for the dish. \n> "
    else: 
        message = "Unexpected property."
    return message

def guess_mystery_dish(mystery_dish):
    clear()
    #let user guess the mystery dish
    final_guess = input("The time has come. Guess the mystery food. \n> ").lower()
    
    #check answer
    if final_guess == mystery_dish['name']:
        print("Congratulations! You won!")
    else:
        print(f"You lose, and the mystery dish dissappears into the ether, nameless.  \
        \nDays later, it comes to you in a dream. It was {mystery_dish['name']}.")
    
    #return whether user wants to play again
    return True if input("Do you want to play again?(yes/no) \n> ").lower() == "yes" else False   

def clear():
    #clear terminal
    if name == 'nt':
        system('cls')
    else:
        system('clear')
        
if __name__ == "__main__":
    main()
