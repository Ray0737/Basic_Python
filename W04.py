'''
Week 04 | Control Flow
'''

#Exercise 01 
num = int(input("Enter an integer: "))
if num > 0:
    print(f"{num} is more than 0")
elif num <= 0:
    print(f"{num} is less than or equal to 0")

#Exercise 02 
width = int(input("Enter the width in cm: "))
length = int(input("Enter the length in cm: "))
area = width*length
if width and length > 0:
    print(f"The area of the rectangle = {area} cm^2 ")
else:
    print("Please fill in with (+) integer")

#Exercise 03 
temp = float(input("Enter the temp in °F: "))
if temp >= 32:
    c = ((temp-32)/9)*5
    print(f"Temp in celsius = {c}°C")
elif temp < 32:
    print("cool")

#Exercise 04 
gpa = float(input("Enter the score (x/100): "))
gpa = round(gpa)
if gpa >= 80:
    print("Grade 4")
elif gpa >= 75:
    print("Grade 3.5")
elif gpa >= 70:
    print("Grade 3")
elif gpa >= 65:
    print("Grade 2.5")
elif gpa >= 60:
    print("Grade 2")
elif gpa >= 55:
    print("Grade 1.5")
elif gpa >= 50:
    print("Grade 1")
elif gpa < 50:
    print("0")

#Exercise 05 
hr = int(input("Enter how long you stay in (hr): "))
min =int(input("Enter how long you stay in (min): "))
if (hr < 0) or (min < 0):
    print("Please fill in with (+) integer")
elif hr > 1:
    if min >= 0:
        hr = hr+1
        bill = hr*30
    elif hr > 1 and min == 0:
        bill = hr*30
    print(f"You total bill is {bill} THB")
elif (hr == 1) or (min <= 60):
    print("free")

#Exercise 06 
member = input("Are you member or not (Yes/No): ")
if member == "Yes":
    bill = float(input("Enter your total bill: "))
    if bill >= 5000:
        discount = (bill/100)*15
        new_bill = bill - discount
        print(f"bill = {bill} THB\ndiscount = {discount} THB\nNew bill = {new_bill}")
    elif bill >= 1000:
        discount = (bill/100)*10
        new_bill = bill - discount
        print(f"bill = {bill} THB\ndiscount = {discount} THB\nNew bill = {new_bill}")
    elif bill >= 500:
        discount = (bill/100)*5
        new_bill = bill - discount
        print(f"bill = {bill} THB\ndiscount = {discount} THB\nNew bill = {new_bill}")
elif member == "No":
    print("No discount for you ;-;")

#Exercise 07 
print("Bank only have 1000THB, 500THB, and 100THB banknotes")
withdraw = int(input("Enter the amount of withdraw: "))
if withdraw % 100 == 0:
    bank1000 = withdraw // 1000
    withdraw = withdraw % 1000
    bank500 = withdraw //500
    withdraw = withdraw % 500
    bank100 = withdraw //100
    print(f"n bank1000 = {bank1000}\nn bank500 = {bank500}\nn bank100 = {bank100}")
else:
    print("withdraw unable")

    

        





  


