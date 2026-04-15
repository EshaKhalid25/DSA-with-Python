# 05: Loops

Loops are used to execute a block of code repeatedly.

## The `for` Loop
The `for` loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

**Iterating over a sequence:**
```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```

**The `range()` function:**
To loop through a set of code a specified number of times, we can use the `range()` function.
```python
# Prints numbers from 0 to 4
for i in range(5):
    print(i)

# Prints numbers from 2 to 5
for i in range(2, 6):
    print(i)

# Prints numbers from 1 to 10 with a step of 2
for i in range(1, 11, 2):
    print(i)
```

## The `while` Loop
With the `while` loop, we can execute a set of statements as long as a condition is true.

**Syntax:**
```python
while condition:
    # code to execute
```

**Example:**
```python
count = 0
while count < 5:
    print(count)
    count += 1 # Important: update the counter to avoid an infinite loop
```

## Loop Control Statements
- **`break` Statement:** Used to exit a loop completely.
- **`continue` Statement:** Used to skip the current iteration and move to the next one.

**`break` Example:**
```python
for i in range(10):
    if i == 5:
        break # Exit the loop when i is 5
    print(i)
# Output: 0, 1, 2, 3, 4
```

**`continue` Example:**
```python
for i in range(10):
    if i % 2 == 0:
        continue # Skip even numbers
    print(i)
# Output: 1, 3, 5, 7, 9
```

## The `else` Clause in Loops
Python allows an `else` clause at the end of a loop.
- For a `for` loop, the `else` block is executed when the loop has finished iterating through the list.
- For a `while` loop, the `else` block is executed when the condition becomes false.
- The `else` block is **not** executed if the loop is terminated by a `break` statement.

**Example:**
```python
for i in range(5):
    print(i)
else:
    print("Loop finished without a break.")

# Example with break
for i in range(5):
    if i == 3:
        break
    print(i)
else:
    print("This will not be printed.")
```
