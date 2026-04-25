# Practice Questions: 05 - Advanced Concepts

# 1. Composition
#   a) Create a class `Author` with a `name` attribute.
#   b) Create a class `Book`.
#   c) The `Book`'s `__init__` method should take a `title` and an `author_name`.
#   d) Inside the `Book`'s `__init__`, it should create an `Author` object. This shows composition (a `Book` "has an" `Author`).
#   e) Add a method `display_book_info` to the `Book` class that prints the book's title and the author's name.
#   f) Create a `Book` object and call its `display_book_info` method.

class Author:
    def __init__(self, name):
        self.name = name
class Book:
    def __init__(self, title, author_name):
        self.title = title
        self.author = Author(author_name)
    
    def display_book_info(self):
        print(f"Title: {self.title}, Author: {self.author.name}")
my_book = Book("The Great Gatsby", "F. Scott Fitzgerald")
my_book.display_book_info()


# 2. Composition vs. Inheritance
#   a) Consider a `Car` and an `Engine`.
#   b) Which relationship makes more sense:
#      - A `Car` **is an** `Engine` (Inheritance)
#      - A `Car` **has an** `Engine` (Composition)
#   c) Write a short comment in your code explaining your choice.
#   d) Implement the relationship you chose with simple `Car` and `Engine` classes. The `Engine` should have a `start()` method, and the `Car` should have a `start_car()` method that calls the engine's method.

class Car:
    def __init__(self, engine):
        self.engine = engine
    
    def start_car(self):
        self.engine.start()
class Engine:
    def start(self):
        print("Engine started.")
# A Car has an Engine, so we use composition. A Car is not an Engine, so inheritance would not be appropriate here.
my_engine = Engine()
my_car = Car(my_engine)
my_car.start_car()


# 3. Generics (using `typing`)
#   a) Import `TypeVar` and `Generic` from the `typing` module.
#   b) Declare a `TypeVar` called `T`.
#   c) Create a generic class `Box` that can hold an item of any type.
#      - It should inherit from `Generic[T]`.
#      - The `__init__` method should take an `item` of type `T`.
#      - It should have a method `get_item` that returns the item (of type `T`).
#   d) Create an instance of `Box` that is specifically for integers (`Box[int]`) and put an integer in it.
#   e) Create another instance of `Box` for strings (`Box[str]`) and put a string in it.
#   f) Get the items from both boxes and print them.
#   (Note: This exercise is about understanding the type hinting structure. The code will run without the hints, but a type checker like MyPy would use them to find errors).

from typing import TypeVar, Generic
T = TypeVar('T')
class Box(Generic[T]):
    def __init__(self, item: T):
        self.item = item
    
    def get_item(self) -> T:
        return self.item
int_box = Box[int](123)
str_box = Box[str]("Hello, World!")
print(int_box.get_item())  # This will print 123
print(str_box.get_item())  # This will print "Hello, World!"

