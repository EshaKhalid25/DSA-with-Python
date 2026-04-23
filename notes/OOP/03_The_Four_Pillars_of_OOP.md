# 03: The Four Pillars of OOP

The four fundamental principles of Object-Oriented Programming are Inheritance, Encapsulation, Abstraction, and Polymorphism.

---

## 1. Inheritance
Inheritance allows us to define a class that inherits all the methods and properties from another class.
- **Parent class** (or Base class): the class being inherited from.
- **Child class** (or Derived class): the class that inherits from another class.

### Types of Inheritance
- **Single Inheritance:** A child class inherits from a single parent class.
- **Multiple Inheritance:** A child class inherits from multiple parent classes.

### Example (Single Inheritance)
```python
# Parent class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")

# Child class
class Dog(Animal):
    # Overriding the parent's speak method
    def speak(self):
        return f"{self.name} says Woof!"

class Cat(Animal):
    # Overriding the parent's speak method
    def speak(self):
        return f"{self.name} says Meow!"

my_dog = Dog("Buddy")
print(my_dog.speak()) # Output: Buddy says Woof!
```

### The `super()` Function
The `super()` function is used to give access to methods and properties of a parent or sibling class. It is commonly used to call the parent's `__init__()` method from the child's `__init__()`.

```python
class Bird:
    def __init__(self, name):
        self.name = name

class FlyingBird(Bird):
    def __init__(self, name, wing_span):
        super().__init__(name) # Call the parent's constructor
        self.wing_span = wing_span
```

---

## 2. Encapsulation
Encapsulation is the bundling of data (attributes) and the methods that operate on the data into a single unit (a class). It also restricts direct access to some of an object's components.

### Access Modifiers
Python doesn't have strict `private` or `protected` keywords like C++ or Java. Instead, it relies on naming conventions:
- **Public:** Accessible from anywhere. (e.g., `name`)
- **Protected:** Should only be accessed within the class and its subclasses. Indicated by a single underscore prefix. (e.g., `_name`)
- **Private:** Should only be accessed within the class. Indicated by a double underscore prefix. Python performs "name mangling" on these. (e.g., `__name`)

**Note on Python's Philosophy:** This is a convention, not a strict rule. Python's philosophy is "we're all consenting adults here." There is no concept of a `friend` class.

```python
class Car:
    def __init__(self, make):
        self.make = make          # Public
        self._protected_var = 10  # Protected
        self.__private_var = 20   # Private

    def get_private(self):
        return self.__private_var

my_car = Car("Toyota")
print(my_car.make)
print(my_car._protected_var) # Accessible, but convention says not to
# print(my_car.__private_var) # This will cause an AttributeError
print(my_car.get_private()) # Access via a method
```

---

## 3. Abstraction
Abstraction means hiding the complex implementation details and showing only the essential features of the object. In Python, we can achieve abstraction using Abstract Base Classes (ABCs).

- An abstract class can't be instantiated.
- It can contain abstract methods, which are declared but contain no implementation. Subclasses are required to provide an implementation for these methods.

```python
from abc import ABC, abstractmethod

class Shape(ABC): # Inherit from ABC to make it an abstract class
    @abstractmethod
    def area(self):
        pass

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self): # Must implement the abstract method
        return self.side * self.side

# my_shape = Shape() # This would raise a TypeError
my_square = Square(5)
print(my_square.area()) # Output: 25
```

---

## 4. Polymorphism
Polymorphism means "many forms", and it refers to the ability of different objects to respond to the same method call in different ways.

### Method Overriding (Polymorphism with Inheritance)
This is what we saw in the Inheritance example. Both `Dog` and `Cat` objects have a `speak()` method, but they behave differently.

### Duck Typing (Polymorphism without Inheritance)
"If it walks like a duck and it quacks like a duck, then it must be a duck."
In Python, we don't care about the object's type, only that it has the methods we need.

```python
class Duck:
    def quack(self):
        print("Quack, quack!")

class Person:
    def quack(self):
        print("I'm quacking like a duck!")

def make_it_quack(obj):
    # We don't care if obj is a Duck or a Person,
    # only that it has a quack() method.
    obj.quack()

duck = Duck()
person = Person()

make_it_quack(duck)   # Output: Quack, quack!
make_it_quack(person) # Output: I'm quacking like a duck!
```
