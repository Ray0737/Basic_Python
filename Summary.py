# Python Summary Notes (Detailed)

#-----------------------------------------BASIC SYNTAX-----------------------------------------#

# Comments:
# Single-line comment
"""
Multi-line
comment
(docstring)
"""

# Variables: Dynamic typing, no explicit declaration needed
name = "Alice"
age = 30
height = 1.75
is_student = True

# Data Types (Built-in):
# Numbers: int, float, complex
integer_var = 10
float_var = 3.14
complex_var = 2 + 3j

# Strings: Immutable sequence of characters
string_var = "Hello, Python!"
multi_line_string = """This is
a multi-line
string."""

s1 = "Python"
s2 = "12345"
s3 = "Hello World"
s4 = "HelloWorld"
s5 = "helloworld"
s6 = "1.23"

print(s1.isalpha())   # True (contains only alphabetic characters)
print(s2.isdigit())   # True (contains only digits)
print(s2.isnumeric()) # True (more general, includes unicode numbers)
print(s2.isdecimal()) # True (subset of numeric, decimal digits)
print(s3.isspace())   # False (contains only whitespace characters)
print(" ".isspace())  # True
print(s4.isalnum())   # True (contains only alphanumeric characters)
print(s5.islower())   # True (all cased characters are lowercase)
print(s1.isupper())   # False (all cased characters are uppercase)
print("HELLO".isupper()) # True
print(s1.istitle())   # True (first letter of each word is uppercase, rest lowercase)
print(s6.isdecimal()) # False (contains a dot)
print(s6.isdigit())   # False (contains a dot)

# Booleans: True/False (case-sensitive)
bool_true = True
bool_false = False

# None: Represents the absence of a value
none_var = None

# Type Conversion (Casting):
int_to_float = float(10)      # 10.0
float_to_int = int(3.9)       # 3 (truncates)
str_to_int = int("123")       # 123
int_to_str = str(456)         # "456"

# Input/Output:
# user_input = input("Enter something: ") # Always returns a string
# print("You entered:", user_input)
# print(f"Name: {name}, Age: {age}") # F-strings (formatted string literals)

# Operators:
# Arithmetic: +, -, *, /, // (floor division), % (modulo), ** (exponentiation)
result_add = 5 + 3    # 8
result_div = 10 / 3   # 3.333...
result_floor = 10 // 3 # 3
result_mod = 10 % 3   # 1
result_exp = 2 ** 3   # 8

# Comparison: == (equal), != (not equal), <, >, <=, >=
is_equal = (5 == 5)   # True
is_greater = (10 > 5) # True

# Logical: and, or, not
logical_and = (True and False) # False
logical_or = (True or False)   # True
logical_not = (not True)       # False

# Assignment: =, +=, -=, *=, /=, //=, %=, **=
x = 10
x += 5  # x is now 15

# Identity: is, is not (compares memory location)
a = [1, 2]
b = [1, 2]
c = a
print(a is b) # False (different objects)
print(a is c) # True (same object)

# Membership: in, not in (checks for presence in a sequence)
my_list = [1, 2, 3]
print(2 in my_list)     # True
print(4 not in my_list) # True

# Bitwise: &, |, ^, ~, <<, >> (less common for general programming)

#-----------------------------------------DATA STRUCTURE-----------------------------------------#

# Lists: Ordered, mutable, allows duplicates
my_list = [1, "hello", 3.14, True, 1]
print(my_list[0])      # Access by index: 1
print(my_list[-1])     # Last element: 1
my_list.append("new")  # Add to end
my_list.insert(1, "inserted") # Insert at specific index
my_list.remove("hello") # Remove first occurrence of value
my_list.pop()          # Remove and return last element
my_list.pop(0)         # Remove and return element at index 0
# my_list.sort()       # Sorts in-place (if elements are comparable)
# my_list.reverse()    # Reverses in-place
sliced_list = my_list[1:3] # Slicing (start:end-1)
print(len(my_list))    # Length

# Tuples: Ordered, immutable, allows duplicates
my_tuple = (1, "hello", 3.14)
print(my_tuple[0])     # Access by index: 1
# my_tuple[0] = 2      # Error: Tuples are immutable
print(my_tuple.count("hello")) # Count occurrences
print(my_tuple.index(3.14))    # Get index of value

# Sets: Unordered, mutable, no duplicates
my_set = {1, 2, 3, 2, 1} # {1, 2, 3}
my_set.add(4)
my_set.remove(1)
set_union = {1, 2}.union({3, 4})       # {1, 2, 3, 4}
set_intersection = {1, 2}.intersection({2, 3}) # {2}
print(len(my_set))

# Dictionaries: Unordered, mutable, key-value pairs, keys must be unique and immutable
my_dict = {"name": "Alice", "age": 30, "city": "New York"}
print(my_dict["name"])      # Access by key: Alice
my_dict["age"] = 31         # Update value
my_dict["email"] = "alice@example.com" # Add new key-value pair
del my_dict["city"]         # Delete by key
print(my_dict.keys())       # Get all keys
print(my_dict.values())     # Get all values
print(my_dict.items())      # Get all key-value pairs as tuples
print("name" in my_dict)    # Check if key exists

#-----------------------------------------CONTROL FLOW-----------------------------------------#

# Conditional Statements (if, elif, else):
age = 25
if age < 18:
    print("Minor")
elif 18 <= age < 65:
    print("Adult")
else:
    print("Senior")

# Loops:

# For loop (iterating over sequences)
for char in "Python":
    print(char)

for i in range(5): # range(start, stop, step)
    print(i) # 0, 1, 2, 3, 4

for index, value in enumerate(["a", "b", "c"]):
    print(f"Index: {index}, Value: {value}")

# While loop (executes as long as a condition is true)
count = 0
while count < 3:
    print(count)
    count += 1

# Loop Control Statements:
# break: Exits the loop
for i in range(10):
    if i == 5:
        break
    print(i) # Prints 0, 1, 2, 3, 4

# continue: Skips the rest of the current iteration and goes to the next
for i in range(5):
    if i == 2:
        continue
    print(i) # Prints 0, 1, 3, 4

# pass: A null operation; does nothing. Used as a placeholder.
if True:
    pass # To be implemented later

#-----------------------------------------FUNCTION-----------------------------------------#

# Defining a function:
def greet(name="Guest"): # Default parameter value
    """
    This function greets the user.
    Docstrings explain what the function does.
    """
    return f"Hello, {name}!"

# Calling a function:
message = greet("Bob")
print(message)
print(greet()) # Uses default "Guest"

# Positional and Keyword Arguments:
def describe_person(name, age):
    print(f"{name} is {age} years old.")

describe_person("Alice", 30)       # Positional
describe_person(age=25, name="Bob") # Keyword arguments (order doesn't matter)

# Arbitrary Arguments (*args and **kwargs):
def sum_all(*args): # Accepts any number of positional arguments as a tuple
    total = 0
    for num in args:
        total += num
    return total

print(sum_all(1, 2, 3, 4)) # 10

def print_info(**kwargs): # Accepts any number of keyword arguments as a dictionary
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(city="London", population=9000000)

# Lambda Functions (Anonymous Functions):
add_one = lambda x: x + 1
print(add_one(5)) # 6

# Higher-order functions (e.g., map, filter, sorted)
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x*x, numbers)) # [1, 4, 9, 16, 25]
evens = list(filter(lambda x: x % 2 == 0, numbers)) # [2, 4]

# --- 5. OBJECT-ORIENTED PROGRAMMING (OOP) ---

# Classes and Objects:
class Dog:
    # Class attribute
    species = "Canis familiaris"

    # Constructor method (__init__)
    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age    # Instance attribute

    # Instance method
    def bark(self):
        return f"{self.name} says Woof!"

    def get_info(self):
        return f"{self.name} is {self.age} years old."

# Creating objects (instances of the class)
my_dog = Dog("Buddy", 5)
your_dog = Dog("Lucy", 3)

print(my_dog.name)        # Access instance attribute
print(my_dog.bark())      # Call instance method
print(Dog.species)        # Access class attribute

# Inheritance:
class GoldenRetriever(Dog): # GoldenRetriever inherits from Dog
    def __init__(self, name, age, color):
        super().__init__(name, age) # Call parent class constructor
        self.color = color

    # Overriding a method
    def bark(self):
        return f"{self.name} says Yelp!"

    def retrieve(self, item):
        return f"{self.name} retrieved the {item}!"

goldie = GoldenRetriever("Max", 2, "golden")
print(goldie.get_info())
print(goldie.bark())      # Calls overridden method
print(goldie.retrieve("ball"))
print(goldie.species)     # Inherited class attribute

# Encapsulation (using conventions for private attributes):
class Account:
    def __init__(self, balance):
        self.__balance = balance # Convention for "private" attribute (name mangling)

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

# Polymorphism (different objects responding to the same method call)
# (Illustrated implicitly by overridden methods in inheritance)

# Abstraction (using abstract base classes - requires 'abc' module)
# from abc import ABC, abstractmethod
#
# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass
#
# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
#     def area(self):
#         return 3.14 * self.radius ** 2

# --- 6. MODULES AND PACKAGES ---

# Modules: Python files containing code (functions, classes, variables)
# Import a built-in module
import math
print(math.pi)
print(math.sqrt(16))

# Import specific items
from math import pi, sqrt
print(pi)

# Alias an import
import random as rnd
print(rnd.randint(1, 10))

# Custom Modules: Create a file (e.g., my_module.py) with functions
# # my_module.py:
# def say_hello(name):
#     return f"Hello, {name} from my_module!"
#
# # In another file:
# import my_module
# print(my_module.say_hello("World"))

# Packages: Collections of modules in directories (with __init__.py files)
# Example structure:
# my_package/
#   __init__.py
#   module1.py
#   sub_package/
#       __init__.py
#       module2.py
#
# # Importing from a package:
# from my_package import module1
# from my_package.sub_package import module2

# --- 7. EXCEPTION HANDLING ---

# try-except block:
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
except TypeError as e: # Catch specific error and get error object
    print(f"Type error: {e}")
except Exception as e: # Catch any other exception
    print(f"An unexpected error occurred: {e}")
else:
    print("Division successful!") # Executes if no exception occurred
finally:
    print("This block always executes.") # Executes regardless of exception

# Raising exceptions:
# def validate_age(age):
#     if not isinstance(age, (int, float)):
#         raise TypeError("Age must be a number.")
#     if age < 0:
#         raise ValueError("Age cannot be negative.")
#     print("Age is valid.")
#
# try:
#     validate_age(-5)
# except (TypeError, ValueError) as e:
#     print(f"Validation error: {e}")

# --- 8. FILE I/O ---

# Opening and closing files (using 'with' statement for automatic closing)
# 'r' - read (default), 'w' - write (creates/overwrites), 'a' - append, 'x' - create, 'b' - binary, 't' - text (default)

# Writing to a file:
# with open("my_file.txt", "w") as f:
#     f.write("Hello, world!\n")
#     f.write("This is a new line.\n")

# Reading from a file:
# with open("my_file.txt", "r") as f:
#     content = f.read()     # Reads entire file
#     print(content)
#
# with open("my_file.txt", "r") as f:
#     lines = f.readlines()  # Reads all lines into a list
#     for line in lines:
#         print(line.strip()) # .strip() removes leading/trailing whitespace (including newline)
#
# with open("my_file.txt", "r") as f:
#     for line in f:         # Iterating directly over file object is memory efficient
#         print(line.strip())

# Appending to a file:
# with open("my_file.txt", "a") as f:
#     f.write("Appended line.\n")

# --- 9. ADVANCED TOPICS (Briefly) ---

# Decorators: Functions that modify the behavior of other functions
# def my_decorator(func):
#     def wrapper():
#         print("Something is happening before the function is called.")
#         func()
#         print("Something is happening after the function is called.")
#     return wrapper
#
# @my_decorator
# def say_whee():
#     print("Whee!")
#
# say_whee()

# Generators: Functions that return an iterator (using 'yield')
def countdown(n):
    while n > 0:
        yield n
        n -= 1

# for num in countdown(3):
#     print(num) # 3, 2, 1

# Context Managers: Objects that define 'with' statement behavior (e.g., file handling)
# Implemented using __enter__ and __exit__ methods or the @contextmanager decorator.

# List, Dictionary, Set Comprehensions: Concise ways to create data structures
squares = [x**2 for x in range(5)] # [0, 1, 4, 9, 16]
even_dict = {x: x*2 for x in range(5) if x % 2 == 0} # {0: 0, 2: 4, 4: 8}
unique_chars = {char for char in "hello"} # {'h', 'e', 'l', 'o'}

# Iterators and Iterables:
# An iterable is an object capable of returning its members one at a time (e.g., list, tuple, string).
# An iterator is an object that represents a stream of data (has __iter__() and __next__() methods).

# Regular Expressions (re module): For pattern matching in strings.
import re
pattern = r"apple"
text = "I have an apple and an orange."
match = re.search(pattern, text)
if match:
    print(f"Found '{match.group()}' at index {match.start()}")

# --- END OF SUMMARY ---
