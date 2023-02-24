#!usr/bin/env python3

import random

wordbank= ["indentation", "spaces"]
tlgstudents= ['Albert', 'Anthony', 'Brenden', 'Craig', 'Deja', 'Elihu', 'Eric', 'Giovanni', 'James', 'Joshua', 'Maria', 'Mohamed', 'PJ', 'Philip', 'Sagan', 'Suchit', 'Meka', 'Trey', 'Winton', 'Xiuxiang', 'Yaping']

wordbank.append(4)

#input approach:
num = int(input(f"Choose a number between 1 and {len(tlgstudents)}: "))-1

student_name = tlgstudents[num]

print(f"{student_name} always uses {wordbank[2]} {wordbank[1]} to indent.")


#random name approach:
num = random.randint(0, len(tlgstudents))

student_name = tlgstudents[num]

print(f"Randomly generated: {student_name} always uses {wordbank[2]} {wordbank[1]} to indent.")
