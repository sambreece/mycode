#!/usr/bin/env python3
#ask user for host name
hostname = input("What value should we set for hostname?")
## check host name against expected (any capitalization)
if hostname.lower() == "mtg":
    print("The hostname was found to be mtg")
    print("hostname matches expected config")

#print out as completing script
print("Exiting the script...")
