#!usr/bin/env python3

#take user input
while True:    
    num_beers = input("What number of beers would you like to start with? ")
    if num_beers.isdigit():
        num_beers = int(num_beers)
        if num_beers <= 100 and num_beers > 0:
            break
        else:
            print("Must be less than or equal to 100 and greater than zero.")
    else:
        print("Input must be a number less than or equal to 100 and greater than zero.")

for n in range(num_beers, 0, -1):
    print(f"{n} bottles of beer on the wall! \
            \n{n} bottles of beer on the wall! {n} bottles of beer! \
            \nYou take one down, pass it around! \
            \n{n} bottles of beer on the wall!")
