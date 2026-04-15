# 08: File Handling

File handling is an important part of any web application. Python has several functions for creating, reading, updating, and deleting files.

## Opening a File
The `open()` function is the key to working with files. It takes two parameters: `filename` and `mode`.

**Modes for opening a file:**
- `"r"` - **Read** - Default value. Opens a file for reading, error if the file does not exist.
- `"a"` - **Append** - Opens a file for appending, creates the file if it does not exist.
- `"w"` - **Write** - Opens a file for writing, creates the file if it does not exist. It will overwrite the entire file.
- `"x"` - **Create** - Creates the specified file, returns an error if the file exists.

You can also specify if the file should be handled as binary or text mode:
- `"t"` - **Text** - Default value. Text mode.
- `"b"` - **Binary** - Binary mode (e.g., for images).

**Syntax:**
```python
f = open("demofile.txt", "r")
# It is good practice to use the with keyword when dealing with file objects.
# The advantage is that the file is properly closed after its suite finishes,
# even if an exception is raised at some point.
with open("demofile.txt", "r") as f:
    # ... do something with the file
```

## Reading From a File
- `read()`: Returns the whole content of the file.
- `readline()`: Returns one line from the file.
- `readlines()`: Returns a list containing each line in the file as a list item.

**Example:**
```python
# Assuming 'f' is an open file object in read mode
print(f.read()) # Read the whole file

# Read line by line
with open("demofile.txt", "r") as f:
    for line in f:
        print(line, end='') # The end='' prevents extra newlines
```

## Writing to a File
- `write(text)`: Writes the specified string to the file.
- `writelines(lines)`: Writes a list of strings to the file.

**Example (Write - Overwrites):**
```python
with open("newfile.txt", "w") as f:
    f.write("Hello, World!\n")
    f.write("This is a new file.")
```

**Example (Append - Adds to the end):**
```python
with open("newfile.txt", "a") as f:
    f.write("\nThis line is appended.")
```

## Closing a File
It's crucial to close a file after you are finished with it. It frees up system resources.
- `f.close()`

If you use the `with` statement, the file will be closed automatically for you.

## Deleting a File
To delete a file, you must import the `os` module, and use its `os.remove()` function.

**Example:**
```python
import os

if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")
```
