################### Scope ####################

# enemies = 1


# def increase_enemies():
#    enemies = 2
#    print(f"enemies inside function: {enemies}")


# increase_enemies()
# print(f"enemies outside function: {enemies}")


# Local Scope
# def drink_potion():
#     potion_strength = 2
#     print(potion_strength)
#
#
# drink_potion()
# print(potion_strength) # Error

# Global Scope
# player_health = 10


# def drink_potion():
#     potion_strength = 2
#     print(player_health)
#
#
# drink_potion()

# There is no Block Scope
# game_level = 3
# enemies = ["Skeleton", "Zombie", "Alien"]
#
# if game_level < 5:
#     new_enemy = enemies[0]
#
# print(new_enemy)


# Modifying Global Scope

# enemies = 1
# def increase_enemies():
#     global enemies
#     enemies = ["Skeleton", "Zombie", "Alien"]
#     print(f"enemies inside function: {enemies}")

# increase_enemies()
# print(f"enemies outside function: {enemies}")

# enemies = 1
#
#
# def increase_enemies():
#     print(f"enemies inside function: {enemies}")
#     return enemies + 1
#
#
# enemies = increase_enemies()
# print(f"enemies outside function: {enemies}")

# Global Constants
# PI = 3.14159
# URL = "https://www.google.com"
# TWITTER_HANDLE = "@yu_angela"


# def calc():
#     print(PI)
#

# calc()

i = 50


def foo():
    i = 100
    return i


foo()
print(i)


def bar():
    my_variable = 9

    if 16 > 9:
        my_variable = 16

    print(my_variable)


bar()
