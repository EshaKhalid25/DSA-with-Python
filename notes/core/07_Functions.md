# 07: Functions

A function is a block of code which only runs when it is called. You can pass data, known as parameters, into a function. A function can return data as a result.

## Defining and Calling a Function
- Use the `def` keyword to define a function.
- Call the function using its name followed by parentheses `()`.

**Syntax:**
```python
def function_name(parameters):
    """Docstring explaining the function."""
    # code block
    return value
```

**Example:**
```python
def greet():
    print("Hello, world!")

greet() # Calling the function
```

## Parameters and Arguments
- A **parameter** is the variable listed inside the parentheses in the function definition.
- An **argument** is the value that is sent to the function when it is called.

**Example:**
```python
def greet_user(name): # 'name' is a parameter
    print(f"Hello, {name}!")

greet_user("Alice") # "Alice" is an argument
```

## The `return` Statement
The `return` statement is used to exit a function and return a value. If no return statement is specified, the function returns `None`.

**Example:**
```python
def add_numbers(x, y):
    return x + y

sum_result = add_numbers(5, 3)
print(sum_result) # Output: 8
```

## Default Arguments
You can specify a default value for a parameter. This value is used if no argument is provided for that parameter when the function is called.

**Example:**
```python
def greet_country(country="Norway"):
    print(f"I am from {country}")

greet_country("Sweden") # Output: I am from Sweden
greet_country()         # Output: I am from Norway
```

## Arbitrary Arguments, `*args` and `**kwargs`
- `*args`: If you don't know how many arguments will be passed, use `*` before the parameter name. The function will receive a **tuple** of arguments.
- `**kwargs`: If you don't know how many keyword arguments will be passed, use `**` before the parameter name. The function will receive a **dictionary** of arguments.

**Example `*args`:**
```python
def sum_all(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total

print(sum_all(1, 2, 3, 4)) # Output: 10
```

**Example `**kwargs`:**
```python
def display_info(**user_info):
    for key, value in user_info.items():
        print(f"{key}: {value}")

display_info(name="John", age=30, city="New York")
```

## Scope of Variables
- **Local Scope:** A variable created inside a function is available only inside that function.
- **Global Scope:** A variable created in the main body of the Python code is a global variable and belongs to the global scope.

**Example:**
```python
x = "global" # global variable

def my_func():
    y = "local" # local variable
    print(x) # can access global variable
    print(y)

my_func()
# print(y) # This would cause an error because y is local to my_func
```
To modify a global variable from inside a function, use the `global` keyword.
```python
count = 0
def increment():
    global count
    count += 1

increment()
print(count) # Output: 1
```
