#!/usr/bin/env python3

def main():    
    usr_name = input("Please enter your name:\n>") 
              
    usr_name = usr_name.title()    
    usr_date = int(input("Please enter your birth year in YYYY format, e.g 2010:\n>"))
    index = usr_date % 12       
    output = [f"{usr_name} your zodiac sign is Rabbit, you are vigilant, witty, quick-minded, and ingenious.",
            f"{usr_name} your zodiac sign is Rat, you are artistic, sociable, industrious, charming, and intelligent.", 
            f"{usr_name} your zodiac sign is Tiger, you are courageous, enthusiastic, confident, charismatic, and a leader.",
            f"{usr_name} your zodiac sign is Ox, you are strong, thorough, determined, loyal, and reliable.",
            f"{usr_name} your zodiac sign is Dragon, you are talented, powerful, lucky, and successfull.",
            f"{usr_name} your zodiac sign is Snake, you are wise, like to work alone, and determined.",
            f"{usr_name} your zodiac sign is Horse, you are animated, active, and energetic.",
            f"{usr_name} your zodiac sign is Sheep, you are creative, resilient, gentle, mild-mannered, and shy.",
            f"{usr_name} your zodiac sign is Monkey, you are sharp, smart, curious, and mischievious.",
            f"{usr_name} your zodiac sign is Rooster, you are hardworking, resourceful, courageous, and talented.",
            f"{usr_name} your zodiac sign is Dog, you are loyal, honest, cautious, and kind.", 
            f"{usr_name} your zodiac sign is Pig, you are a symbol of wealth, honesty, and practicality."]
    print(output[index])
main()

