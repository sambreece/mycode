#!/usr/bin/env python3

#declaring my_list
my_list = [ "192.168.0.5", 5060, "UP" ]

#printing first list item to stdout
print("The first item in the list (IP): " + my_list[0] )

#printing second item to stdout (after converting to str)
print("The second item in the list (port): " + str(my_list[1]) )

#printing third item to stdout
print("The last item in the list (state): " + my_list[2] )

#declaring ip list
iplist = [ 5060, "80", 55, "10.0.0.1", "10.20.30.1", "ssh" ]

#printing ip addresses to console
print("IP addresses: " + iplist[3] + ", and " + iplist[4])
