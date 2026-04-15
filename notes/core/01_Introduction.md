# 01: Introduction to Python

## What is Python?
- Python is a high-level, interpreted, general-purpose programming language.
- Its design philosophy emphasizes code readability with its notable use of significant whitespace.
- It's dynamically typed and garbage-collected.
- It supports multiple programming paradigms, including structured (particularly, procedural), object-oriented, and functional programming.

## Variables and Data Types
In Python, you don't need to declare a variable's type. The type is inferred at runtime.

**Common Data Types:**
- **Text Type:** `str`
- **Numeric Types:** `int`, `float`, `complex`
- **Sequence Types:** `list`, `tuple`, `range`
- **Mapping Type:** `dict`
- **Set Types:** `set`, `frozenset`
- **Boolean Type:** `bool`
- **Binary Types:** `bytes`, `bytearray`, `memoryview`

**Example:**
```python
name = "Alice"      # str
age = 30           # int
height = 5.9       # float
is_student = False # bool
```

## Type Casting
You can convert from one type to another with the following functions:
- `int()`: constructs an integer number from an integer literal, a float literal (by removing all decimals), or a string literal (providing the string represents a whole number)
- `float()`: constructs a float number from an integer literal, a float literal or a string literal (providing the string represents a float or an integer)
- `str()`: constructs a string from a wide variety of data types, including strings, integer literals and float literals

**Example:**
```python
x = int(1)      # x will be 1
y = int(2.8)    # y will be 2
z = int("3")    # z will be 3

a = float(1)    # a will be 1.0
b = float("4.2")# b will be 4.2

c = str(8.0)    # c will be '8.0'
```

## Basic Input/Output
- `print()`: Outputs data to the standard output device (screen).
- `input()`: Allows for user input. It always returns the input as a string.

**Example:**
```python
print("Hello, World!")

user_name = input("Enter your name: ")
print("Hello, " + user_name)

user_age = input("Enter your age: ")
# You need to cast the input if you want to use it as a number
age_in_five_years = int(user_age) + 5
print("You will be " + str(age_in_five_years) + " in five years.")
```

## Comments
Comments are used to explain Python code.
- Single-line comments start with a `#`.
- Multi-line comments can be written using triple quotes (`"""` or `'''`).

**Example:**
```python
# This is a single-line comment

"""
This is a multi-line comment.
It can span across multiple lines.
"""
```
