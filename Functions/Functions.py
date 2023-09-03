# functions

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def calculator(a, b, operation):
    if operation == "+":
        return add(a, b)
    elif operation == "-":
        return subtract(a, b)
    elif operation == "*":
        return multiply(a, b)
    elif operation == "/":
        return divide(a, b)
    else:
        return "Invalid operation"

print(calculator(2, 3, "+"))
print(calculator(2, 3, "-"))
print(calculator(2, 3, "*"))
print(calculator(2, 3, "/"))
print(calculator(2, 3, "a"))