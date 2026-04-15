# Practice Questions: Functions

# 1. Basic Function
#   a) Define a function named `print_greeting` that takes no arguments.
#   b) The function should print the message "Hello, welcome to functions!".
#   c) Call the function.

def print_greeting():
    print("Hello, welcome to functions!")

print_greeting()


# 2. Function with Parameters
#   a) Define a function named `greet_user` that takes one argument, `name`.
#   b) The function should print a personalized greeting, like "Hello, [Name]!".
#   c) Call the function with your name as the argument.

def greet_user(name):
    print(f"Hello, {name}!")

greet_user("Esha")


# 3. Function with `return` Value
#   a) Define a function named `calculate_area` that takes two arguments, `width` and `height`.
#   b) The function should calculate the area (`width * height`) and return the result.
#   c) Call the function with `width=10` and `height=5`.
#   d) Store the returned value in a variable `area` and print it.

def calculate_area(width, height):
    return width * height

area = calculate_area(10, 5)
print(area)


# 4. Function with Default Argument
#   a) Define a function named `create_email` that takes two arguments, `username` and `domain` (with a default value of "example.com").
#   b) The function should return a formatted email string, e.g., "username@domain.com".
#   c) Call the function once with just a username ("testuser").
#   d) Call the function again with a username ("admin") and a custom domain ("company.org").
#   e) Print the results of both calls.

def create_email(username, domain="example.com"):
    return f"{username}@{domain}"

email1 = create_email("testuser")
email2 = create_email("admin", "company.org")

print(email1)
print(email2)


# 5. Putting it all together
#   a) Define a function named `check_list_for_number`.
#   b) It should take two arguments: a list of numbers (`num_list`) and a single number to search for (`search_num`).
#   c) The function should loop through the list.
#   d) If the `search_num` is found in the list, the function should immediately return `True`.
#   e) If the loop finishes without finding the number, the function should return `False`.
#   f) Create a sample list, e.g., `my_numbers = [1, 5, 8, 12, 15]`.
#   g) Call the function to check if the number 8 is in the list and print the result.
#   h) Call the function again to check if the number 10 is in the list and print the result.

def check_list_for_number(num_list, search_num):
    for num in num_list:
        if num == search_num:
            return True
    return False

my_numbers = [1, 5, 8, 12, 15]
result1 = check_list_for_number(my_numbers, 8)
result2 = check_list_for_number(my_numbers, 10)
print(result1)  # Should print True
print(result2)  # Should print False
