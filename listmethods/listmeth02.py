#!/usr/bin/env python3

#declare lists
proto = ["ssh", "http", "https"]
protoa = ["ssh", "http", "https"]


#print proto list
print(proto)

proto.append("dns") # this line will add "dns" to the end of our list
protoa.append("dns") # this line will add "dns" to the end of our list

#print proto list
print(proto)

proto2 = [ 22, 80, 443, 53 ] # a list of common ports
proto.extend(proto2) # pass proto2 as an argument to the extend method

#print proto list (with proto2 list extended to it)
print(proto)

#print protoa list with proto2 appended to it
protoa.append(proto2) # pass proto2 as an argument to the append method
print(protoa)


#count number of times http is on list and print
print(protoa.count("http"))

#reverse protoa list and print
protoa.reverse()
print(protoa)
