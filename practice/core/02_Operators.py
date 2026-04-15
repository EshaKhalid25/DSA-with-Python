# Practice Questions: Python Operators

# 1. Arithmetic Operators
#   a) Create two variables, `num1 = 20` and `num2 = 5`.
#   b) Calculate and print their sum, difference, product, and quotient (division).
#   c) Calculate and print the remainder when `num1` is divided by `num2`.
#   d) Calculate and print `num1` raised to the power of `num2`.
#   e) Calculate and print the result of the floor division of `num1` by `num2`.

num1 = 20
num2 = 5

print("Sum:", num1 + num2)
print("Difference:", num1 - num2)
print("Product:", num1 * num2)
print("Quotient:", num1 / num2)
print("Remainder:", num1 % num2)
print("Power:", num1 ** num2)
print("Floor Division:", num1 // num2)


# 2. Comparison Operators
#   a) Using `num1` and `num2` from above, check and print if `num1` is greater than `num2`.
#   b) Check and print if `num1` is equal to `num2`.
#   c) Check and print if `num1` is not equal to `num2`.

print("Is num1 greater than num2?", num1 > num2)
print("Is num1 equal to num2?", num1 == num2)
print("Is num1 not equal to num2?", num1 != num2)


# 3. Logical Operators
#   a) Create two boolean variables, `is_sunny = True` and `is_warm = False`.
#   b) Check and print if it's a good day for the beach (i.e., if it is sunny AND warm).
#   c) Check and print if it's a good day to be outside (i.e., if it is sunny OR warm).
#   d) Check and print the opposite of `is_sunny`.

is_sunny = True
is_warm = False
print("Is it a good day for the beach?", is_sunny and is_warm)
print("Is it a good day to be outside?", is_sunny or is_warm)
print("Is it not sunny?", not is_sunny)



# 4. Assignment Operators
#   a) Create a variable `counter = 10`.
#   b) Increment the `counter` by 5 using an assignment operator. Print the result.
#   c) Decrement the `counter` by 3 using an assignment operator. Print the result.
#   d) Multiply the `counter` by 2 using an assignment operator. Print the result.

counter = 10
counter += 5
print("Counter after incrementing by 5:", counter)

counter -= 3
print("Counter after decrementing by 3:", counter)

counter *= 2
print("Counter after multiplying by 2:", counter)


# 5. Putting it all together
#   a) Write a program that checks if a number is even and positive.
#   b) Create a variable `number` with a value (e.g., 10, -5, 7).
#   c) Use arithmetic and logical operators to determine if the number meets both conditions.
#   d) Print a message like "`10` is both even and positive: `True`".
#   Hint: A number is even if `number % 2 == 0`.

number = 10
is_even = (number % 2 == 0)
is_positive = (number > 0)
print(f"{number} is both even and positive: {is_even and is_positive}")

