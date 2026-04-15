# Practice Questions: Conditional Statements

# 1. `if` Statement
#   a) Create a variable `score` and set it to a value, e.g., 85.
#   b) Write an `if` statement that prints "Excellent!" if the score is greater than 80.

score = 85
if score > 80:
    print("Excellent!")


# 2. `if-else` Statement
#   a) Create a variable `age` and set it to 16.
#   b) Write an `if-else` statement that prints "You can drive" if age is 18 or older, and "You can't drive yet" otherwise.

age = 16
if age >= 18:
    print("You can drive")
else:
    print("You can't drive yet")


# 3. `if-elif-else` Ladder
#   a) Write a program that checks if a number is positive, negative, or zero.
#   b) Create a variable `number` and test it with different values (e.g., 10, -5, 0).
#   c) Print "Positive", "Negative", or "Zero" accordingly.

number = 10
if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else: 
    print("Zero")


# 4. Nested `if` Statements
#   a) Write a program to check if a person is eligible for a senior citizen discount.
#   b) Create variables `age = 70` and `is_citizen = True`.
#   c) The outer `if` should check if the person is a citizen.
#   d) The inner `if` should check if the person's age is 65 or over.
#   e) Print "Eligible for senior discount" only if both conditions are met. Otherwise, print an appropriate message.

age = 70
is_citizen = True
if is_citizen:
    if age >= 65:
        print("Eligible for senior discount")
    else:
        print("Not eligible for senior discount due to age")
else:
    print("Not eligible for senior discount due to citizenship status")


# 5. Putting it all together
#   a) Create a mini-calculator for two numbers.
#   b) Ask the user for two numbers and an operator (+, -, *, /).
#   c) Use an `if-elif-else` structure to check the operator.
#   d) Perform the calculation and print the result, e.g., "10 + 5 = 15".
#   e) Include a check for division by zero and print an error message if the user tries to divide by 0.

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operator = input("Enter an operator (+, -, *, /): ")

if operator == "+":
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
elif operator == "-":
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
elif operator == "*":
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
elif operator == "/":
    if num2 != 0:
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
    else:
        print("Error: Cannot divide by zero.")
else:
    print("Invalid operator. Please use +, -, *, or /.")

