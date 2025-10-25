# Exercise 1-2 Lv: Moderate
a = input("Enter your sth")
x = type(a)
print(f"{a} {x}")

# Exercise 3-4 Lv: Moderate
name = input("Enter your name")
x = type(name)
print(f"your name is {name} \nYour have enter the value in {x}")

# Exercise 5 Lv: Moderate
num1 = float(input("enter a number"))
num2 = float(input("enter a number"))
addition = num1 + num2
x = type(addition)
subtraction = num1-num2
y = type(subtraction)
multiplication = num1*num2
z = type(multiplication)
division = num1/num2
a = type(division)
print(f"{num1} + {num2} = {addition} \nYour ans has the value in {x}")
print(f"{num1} - {num2} = {subtraction} \nYour ans has the value in {y}")
print(f"{num1} x {num2} = {multiplication} \nYour ans has the value in {z}")
print(f"{num1} ÷ {num2} = {division} \nYour ans has the value in {a}")

# Exercise 6 Lv: Moderate
a = float(input("Enter a real number"))
b = int(input("enter a integer"))
addition = a+b
x = type(addition)
subtraction = a-b
y = type(subtraction)
print(f"{a} + {b} = {addition} \nYour ans has the value in {x}")
print(f"{a} - {b} = {subtraction} \nYour ans has the value in {y}")

# Exercise 7 Lv: Moderate
force = float(input("whats the force (N)"))
distance = float(input("Whats the distance (M)"))
time = float(input("What's the time of the action"))
work = force*distance
power = work/time
print(f"your work is {work} Jules \nand the total power is {power} Watt")

# Exercise 8-9 Lv: Moderate
firstname = input("enter your firstname")
surname = input("Enter your surname")
age = int(input("Enter your age ininteger"))
age_sister = int(input("Enter your sister's age ininteger"))
print(f"your name is {firstname} {surname}, and you're {age} years old, and you have a sister withe the age of {age_sister} years old, and the age gap is {age - age_sister}")

#Exercise 10-12 Lv: Moderate
x = float(input("enter a number"))
y = float(input("enter a number"))
result_1 = x>y
print(bool(result_1))
print(type(result_1))

# Exercise 13 Lv: Moderate
import math
radius = float(input("Enter the radius of the base of the cone (Cm)"))
height = float(input("Enter the height of your cone (Cm)"))
volume = (1/3)*math.pi*(radius**2)*height
print(f"The volume of your cone is {volume} Cubic Centimeter")

