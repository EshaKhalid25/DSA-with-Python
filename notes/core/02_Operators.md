# 02: Python Operators

Operators are special symbols in Python that carry out arithmetic or logical computation.

## Arithmetic Operators
Used to perform mathematical operations.
- `+` (Addition)
- `-` (Subtraction)
- `*` (Multiplication)
- `/` (Division) - always returns a float
- `%` (Modulus) - returns the remainder
- `**` (Exponentiation) - `x ** y` = x to the power of y
- `//` (Floor division) - divides and rounds down to the nearest integer

**Example:**
```python
a = 10
b = 3
print(a + b)  # 13
print(a / b)  # 3.333...
print(a // b) # 3
print(a % b)  # 1
print(a ** b) # 1000
```

## Comparison Operators
Used to compare two values.
- `==` (Equal to)
- `!=` (Not equal to)
- `>` (Greater than)
- `<` (Less than)
- `>=` (Greater than or equal to)
- `<=` (Less than or equal to)

**Example:**
```python
x = 5
y = 8
print(x == y) # False
print(x < y)  # True
```

## Logical Operators
Used to combine conditional statements.
- `and`: Returns `True` if both statements are true
- `or`: Returns `True` if one of the statements is true
- `not`: Reverses the result, returns `False` if the result is true

**Example:**
```python
age = 25
is_citizen = True
print(age > 18 and is_citizen) # True
print(not(age < 21))           # True
```

## Assignment Operators
Used to assign values to variables.
- `=` (Assign)
- `+=` (Add and assign)
- `-=` (Subtract and assign)
- `*=` (Multiply and assign)
- `/=` (Divide and assign)
- `%=` (Modulus and assign)
- `//=` (Floor divide and assign)
- `**=` (Exponent and assign)

**Example:**
```python
count = 0
count += 1  # count is now 1
count *= 5  # count is now 5
```
