# 💪 This is a Difficult Challenge 💪
# Instructions
# Love calculator
# You are going to write a program that tests the compatibility between two people.
#
# To work out the love score between two people:
#
# Take both people's names and check for the number of times the letters in the word TRUE occurs.
#
# Then check for the number of times the letters in the word LOVE occurs.
#
# Then combine these numbers to make a 2 digit number.
#
# For Love Scores less than 10 or greater than 90, the message should be:
#
# "Your score is **x**, you go together like coke and mentos."
# For Love Scores between 40 and 50, the message should be:
#
# "Your score is **y**, you are alright together."
# Otherwise, the message will just be their score. e.g.:
#
# "Your score is **z**."
# e.g.
#
# name1 = "Angela Yu"
# name2 = "Jack Bauer"
# T occurs 0 times
#
# R occurs 1 time
#
# U occurs 2 times
#
# E occurs 2 times
#
# Total = 5
#
# L occurs 1 time
#
# O occurs 0 times
#
# V occurs 0 times
#
# E occurs 2 times
#
# Total = 3
#
# Love Score = 53
#
# Print: "Your score is 53."
#
# Example Input 1
# name1 = "Kanye West"
# name2 = "Kim Kardashian"
# Example Output 1
# Your score is 42, you are alright together.
# Example Input 2
# name1 = "Brad Pitt"
# name2 = "Jennifer Aniston"
# Example Output 2
# Your score is 73.
# e.g. When you hit run, this is what should happen:
#
#
#
# The testing code will check for print output that is formatted like one of the lines below:
#
# "Your score is 47, you are alright together."
# "Your score is 125, you go together like coke and mentos."
# "Your score is 54."
# Score Comparison
# Not sure you're getting the correct score for the exercise? Use this table to check your code's score against mine.
#
# Name 1	Name 2	Score
# Catherine Zeta-Jones     	Michael Douglas    	99
# Brad Pitt	Jennifer Aniston	73
# Prince William	Kate Middleton	67
# Angela Yu	Jack Bauer	53
# Kanye West	Kim Kardashian	42
# Beyonce	Jay-Z	23
# John Lennon	Yoko Ono	18
# Hint
# The lower() function changes all the letters in a string to lowercase.
# https://stackoverflow.com/questions/6797984/how-do-i-lowercase-a-string-in-python
#
# The count() function will give you the number of times a letter occurs in a string.
# https://stackoverflow.com/questions/1155617/count-the-number-occurrences-of-a-character-in-a-string
#
# Test Your Code Check your code is doing what it is supposed to. When you're happy with your code, click submit to
# check your solution.

# 🚨 Don't change the code below 👇
# print("Welcome to the Love Calculator!")
# name1 = input("What is your name? \n")
# name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

# Solution1
# 1. Create a variable called combined_string
# and set it equal to lower case version of name1 + name2
# combined_string = name1.lower() + name2.lower()

# 2. Create a variable called t and set it equal to the number of times the letter "t" occurs in combined_string
# t = combined_string.count("t")

# 3. Create a variable called r and set it equal to the number of times the letter "r" occurs in combined_string
# r = combined_string.count("r")

# 4. Create a variable called u and set it equal to the number of times the letter "u" occurs in combined_string
# u = combined_string.count("u")

# 5. Create a variable called e and set it equal to the number of times the letter "e" occurs in combined_string
# e = combined_string.count("e")

# 6. Create a variable called true and set it equal to the sum of t, r, u, e
# true = t + r + u + e

# 7. Create a variable called l and set it equal to the number of times the letter "l" occurs in combined_string
# l = combined_string.count("l")

# 8. Create a variable called o and set it equal to the number of times the letter "o" occurs in combined_string
# o = combined_string.count("o")

# 9. Create a variable called v and set it equal to the number of times the letter "v" occurs in combined_string
# v = combined_string.count("v")

# 10. Create a variable called e and set it equal to the number of times the letter "e" occurs in combined_string
# e = combined_string.count("e")

# 11. Create a variable called love and set it equal to the sum of l, o, v, e
# love = l + o + v + e

# 12. Create a variable called love_score and set it equal to the concatenation of the strings "Your score is " and the
# string version of the variable love_score (e.g. love_score should be a string, not an integer)
# love_score = int(str(true) + str(love))

# 13. If the love score is less than 10 or greater than 90, print "Your score is **x**, you go together like coke and
# mentos."
# if (love_score < 10) or (love_score > 90):
#   print(f"Your score is {love_score}, you go together like coke and mentos.")
# 14. Else if the love score is between 40 and 50, print "Your score is **y**, you are alright together."
# elif (love_score >= 40) and (love_score <= 50):
# print(f"Your score is {love_score}, you are alright together.")
# 15. Otherwise, print "Your score is **z**."
# else:
# print(f"Your score is {love_score}.")

# Solution2

# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
# 1. Create a variable called combined_string
# and set it equal to lower case version of name1 + name2

combined_string = name1.lower() + name2.lower()

# 2. Create a variable called t and set it equal to the number of times the letter "t" occurs in combined_string
# 3. Create a variable called r and set it equal to the number of times the letter "r" occurs in combined_string
# 4. Create a variable called u and set it equal to the number of times the letter "u" occurs in combined_string
# 5. Create a variable called e and set it equal to the number of times the letter "e" occurs in combined_string
# 6. Create a variable called true and set it equal to the sum of t, r, u, e

true = combined_string.count("t") + combined_string.count("r") + combined_string.count("u") + combined_string.count("e")

# 7. Create a variable called l and set it equal to the number of times the letter "l" occurs in combined_string
# 8. Create a variable called o and set it equal to the number of times the letter "o" occurs in combined_string
# 9. Create a variable called v and set it equal to the number of times the letter "v" occurs in combined_string
# 10. Create a variable called e and set it equal to the number of times the letter "e" occurs in combined_string
# 11. Create a variable called love and set it equal to the sum of l, o, v, e

love = combined_string.count("l") + combined_string.count("o") + combined_string.count("v") + combined_string.count("e")

# 12. Create a variable called love_score and set it equal to the concatenation of the strings "Your score is " and the
# string version of the variable love_score (e.g. love_score should be a string, not an integer)

love_score = int(str(true) + str(love))

if (love_score < 10) or (love_score > 90):
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif (love_score >= 40) and (love_score <= 50):
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")
