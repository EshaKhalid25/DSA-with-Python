# 01: Classes and Objects

## What is Object-Oriented Programming (OOP)?
OOP is a programming paradigm based on the concept of "objects", which can contain data in the form of fields (often known as attributes or properties) and code in the form of procedures (often known as methods).

A key feature of OOP is that it allows for the bundling of data and the methods that operate on that data into a single unit, an "object".

## Defining a Class
A class is a blueprint for creating objects. It defines a set of attributes and methods that the created objects will have.

- We use the `class` keyword to define a class.
- By convention, class names in Python start with a capital letter (PascalCase).

**Syntax:**
```python
class MyClassName:
    # class body: attributes and methods
    pass # pass is a placeholder for future code
```

**Example:**
```python
class Dog:
    # This is a simple class definition
    pass
```

## Creating an Object (Instance)
An object is an instance of a class. When a class is defined, no memory is allocated until an object of that class is created.

Creating an object is as simple as calling the class name as if it were a function.

**Example:**
```python
class Dog:
    pass

# Create two different Dog objects
d1 = Dog()
d2 = Dog()

print(d1)
print(d2)
# The output will show that d1 and d2 are two distinct objects in memory.
```

## The `self` Parameter
- The `self` parameter is a reference to the current instance of the class and is used to access variables that belong to the class.
- It must be the **first parameter** of any method in the class.
- You don't have to give it the name `self`, but it is a strong convention and you should always follow it.

When we call a method on an object like `my_object.method(arg1, arg2)`, Python automatically passes the object `my_object` as the first argument `self` to the method.

**Example:**
```python
class Dog:
    # This is an instance method
    def bark(self):
        print("Woof!")

# Create a Dog object
my_dog = Dog()

# Call the bark method on the object
# Python automatically passes `my_dog` as the `self` argument.
my_dog.bark() # Output: Woof!
```
In the next section, we'll see how to use `self` to manage the data (attributes) of each object.
