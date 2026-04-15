# Practice Questions: Python Strings

# 1. String Creation and Indexing
#   a) Create a string variable `greeting` with the value "Hello, Python!".
#   b) Print the first character of the string.
#   c) Print the last character of the string using negative indexing.
#   d) Print the character at index 7.

greeting = "Hello, Python!"
print(greeting[0])  
print(greeting[-1])  
print(greeting[7]) 


# 2. String Slicing
#   a) Using the `greeting` string from above, slice and print the word "Python".
#   b) Slice and print the first 5 characters ("Hello").
#   c) Slice and print the string from index 7 to the end.
#   d) Create a new string that is the reverse of the `greeting` string using slicing. Print the reversed string.

print(greeting[7:13])  
print(greeting[:5]) 
print(greeting[7:])  
print(greeting[::-1])  


# 3. String Methods
#   a) Create a string `messy_string = "   lEaRn PyThOn   "`.
#   b) Convert the entire string to lowercase and print it.
#   c) Convert the entire string to uppercase and print it.
#   d) Remove the leading and trailing whitespace from the string and print the cleaned version.
#   e) Replace "PyThOn" with "Data Science" in the original `messy_string` and print the result.

messy_string = "    lEaRn PyThOn     "
print(messy_string.lower()) 
print(messy_string.upper())  
print(messy_string.strip()) 
print(messy_string.replace("PyThOn", "Data Science"))


# 4. String Formatting
#   a) Create two variables, `name = "Alice"` and `age = 30`.
#   b) Use an f-string to create a sentence: "My name is Alice and I am 30 years old." Print the sentence.
#   c) Create a variable `pi = 3.14159265`.
#   d) Use an f-string to print the value of pi formatted to 3 decimal places, like "The value of pi is 3.142".

name = "Alice"
age = 30
print(f"My name is {name} and I am {age} years old.")  

pi = 3.14159265
print(f"The value of pi is {pi:.3f}") 


# 5. Putting it all together
#   a) Ask the user to enter their full name (e.g., "john doe").
#   b) Use string methods to capitalize the first letter of both the first and last name.
#   c) Print a welcome message using an f-string, for example: "Welcome, John Doe!".
#   Hint: You might need to `split()` the string into a list, capitalize the parts, and then `join()` them back together. Or, you can use the `.title()` method.

name = input("Please enter your full name: ")
capitalized_name = name.title()
print(f"Welcome, {capitalized_name}!")

