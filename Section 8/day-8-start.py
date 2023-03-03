# Review:
# Create a function called greet().
# Write 3 print statements inside the function.
# Call the greet() function and run your code.

# def greet():
#   print("Hello Levi")
#   print("How do you do?")
#   print("Isn't the weather nice today?")

# greet()

# function that allows for input

# def greet_with_name(name):
#   print(f"Hello {name}")
#   print(f"How do you do {name}?")

# greet_with_name("Levi")

# function with more than one inputs

# def greet_with(name, location):
#   print(f"Hello {name}")
#   print(f"What is it like in {location}")

# greet_with("Levi", "Sheffield")
# Vs
# greet_with("Sheffield", "Levi")

# functions with keyword arguments

def greet_with(name, location):
  print(f"Hello {name}")
  print(f"What is it like in {location}")

greet_with(name="Levi", location="Mercedes")
# Vs
greet_with(location="Mercedes",name="Levi")