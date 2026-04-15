# Practice Questions: Introduction to Python

# 1. Variables and Data Types
#   a) Create a variable named `city` and assign it the value "New York".
#   b) Create a variable named `temperature` and assign it a floating-point value of 25.5.
#   c) Create a variable `is_raining` and assign it a boolean value of `False`.
#   d) Print the type of each variable.

city = "New York"
temperature = 25.5
is_raining = False 

print(type(city))
print(type(temperature))
print(type(is_raining))


# 2. Type Casting
#   a) You are given a string `age_str = "30"`. Convert it to an integer and store it in a variable `age_int`.
#   b) You have an integer `quantity = 5`. Convert it to a string and store it in `quantity_str`.
#   c) You have a float `price = 49.99`. Convert it to an integer (truncating the decimal part) and store it in `price_int`.
#   d) Print the final converted variables and their types.

age_str = "30"
age_int = int(age_str)

quantity = 5
quantity_str = str(quantity)

price = 49.99
price_int = int(price)

print(age_int, type(age_int))
print(quantity_str, type(quantity_str))
print(price_int, type(price_int))


# 3. Basic Input/Output
#   a) Write a program that asks the user for their favorite color.
#   b) Store the input in a variable called `favorite_color`.
#   c) Print a message back to the user, for example: "Your favorite color is [color]!"

favorite_color = input("What is your favorite color? ")
print(f"Your favorite color is {favorite_color}!")


# 4. Comments
#   a) Add a single-line comment above your solution for question 3a explaining what the code does.
#   b) Add a multi-line comment at the top of this file with your name and the date.

# This program asks the user for their favorite color and then prints a message with that color.

"""
  Esha Khalid
  April 15, 2026
"""


# 5. Putting it all together
#   a) Write a small program that asks for the user's name and age (as a string).
#   b) Convert the age to an integer.
#   c) Calculate how old the user will be in 10 years.
#   d) Print a single, formatted message that says: "Hello, [Name]! You are currently [Age] years old. In 10 years, you will be [Future Age] years old."
#   e.g., "Hello, Alice! You are currently 25 years old. In 10 years, you will be 35 years old."

user_name = input("What is your name? ")
user_age_str = input("What is your age? ")

user_age = int(user_age_str)
future_age = user_age + 10
print(f"Hello, {user_name}! You are currently {user_age} years old. In 10 years, you will be {future_age} years old.")

