# Practice Questions: 01 - Classes and Objects

# 1. Basic Class and Object
#   a) Define a simple class named `Car`.
#   b) In the class body, use the `pass` statement for now.
#   c) Create two different objects (instances) of the `Car` class, named `car_1` and `car_2`.
#   d) Print both objects to see their memory addresses.

class Car:
    pass

car_1 = Car()
car_2 = Car()
print(car_1)
print(car_2)


# 2. Class with a Method
#   a) Define a class named `Book`.
#   b) Inside the class, define a method named `display_info` that prints the message "This is a book.".
#   c) Remember to include the `self` parameter in the method definition.
#   d) Create an object of the `Book` class named `my_book`.
#   e) Call the `display_info` method on the `my_book` object.

class Book:
    def display_info(self):
        print("This is a book.")
    
my_book = Book()
my_book.display_info()


# 3. Putting it all together
#   a) Define a class named `Calculator`.
#   b) Inside the class, define a method named `add` that takes two numbers (in addition to `self`) as arguments.
#   c) The `add` method should print the sum of the two numbers.
#   d) Create an instance of the `Calculator` class.
#   e) Call the `add` method with two numbers of your choice, for example, 5 and 10.

class Calculator:
    def add(self, num1, num2):
        print(num1 + num2)
calc = Calculator()
calc.add(5, 10)

