# 04: Conditional Statements

Conditional statements allow you to execute certain blocks of code based on whether a condition is true or false.

## The `if` Statement
Executes a block of code only if the specified condition is true.

**Syntax:**
```python
if condition:
    # code to execute if condition is true
```

**Example:**
```python
temperature = 35
if temperature > 30:
    print("It's a hot day!")
```

## The `if-else` Statement
Executes one block of code if the condition is true, and another block if it is false.

**Syntax:**
```python
if condition:
    # code to execute if condition is true
else:
    # code to execute if condition is false
```

**Example:**
```python
age = 17
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote yet.")
```

## The `if-elif-else` Ladder
Used to decide among several alternatives. `elif` is short for "else if".

**Syntax:**
```python
if condition1:
    # code for condition1
elif condition2:
    # code for condition2
else:
    # code if all above conditions are false
```

**Example:**
```python
score = 85
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "D"
print(f"Your grade is {grade}")
```

## Nested `if` Statements
You can have `if` statements inside other `if` statements.

**Example:**
```python
num = 15
if num >= 0:
    if num == 0:
        print("Zero")
    else:
        print("Positive number")
else:
    print("Negative number")
```

## Ternary Operator (Conditional Expressions)
A shorthand for the `if-else` statement.

**Syntax:**
`value_if_true if condition else value_if_false`

**Example:**
```python
age = 20
message = "Adult" if age >= 18 else "Minor"
print(message) # Output: Adult
```
