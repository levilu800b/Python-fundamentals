# Instructions

# Banker Roulette - Who will pay the bill today?

# You are going to write a program that will select a random name from a list of names. The person
# selected will have to pay for everybody's food bill.
#
# Important: You are not allowed to use the choice() function.
#
# Line 8 splits the string names_string into individual names and puts them inside a List called names. For this to
# work, you must enter all the names as names followed by comma then space. e.g. name, name, name
#
# Example Input
# Angela, Ben, Jenny, Michael, Chloe
# Note: notice that there is a space between the comma and the next name.
#
# Example Output
# Michael is going to buy the meal today!
# Hint
# You might need the help of the len() function.
# https://stackoverflow.com/questions/1712227/how-do-i-get-the-number-of-elements-in-a-list
#
# Remember that Lists start at index 0! Testing Your Code Check your code is doing what it is supposed to. When
# you're happy with your code, click submit to check your solution. Your program may look like it is failing the
# tests when it isn't. We're using the random functionality in this exercise, so the tests will match different
# outcomes.

# Import the random module here

import random

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

# Get the total number of names in list.

total_names_in_list = len(names)

# Generate random numbers between 0 and the last index.

random_choice = random.randint(0, total_names_in_list - 1)

# Pick out random person from list of names using the random number.

person_who_will_pay = names[random_choice]

# Print the result.

print(f"{person_who_will_pay} is going to buy the meal today!")
