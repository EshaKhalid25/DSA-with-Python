# Practice Questions: 02 - Attributes and Methods

# 1. The `__init__()` Method and Instance Attributes
#   a) Define a class `Person`.
#   b) In the `__init__` method, accept `name` and `age` as arguments.
#   c) Inside `__init__`, create two instance attributes: `self.name` and `self.age`.
#   d) Create an instance of the `Person` class with a name and age of your choice.
#   e) Print the `name` and `age` attributes of the object you created.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
person1 = Person("Alice", 30)
print(person1.name)
print(person1.age)


# 2. Class Attributes
#   a) Define a class `Student`.
#   b) Add a class attribute `school_name` and set it to "Springfield Elementary".
#   c) In the `__init__` method, accept a `student_name` and initialize an instance attribute.
#   d) Create two different `Student` objects.
#   e) Print the `school_name` for both students to show that it's shared.
#   f) Try changing the class attribute directly via the class: `Student.school_name = "Shelbyville Elementary"`.
#   g) Print the `school_name` for both students again to see the change.

class Student:
    school_name = "Springfield Elementary"
    
    def __init__(self, student_name):
        self.student_name = student_name

student1 = Student("Jisoo")
student2 = Student("Lisa")
print(student1.school_name)
print(student2.school_name)


# 3. Instance Methods
#   a) Define a class `BankAccount`.
#   b) In `__init__`, initialize two instance attributes: `account_holder` and `balance` (set initial balance to 0).
#   c) Create an instance method `deposit` that takes an `amount` as an argument and adds it to the balance.
#   d) Create another instance method `withdraw` that takes an `amount` and subtracts it from the balance.
#   e) Create a method `get_balance` that prints the current balance.
#   f) Create an object, deposit some money, withdraw some, and then print the final balance.

class BankAccount:
    def __init__(self, account_holder):
        self.account_holder = account_holder
        self.balance = 0
    
    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        self.balance -= amount
    
    def get_balance(self):
        print(f"Current balance: {self.balance}")

account = BankAccount("Bob")
account.deposit(100)
account.withdraw(30)
account.get_balance()


# 4. Static Methods
#   a) Define a class `StringUtils`.
#   b) Create a static method `is_palindrome` that takes a string and returns `True` if it's a palindrome and `False` otherwise. (A palindrome reads the same forwards and backward).
#   c) The method should ignore case and spaces.
#   d) Call the static method directly on the class with a few test strings (e.g., "Racecar", "hello", "A man a plan a canal Panama").
#   Hint: `s.replace(' ', '').lower()` can help clean the string.

class StringUtils:
    @staticmethod
    def is_palindrome(s):
        cleaned = s.replace(' ', '').lower()
        return cleaned == cleaned[::-1]
print(StringUtils.is_palindrome("Racecar"))
print(StringUtils.is_palindrome("hello"))


# 5. Putting it all together
#   a) Create a class `Circle`.
#   b) Add a class attribute `pi` with the value 3.14159.
#   c) The `__init__` method should take a `radius`.
#   d) Create an instance method `calculate_area` that uses the `pi` class attribute and the instance's `radius` to calculate the area of the circle (Area = pi * r^2).
#   e) Create a static method `description` that simply prints "This is a utility class for circles."
#   f) Create a `Circle` object with a radius of 5 and print its area.
#   g) Call the static `description` method.

class Circle:
    pi = 3.14159
    
    def __init__(self, radius):
        self.radius = radius
    
    def calculate_area(self):
        return Circle.pi * (self.radius ** 2)
    
    @staticmethod
    def description():
        print("This is a utility class for circles.")
circle = Circle(5)
print(circle.calculate_area())

circle.description()
