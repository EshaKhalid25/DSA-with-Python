# Practice Questions: File Handling

# Note: For these exercises, you will be creating and manipulating files in the same directory as this script.

# 1. Writing to a File
#   a) Open a file named "greetings.txt" in write mode (`"w"`).
#   b) Write the following two lines to the file:
#      - "Hello, from Python!"
#      - "This is the first line of the file."
#   c) Close the file.
#   d) Use the file explorer to check if "greetings.txt" was created and has the correct content.
#   (It's best to use the `with` statement for this).

with open("greetings.txt", "w") as file:
    file.write("Hello, from Python!\n")
    file.write("This is the first line of the file.\n")


# 2. Reading from a File
#   a) Open the "greetings.txt" file you just created in read mode (`"r"`).
#   b) Read the entire content of the file into a single string variable.
#   c) Print the content.
#   d) Close the file.

with open("greetings.txt", "r") as file:
    content = file.read()
    print(content)


# 3. Appending to a File
#   a) Open "greetings.txt" in append mode (`"a"`).
#   b) Add a new line to the end of the file: "This line was appended."
#   c) Close the file.
#   d) Open the file again in read mode and print its content to verify the new line was added.

with open("greetings.txt", "a") as file:
    file.write("This line was appended.\n")

with open("greetings.txt", "r") as file:
    content = file.read()
    print(content)


# 4. Reading Line by Line
#   a) Create a new file named "shopping_list.txt" in write mode.
#   b) Write a few items to the list, each on a new line (e.g., "Milk", "Bread", "Eggs").
#   c) Close the file.
#   d) Open "shopping_list.txt" in read mode.
#   e) Use a `for` loop to read the file line by line and print each line.

with open("shopping_list.txt", "w") as file:
    file.write("Milk\n")
    file.write("Bread\n")
    file.write("Eggs\n")

with open("shopping_list.txt", "r") as file:
    for line in file:
        print(line.strip())  # Using strip() to remove the newline character


# 5. Putting it all together
#   a) Ask the user for their name.
#   b) Open a file named "user_log.txt" in append mode.
#   c) Write a log entry to the file, including the user's name and the current date/time.
#      - You can get the current time by importing the `datetime` module:
#        `from datetime import datetime`
#        `now = datetime.now()`
#        `timestamp = now.strftime("%Y-%m-%d %H:%M:%S")`
#   d) The log entry should look like this: "User: [Name] logged in at [Timestamp]".
#   e) Close the file.
#   f) Run the script a few times with different names to see the log file grow.

from datetime import datetime
name = input("Please enter your name: ")
now = datetime.now()    
timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
with open("user_log.txt", "a") as file:
    file.write(f"User: {name} logged in at {timestamp}\n")

    