# 03: Python Strings

Strings in Python are sequences of characters, enclosed in single, double, or triple quotes.

## String Creation
```python
s1 = 'This is a string.'
s2 = "This is also a string."
s3 = """This is a multi-line
string."""
```

## String Slicing and Indexing
- **Indexing:** Access a single character. Python uses 0-based indexing. Negative indexing starts from the end.
- **Slicing:** Access a range of characters.

**Example:**
```python
text = "Python"
print(text[0])    # 'P'
print(text[-1])   # 'n'

# Slicing: [start:stop:step]
print(text[2:5])  # 'tho' (characters from index 2 to 4)
print(text[:3])   # 'Pyt' (from the beginning to index 2)
print(text[2:])   # 'thon' (from index 2 to the end)
print(text[::-1]) # 'nohtyP' (reverse the string)
```

## Common String Methods
Strings are immutable, so methods return a new string.
- `upper()`: Converts the string to uppercase.
- `lower()`: Converts the string to lowercase.
- `strip()`: Removes leading/trailing whitespace.
- `lstrip()`: Removes leading whitespace.
- `rstrip()`: Removes trailing whitespace.
- `split(separator)`: Splits the string into a list of substrings.
- `replace(old, new)`: Replaces occurrences of a substring.
- `startswith(prefix)`: Returns `True` if the string starts with the prefix.
- `endswith(suffix)`: Returns `True` if the string ends with the suffix.
- `find(substring)`: Returns the lowest index of the substring, or -1 if not found.
- `count(substring)`: Returns the number of occurrences of the substring.

**Example:**
```python
message = "  Hello, World!  "
print(message.strip())      # "Hello, World!"
print(message.lower())      # "  hello, world!  "
print(message.split(','))   # ['  Hello', ' World!  ']
print(message.replace("World", "Python")) # "  Hello, Python!  "
```

## String Formatting
- **f-Strings (Formatted String Literals):** The most modern and preferred way.
- `str.format()` method.

**Example (f-Strings):**
```python
name = "Bob"
age = 40
print(f"His name is {name} and he is {age} years old.")
# Output: His name is Bob and he is 40 years old.

price = 19.99
print(f"The price is ${price:.2f}") # Format to 2 decimal places
# Output: The price is $19.99
```
