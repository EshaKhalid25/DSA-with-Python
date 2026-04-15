# Practice Questions: Loops

# 1. `for` Loop with `range()`
#   a) Write a `for` loop that prints the numbers from 1 to 10 (inclusive).
#   b) Write a `for` loop that prints all the even numbers from 2 to 20.
#   c) Write a `for` loop that counts down from 10 to 1 and then prints "Blastoff!".

for i in range(1, 11):
    print(i)

for i in range(2, 21, 2):
    print(i)

for i in range(10, 0, -1):
    print(i)
else:
    print("Blastoff!")


# 2. `for` Loop with Sequences
#   a) Create a list of your favorite fruits: `fruits = ["apple", "banana", "cherry", "date"]`.
#   b) Write a `for` loop that iterates through the list and prints each fruit.
#   c) Write a `for` loop that iterates through the string "Python" and prints each character.

fruits = ["apple", "banana", "cherry", "date"]
for fruit in fruits:
    print(fruit)

for char in "Python":
    print(char)


# 3. `while` Loop
#   a) Write a `while` loop that prints numbers from 1 to 5.
#   b) Create a program that asks the user to guess a secret number (e.g., 7).
#   c) Keep asking for input in a `while` loop until the user guesses the correct number. Print a "You got it!" message when they guess correctly.

secret_number = 7
guess = None
while guess != secret_number:
    guess = int(input("Guess the secret number (between 1 and 10): "))
    if guess == secret_number:
        print("You got it!")
    else:
        print("Try again!")


# 4. Loop Control Statements (`break` and `continue`)
#   a) Write a `for` loop that iterates from 1 to 20.
#   b) Inside the loop, if a number is divisible by 3, `continue` to the next iteration (skip printing it).
#   c) If a number is 15, `break` out of the loop.
#   d) Print the numbers that are not skipped.

for i in range(1, 21):
    if i % 3 == 0:
        continue
    if i == 15:
        break
    print(i)


# 5. Putting it all together
#   a) Write a program to find the sum of all numbers from 1 to 100 that are divisible by 5.
#   b) Initialize a `total` variable to 0.
#   c) Use a `for` loop and the `range()` function.
#   d) Inside the loop, use an `if` statement to check for divisibility by 5.
#   e) If divisible, add the number to the `total`.
#   f) After the loop, print the final `total`.

total = 0
for i in range(1, 101):
    if i % 5 == 0:
        total += i
print("The sum of all numbers from 1 to 100 that are divisible by 5 is:", total)

