# import random

# random_integer = random.randint(0, 10)
# print(random_integer)

# random_float = random.random() * 5
# print(random_float)

# love_score = random.randint(1, 100)
# print(f"Your love score is {love_score}")

# lists

# states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts",
# "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont",
# "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri",
# "Arkansas", "Michigan", "Florida", "Texas", "Iowa",  "Wisconsin", "California", "Minnesota", "Oregon", "Kansas",
# "West Virginia", "Nevada", "Nebraska",       "Colorado", "North Dakota", "South Dakota", "Montana", "Washington",
# "Idaho", "Wyoming", "Utah",          "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

# print(states_of_america[2])

# states_of_america[1] = "Pencilvania"

# print(states_of_america)

# # add item

# states_of_america.append("leviK")
# print(states_of_america)

# states_of_america.extend("Meron", "Anosh", )

# states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts",
# "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont",
# "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri",
# "Arkansas", "Michigan", "Florida", "Texas", "Iowa",  "Wisconsin", "California", "Minnesota", "Oregon", "Kansas",
# "West Virginia", "Nevada", "Nebraska",       "Colorado", "North Dakota", "South Dakota", "Montana", "Washington",
# "Idaho", "Wyoming", "Utah",          "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

# # IndexError

# num_of_states = len(states_of_america)

# print(states_of_america[num_of_states - 10])

# dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears",
# "Tomatoes", "Celery", "Potatoes"]

# fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]

# vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

# dirty_dozen = [fruits, vegetables]

# fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
# fruits[-1] = "Melons"
# fruits.append("Lemons")
# print(fruits)

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]

print(dirty_dozen[1][1])
