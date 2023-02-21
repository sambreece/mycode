#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   List - simple list"""

def main():
    # create a list called list1
    list1 = ["cisco_nxos", "arista_eos", "cisco_ios"]

    # display list1
    print(list1)

    #display list[1] 
    print(list1[1])

    #create new list with single item
    list2 = ["juniper"]

    #extend list1 by list2
    list1.extend(list2)

    #display list1, which now contains list2
    print(list1)

    #create third list
    list3 = ["10.1.0.1", "10.2.0.1", "10.3.0.1"]

    #append list3 to list1
    list1.append(list3)

    #display new list1
    print(list1)

    #return just the list of IP addresses
    print(list1[4])

    #display the first item of the IP list
    print(list1[4][0])

#optional challenge below

    #create list of animals

    animal_list = ["Dog", "Cat", "Bird", "Fish", "Cow"]

    print(" ".join(animal_list))



main()

