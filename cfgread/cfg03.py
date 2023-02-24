#!/usr/bin/env python3
## create file object in "r"ead mode
file_name = input("What file should be loaded?")


with open(file_name, "r") as configfile:
    ## readlines() creates a list by reading target
    ## file line by line
    configlist = configfile.readlines()

## file was just auto closed (no more indenting)

## each item of the list now has the "\n" characters back
print(configlist)
print(len(configlist))
