# Practice Questions: 03 - The Four Pillars of OOP

# 1. Inheritance
#   a) Create a parent class `Vehicle` with an `__init__` method that accepts `make` and `model`.
#   b) Add a method `display_info` to `Vehicle` that prints the make and model.
#   c) Create a child class `Car` that inherits from `Vehicle`.
#   d) In the `Car` class, add a new method `honk` that prints "Honk! Honk!".
#   e) Create a `Car` object and call both `display_info` and `honk` on it.

class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    
    def display_info(self):
        print(f"Make: {self.make}, Model: {self.model}")

class Car(Vehicle):
    def honk(self):
        print("Honk! Honk!")
car = Car("Toyota", "Corolla")
car.display_info()
car.honk()


# 2. Method Overriding and `super()`
#   a) Continuing from above, create another child class `Motorcycle` that also inherits from `Vehicle`.
#   b) The `__init__` method of `Motorcycle` should accept `make`, `model`, and `has_sidecar`.
#   c) Use `super()` to call the parent's `__init__` method.
#   d) Override the `display_info` method in `Motorcycle` to also print whether it has a sidecar.
#   e) Create a `Motorcycle` object and call its `display_info` method.

class Motorcycle(Vehicle):
    def __init__(self, make, model, has_sidecar):
        super().__init__(make, model)
        self.has_sidecar = has_sidecar
    
    def display_info(self):
        super().display_info()
        print(f"Has sidecar: {self.has_sidecar}")
motorcycle = Motorcycle("Harley-Davidson", "Street 750", False)
motorcycle.display_info()


# 3. Encapsulation (Access Modifiers)
#   a) Create a class `Employee`.
#   b) In `__init__`, initialize a public attribute `name`, a protected attribute `_employee_id`, and a private attribute `__salary`.
#   c) Create a method `get_salary` to publicly expose the private salary.
#   d) Create another method `set_salary` to allow changing the private salary.
#   e) Create an `Employee` object.
#   f) Access and print the `name` and `_employee_id`.
#   g) Try to access `__salary` directly. What happens? (Add a comment).
#   h) Use the `get_salary` and `set_salary` methods to view and modify the salary.

class Employee:
    def __init__(self, name, employee_id, salary):
        self.name = name
        self._employee_id = employee_id
        self.__salary = salary

    def get_salary(self):
        print(f"Salary: {self.__salary}")
    
    def set_salary(self, new_salary):
        self.__salary = new_salary

employee = Employee('Hadia', 'E123', 50000)
print(employee.name)
print(employee._employee_id)
# print(employee.__salary)  # This will raise an AttributeError because __salary is a private attribute and cannot be accessed directly from outside the class.
employee.get_salary()


# 4. Abstraction (Abstract Base Classes)
#   a) Import `ABC` and `abstractmethod` from the `abc` module.
#   b) Create an abstract class `Database` that inherits from `ABC`.
#   c) Define two abstract methods: `connect` and `disconnect`.
#   d) Create two concrete classes, `MySQLDatabase` and `MongoDatabase`, that inherit from `Database`.
#   e) Implement the `connect` and `disconnect` methods in both child classes with simple print statements (e.g., "Connecting to MySQL...").
#   f) Create instances of `MySQLDatabase` and `MongoDatabase` and call their methods.

from abc import ABC, abstractmethod
class Database(ABC):
    @abstractmethod
    def connect(self):
        pass
    
    @abstractmethod
    def disconnect(self):
        pass

class MySQLDatabase(Database):
    def connect(self):
        print("Connecting to SQL...")
    
    def disconnect(self):
        print("Disconnecting from SQL...")

class MongoDatabase(Database):
    def connect(self):
        print("Connecting to MongoDB...")
    
    def disconnect(self):
        print("Disconnecting from MongoDB...")

sqlDatabase = MySQLDatabase()
sqlDatabase.connect()
sqlDatabase.disconnect()

mongoDatabase = MongoDatabase()
mongoDatabase.connect()
mongoDatabase.disconnect()


# 5. Polymorphism (Duck Typing)
#   a) Create two independent classes: `Guitar` and `Piano`.
#   b) Both classes should have a method named `make_sound`.
#   c) The `Guitar`'s method should print "Strumming the guitar".
#   d) The `Piano`'s method should print "Playing the piano keys".
#   e) Create a function `play_instrument` that takes an object and calls its `make_sound` method.
#   f) Create instances of `Guitar` and `Piano` and pass them to the `play_instrument` function.

class Guitar:
    def make_sound(self):
        print("Strumming the guitar")
class Piano:
    def make_sound(self):
        print("Playing the piano keys")
def play_instrument(instrument):
    instrument.make_sound()

guitar = Guitar()
piano = Piano()

play_instrument(guitar)
play_instrument(piano)

