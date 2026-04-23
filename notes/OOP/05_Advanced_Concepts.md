# 05: Advanced OOP Concepts

## Generics (Python's version of Templates)
Generics allow you to write functions and classes that can work with a variety of data types, while still providing type hints for static analysis. This is Python's equivalent to templates in C++.

The `typing` module provides the necessary tools.

### `TypeVar`
`TypeVar` is used to declare a type variable, which acts as a placeholder for a type.

**Example: A Generic Function**
```python
from typing import TypeVar, List

# Declare a type variable 'T'
T = TypeVar('T')

# This function can take a list of any type and return the first element of that same type.
def get_first_item(items: List[T]) -> T:
    return items[0]

# Usage
int_list = [1, 2, 3]
first_int = get_first_item(int_list) # Type checker knows this is an int

str_list = ["a", "b", "c"]
first_str = get_first_item(str_list) # Type checker knows this is a string
```

### `Generic`
`Generic` is used to create generic classes.

**Example: A Generic Stack Class**
```python
from typing import TypeVar, Generic, List

T = TypeVar('T')

class Stack(Generic[T]):
    def __init__(self) -> None:
        self._items: List[T] = []

    def push(self, item: T) -> None:
        self._items.append(item)

    def pop(self) -> T:
        return self._items.pop()

# A stack that can only hold integers
int_stack = Stack[int]()
int_stack.push(1)
int_stack.push(2)
# int_stack.push("a") # A type checker would flag this as an error

# A stack that can only hold strings
str_stack = Stack[str]()
str_stack.push("hello")
str_stack.push("world")
```

---

## Composition vs. Inheritance
When designing your classes, you have two primary ways to reuse code: Inheritance and Composition.

### Inheritance ("is a" relationship)
- A `Dog` **is an** `Animal`.
- A `Square` **is a** `Shape`.
- Use inheritance when a class is a more specific version of another class.
- **Pros:** Easy to understand, reuses code from the parent.
- **Cons:** Can lead to rigid hierarchies. Changes in the parent class can unexpectedly break child classes. Multiple inheritance can become very complex ("The Diamond Problem").

### Composition ("has a" relationship)
- A `Car` **has an** `Engine`.
- A `Library` **has a** list of `Book`s.
- Use composition when an object is built from or composed of other objects. You create instances of other classes within your class.

**Example:**
```python
class Engine:
    def start(self):
        print("Engine starting...")

class Car:
    def __init__(self):
        # The Car object is composed of an Engine object.
        self.engine = Engine()

    def start(self):
        print("Starting the car...")
        self.engine.start()

my_car = Car()
my_car.start()
```

### Which one to choose?
**Favor Composition over Inheritance.**

This is a common design principle. Composition is often more flexible and leads to a more stable, loosely coupled design.

- **Use Inheritance only when:**
  - The "is a" relationship is very clear and makes sense.
  - You want to leverage polymorphism and abstract base classes.

- **Use Composition when:**
  - You want to reuse code from another class, but the "is a" relationship doesn't fit.
  - You want more flexibility in how your class is structured.
  - You want to avoid the complexities of deep or multiple inheritance.
