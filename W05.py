#Exercise 1 Lv: Moderate
num = 1
while num < 20:
    if num == 19:
        print(num, end= "")
        break
    else:
        print(num,end = ", ")
        num=num+2

#Exericse 02 Lv: Moderate
for i in [10,20,30,40,50,60,70]:
    print(i)

#Exercise 03 Lv: Moderate
for i in range(0,19,2):
    print(i)

#Exercise 04 Lv: Moderate
for i in range(0,101,3):
    if i%3 == 0:
        print(i)

# Exercise 05 Lv: Moderate
x = 9
for i in range(9):
    print("i"*x)
    x=x-1

#Exercise 06: Lv: Advanced
for i in range(1,10):
    print("-" * (9-i) , end="")
    for j in range(1,i+1):
        print(j,end="")
    print()  

#Exercise 07: Lv: Advanced
line = {}
text = input("Enter sth: ")

for ch in text:
    if ch == ' ':
        continue
    line[ch] = line.get(ch,0)+1
for ch in sorted(line):
    print(ch,line[ch])

#Exercise 08: Lv: Advanced
x = input("Enter stuff (q to quit): ")
y = []
n=0
while True:
    if x == "q":
        break
    else:
        x = float(x)
        y.append(x)
        n = n+1
        x = input("Enter stuff (q to quit): ")
        avg = (sum(y))/n
if n==0 and x == "q":
        print("No data")
else:
    print(f"{avg:.2f}")

#Exercise 09: Lv: Advanced
h = int(input("Enter the height of the triangle: "))
for i in range(1, h + 1):
    extspace = h - i
    if i == 1:
        print(" " * extspace + "*")
    elif i == h:
        base_len = 2 * h - 1
        print("*" * base_len)
    else:
        intspace = 2 * i - 3
        print(" " * extspace + "*" + " " * intspace + "*")

#Exercise 10: Lv: Moderate
num = []
x = input("Enter sth: ")
y = input("Enter sth: ")
z = input("Enter sth: ")
a = input("Enter sth: ")
b = input("Enter sth: ")
num.append(x)
num.append(y)
num.append(z)
num.append(a)
num.append(b)
num.sort()
print(num[2])

#Exercise 11: Lv: Advanced
import math
size_input = input("Enter the size of the X pattern: ")
size = int(size_input)
for i in range(math.ceil(size/2)):
    line_chars = ['-'] * size
    line_chars[i] = 'X'
    if i != size - 1 - i: # check if its at the last index
        line_chars[size - 1 - i] = 'X' # start moving into the middle
    print("".join(line_chars))
if size%2 != 0:     
    for i in range(size // 2 - 1, -1, -1): #round down and invert to last index
        line_chars = ['-'] * size
        line_chars[i] = 'X'
        line_chars[size - 1 - i] = 'X'
        print("".join(line_chars))
else:
    for i in range(size // 2 - 2, -1, -1): #round down and invert to last index
        line_chars = ['-'] * size
        line_chars[i] = 'X'
        line_chars[size - 1 - i] = 'X'
        print("".join(line_chars))