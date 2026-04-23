# 02: Attributes and Methods

## The `__init__()` Method (Constructor)
The `__init__()` method is a special method that Python runs automatically whenever we create a new instance of a class. It's often referred to as the class "constructor".

- It is used to initialize the object's state, i.e., to set the initial values for the object's attributes.
- Like all methods, its first parameter must be `self`.

**Example:**
```python
class Dog:
    def __init__(self, name, age):
        print(f"A new dog named {name} has been created!")
        # We'll assign these to attributes in the next step.

my_dog = Dog("Buddy", 4) # The __init__ method is called automatically here.
```

## Instance Attributes
Instance attributes are specific to each object (instance) of a class. They are defined inside the `__init__()` method and belong to the object itself.

- We use `self.attribute_name = value` to create and assign an instance attribute.

**Example:**
```python
class Dog:
    def __init__(self, name, age):
        # These are instance attributes
        self.name = name
        self.age = age

dog1 = Dog("Buddy", 4)
dog2 = Dog("Lucy", 2)

# Each instance has its own data
print(dog1.name) # Output: Buddy
print(dog2.name) # Output: Lucy
```

## Class Attributes
Class attributes are shared by all instances of a class. They are defined directly inside the class, but outside of any method.

- They are like `static` variables in other languages.

**Example:**
```python
class Dog:
    # This is a class attribute
    species = "Canis familiaris"

    def __init__(self, name):
        self.name = name

dog1 = Dog("Buddy")
dog2 = Dog("Lucy")

# Both instances share the same class attribute
print(dog1.species) # Output: Canis familiaris
print(dog2.species) # Output: Canis familiaris
```

## Instance, Class, and Static Methods

### Instance Methods
- The most common type of method.
- Takes `self` as the first parameter.
- Can access and modify the object's state (instance attributes).

```python
class Dog:
    def __init__(self, name):
        self.name = name

    # This is an instance method
    def speak(self):
        return f"{self.name} says woof!"
```

### Class Methods
- Marked with a `@classmethod` decorator.
- Takes `cls` (representing the class itself) as the first parameter, not `self`.
- Cannot access instance attributes, but can access and modify class attributes.
- Often used as factory methods to create instances in a specific way.

```python
class Dog:
    species = "Canis familiaris"

    def __init__(self, name):
        self.name = name

    @classmethod
    def get_species(cls):
        return cls.species

print(Dog.get_species()) # Call it on the class itself
```

### Static Methods
- Marked with a `@staticmethod` decorator.
- Does not take `self` or `cls` as the first parameter.
- Cannot access or modify class or instance state.
- They are essentially regular functions that are namespaced within the class. They are often used for utility functions that have a logical connection to the class.

```python
class MathUtils:
    @staticmethod
    def add(x, y):
        return x + y

print(MathUtils.add(5, 10)) # Call it like a regular function namespaced by the class
```
