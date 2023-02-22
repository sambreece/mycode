#!/usr/bin/env python3
#Challenge 41, Dictionaries

loop = True
valid = False

#defining dictionary
marvelchars= {
"Starlord":
  {"real name": "peter quill",
  "powers": "dance moves",
  "archenemy": "Thanos"},

"Mystique":
  {"real name": "raven darkholme",
  "powers": "shape shifter",
  "archenemy": "Professor X"},

"Hulk":
  {"real name": "bruce banner",
  "powers": "super strength",
  "archenemy": "adrenaline"}
             }

while loop: 
    #User inputs and validation
    while not valid:
        char_name  = input(" Which character do you want to know about? (Starlord, Mystique, Hulk)").capitalize()
        char_stat = input(" What statistic do you want to know about? (real name, powers, archenemy)").lower()
        
        if char_name in marvelchars and  char_stat in marvelchars[char_name]:
            valid = True
        else:
            print("Invalid input, please review the accepted inputs.")
    #printing requested info to user
    print(f"{char_name}'s {char_stat} is: {marvelchars[char_name][char_stat]}")

    #check if the user wants to go again
    keep_running = input("Would you like to know more? (Y/n)")

    if keep_running != "Y":
        loop = False
