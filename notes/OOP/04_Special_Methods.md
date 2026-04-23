# 04: Special Methods (Dunder Methods)

Special methods in Python are the ones surrounded by double underscores (e.g., `__init__`, `__len__`). They are also known as "dunder" methods (for **d**ouble **under**score).

These methods are not meant to be called directly by you. Instead, they are invoked by Python in response to a specific action or syntax, like object creation, addition, or calling `len()`.

## `__str__()` and `__repr__()`
These two methods control how an object is converted to a string.

### `__str__()`
- Called by the `str()` built-in function and, by extension, the `print()` function.
- Its goal is to return a "user-friendly", readable string representation of the object.
- This is what your users will see.

### `__repr__()`
- Called by the `repr()` built-in function.
- Its goal is to be unambiguous and return a "developer-friendly" string representation of the object. Ideally, this string should be a valid Python expression that could be used to recreate the object.
- If `__str__` is not implemented, Python will fall back to using `__repr__`.

**Example:**
```python
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"'{self.title}' by {self.author}"

    def __repr__(self):
        return f"Book(title='{self.title}', author='{self.author}')"

my_book = Book("To Kill a Mockingbird", "Harper Lee")

# Using print() calls __str__()
print(my_book)
# Output: 'To Kill a Mockingbird' by Harper Lee

# Calling str() explicitly
print(str(my_book))
# Output: 'To Kill a Mockingbird' by Harper Lee

# Calling repr() explicitly
print(repr(my_book))
# Output: Book(title='To Kill a Mockingbird', author='Harper Lee')
```

## `__len__()`
- Called by the built-in `len()` function.
- It should return the length of the object, as an integer.

**Example:**
```python
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def __len__(self):
        return len(self.books)

lib = Library()
lib.add_book(Book("1984", "George Orwell"))
lib.add_book(Book("The Hobbit", "J.R.R. Tolkien"))

# Now we can use len() on our Library object
print(len(lib)) # Output: 2
```

## Other Common Dunder Methods
There are many other special methods that allow you to emulate the behavior of built-in types.

- **Comparison Methods:**
  - `__eq__(self, other)`: Defines behavior for the equality operator, `==`.
  - `__ne__(self, other)`: Defines behavior for the inequality operator, `!=`.
  - `__lt__(self, other)`: Defines behavior for the less-than operator, `<`.
  - `__gt__(self, other)`: Defines behavior for the greater-than operator, `>`.

- **Arithmetic Methods:**
  - `__add__(self, other)`: Defines behavior for the addition operator, `+`.
  - `__sub__(self, other)`: Defines behavior for the subtraction operator, `-`.
  - `__mul__(self, other)`: Defines behavior for the multiplication operator, `*`.

By implementing these methods, you can create objects that behave in intuitive ways, just like Python's built-in objects.
