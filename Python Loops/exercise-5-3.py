# Instructions

# Sum of Even Numbers

# You are going to write a program that calculates the sum of all the even numbers from 1 to 100. Thus, the first even number would be 2 and the last one is 100:
#
# i.e. 2 + 4 + 6 + 8 +10 ... + 98 + 100
#
# Important, there should only be 1 print statement in your console output. It should just print the final total and not every step of the calculation.
#
# Hint
# There are quite a few ways of solving this problem, but you will need to use the range() function in any of the solutions.
# Test Your Code
# Check your code is doing what it is supposed to. When you're happy with your code, click submit to check your solution.

# Write your code below this row 👇

#solution 1

total = 0
for number in range(2, 101, 2):
    total += number
print(total)

# Solution 2

total = 0
for number in range(1, 101):
    if number % 2 == 0:
        total += number
print(total)
