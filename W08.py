'''
Week 08 | Object-Oriented Programming
'''

class Employee:
    def __init__(self) -> None:
        print("Default Constructor")
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def edit_salary(self, name, salary):
        self.name = name
        self.salary = salary
    def showdata(self):
        print(f"Name: {self.name}")
        print(f"Salary: {self.salary}")
emp1 = Employee("John Doe", 50000)
emp1.showdata()
emp1.edit_salary("Jane Doe", 60000)
emp1.showdata()

class animal: 
    def showdata(self):
        print("Aomsin")

class fighterjet:
    def detail(self,x):
        self.name = "F22" and "Raptor"
        self.missile = "AIM-120" and "AIM-9"
        self.cannon = "M61A2"
        self.radarcrosssection = 0.001
        self.killcount= x
        print(f"Aircraft:{self.name}")
        print(f"Missile: {self.missile} ")
        print(f"Aircraft:{self.cannon}")
        print(f"Aircraft:{self.radarcrosssection}")
        print(f"Aircraft:{self.killcount}")

Raptor = fighterjet()
Raptor.detail(1)


class Businessman:
    def __init__(self, hp, money, happiness):
        self.hp = hp
        self.money = money
        self.happiness = happiness
    def work(self):
        self.hp -= 10
        self.money += 10
        self.happiness -= 20
    def sleep(self):
        self.hp += 20
        self.money -= 10
        self.happiness += 10
    def play(self):
        self.hp -= 10
        self.money -= 10
        self.happiness += 20
    def showdata(self):
        print(f"HP: {self.hp}, Money: {self.money}, Happiness: {self.happiness}")
man1 = Businessman(100, 100, 100)
man1.showdata()
man1.work()
man1.showdata()
man1.sleep()
man1.showdata()
man1.play()

man1.showdata()
