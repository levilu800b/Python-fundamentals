# while loop
# while loop is used to execute a block of statements repeatedly until a given a condition is satisfied.
# It tests the condition before executing the loop body.
# Syntax:
# while condition:
#     statement(s)

# Example 1: Print i as long as i is less than 6:

i = 1
while i < 6:
    print(i)
    i += 1

# Example 2: Print i as long as i is less than 6, and i is not 3:

i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1