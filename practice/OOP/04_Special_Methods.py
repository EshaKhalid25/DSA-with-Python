# Practice Questions: 04 - Special Methods

# 1. `__str__` Method
#   a) Create a class `Computer` with an `__init__` method that takes `cpu` and `ram` as arguments.
#   b) Implement the `__str__` method for the `Computer` class.
#   c) The method should return a user-friendly string, like "Computer with [cpu] CPU and [ram]GB RAM".
#   d) Create an instance of the `Computer` class and use the `print()` function on it.

class Computer: 
    def __init__(self, cpu, ram):
        self.cpu = cpu
        self.ram = ram
    
    def __str__(self):
        return f"Computer with {self.cpu} CPU and {self.ram}GB RAM"
my_computer = Computer("Intel i7", 16)
print(my_computer)


# 2. `__repr__` Method
#   a) Continuing with the `Computer` class, implement the `__repr__` method.
#   b) The method should return a developer-friendly, unambiguous string that could be used to recreate the object, e.g., `Computer('Intel i7', 16)`.
#   c) In your terminal, create an instance of the class and just type the object's name and press Enter to see the `__repr__` output. Also, call `repr()` on the object.

class Computer: 
    def __init__(self, cpu, ram):
        self.cpu = cpu
        self.ram = ram
    
    def __str__(self):
        return f"Computer with {self.cpu} CPU and {self.ram}GB RAM"
    
    def __repr__(self):
        return f"Computer('{self.cpu}', {self.ram})"

my_computer = Computer("Intel i7", 16)
print(my_computer)  # This will call __str__
print(repr(my_computer))  # This will call __repr__


# 3. `__len__` Method
#   a) Create a class `Playlist`.
#   b) The `__init__` method should initialize an empty list called `songs`.
#   c) Create a method `add_song` that adds a song (just a string) to the list.
#   d) Implement the `__len__` method to return the number of songs in the playlist.
#   e) Create a `Playlist` object, add a few songs, and then use the `len()` function on the object.

class Playlist:
    def __init__(self):
        self.songs = []
    
    def add_song(self, song):
        self.songs.append(song)
    
    def __len__(self):
        return len(self.songs)
my_playlist = Playlist()
my_playlist.add_song("Song 1")
my_playlist.add_song("Song 2")
my_playlist.add_song("Song 3")
print(len(my_playlist))  


# 4. Comparison Methods (`__eq__` and `__gt__`)
#   a) Create a class `Product` with `name` and `price` attributes.
#   b) Implement the `__eq__` method. Two products are equal if their names are the same (case-insensitive).
#   c) Implement the `__gt__` method (`>`). A product is "greater than" another if its price is higher.
#   d) Create two `Product` objects with the same name but different cases (e.g., "Laptop" and "laptop") and check if they are equal.
#   e) Create two more products with different prices and check which one is greater.

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def __eq__(self, other):
        if isinstance(other, Product):
            return self.name.lower() == other.name.lower()
        return NotImplemented
    
    def __gt__(self, other):
        if isinstance(other, Product):
            return self.price > other.price
        return NotImplemented

product1 = Product("Laptop", 1000)
product2 = Product("laptop", 1200)
print(product1 == product2)  # This should return True
product3 = Product("Phone", 800)
print(product1 > product3)  # This should return True


# 5. Putting it all together
#   a) Create a class `Vector` that represents a 2D vector with `x` and `y` attributes.
#   b) Implement `__str__` to print the vector in the format `(x, y)`.
#   c) Implement `__repr__` to print `Vector(x, y)`.
#   d) Implement `__add__` to handle vector addition. Adding two vectors should create a new `Vector` object where the x and y components are the sum of the original vectors' components.
#      (e.g., Vector(2, 3) + Vector(3, 4) should result in Vector(5, 7)).
#   e) Create two `Vector` objects and print the result of their addition.

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"({self.x}, {self.y})"
    
    def __repr__(self):
        return f"Vector({self.x}, {self.y})"
    
    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        return NotImplemented

vector1 = Vector(2, 3)
vector2 = Vector(3, 4)
result_vector = vector1 + vector2
print(result_vector)  # This should print (5, 7)

