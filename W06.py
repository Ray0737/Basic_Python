'''
Week 06 | Functions
'''

#Exercise 00 
def print_name (realname1,surname1,age1):
    print(f"Hello {realname1} {surname1}, You're {age1} Years old")

realname = input("Enter realname: ")
surname = input("Enter surname: ")
age = int(input("Enter age: "))
print_name(realname,surname,age)

#Exercise 01
def bmi_calculator (w1,h1):
    h1 = h1/100
    bmi = w1/((h1)**2)
    print(f"Your BMI: {bmi:.2f}")

w = float(input("Enter your weight in kg: "))
h = float(input("Enter your heiht in Cm: "))
bmi_calculator(w,h)

#Exercise 02
def calculator (n1,n2,op1):
    if op1 == "+":
        return print(n1+n2)
    if op1 == "-":
        return print(n1-n2)
    if op1 == "*":
        return print(n1*n2)
    if op1 == "/":
        return print(n1/n2)
    
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operator = input("Choose Operator (+|-|*|/): ")
calculator(num1,num2,operator)


#Exercise 03 
def find_max_min(nlist):
    sort1 = sorted(nlist)
    a = sort1[0]
    b = sort1[-1]
    print(f"Lowest num = {a} | highest num = {b}")

numlist = []
while True:
    a = input("Enter any num (q to quit): ")
    if a == "q":
        break
    else:
        a = float(a)
        numlist.append(a)

find_max_min(numlist)

