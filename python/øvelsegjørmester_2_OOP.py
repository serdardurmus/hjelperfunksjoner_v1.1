# %%
class Employee:
    raise_amt = 1.04
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

class Developer(Employee):
    raise_amt = 1.10
    def __init__(self, first, last, pay, prog_language):
        super().__init__(first, last, pay)
        self.prog_language = prog_language

dev_1 = Developer("Martin", "Lane", 5000, "Python")
# dev_2 = Developer("Martin2", "Lane2", 4000)

print(dev_1.first)

# %% 
# Finaly Project

from abc import ABC, abstractmethod
# inheritance
class Shape(ABC):
    "Shape = super class / abstraction class"
    # abstraction method
    @abstractmethod
    def area(self): pass
    @abstractmethod
    def perimeter(self): pass
    # overriding and polymorphism
    def toString(self): pass

# child
class Square(Shape):
    "sub class"
    def __init__(self, edge):
        self.__edge = edge  # encapsulation private attribute
    def area(self):
        result = self.__edge ** 2
        print("Square area: ", result)
    def perimeter(self):
        result = self.__edge *4
        print("Square perimeter: ", result)
    # overriding and polymoprfhism
    def toString(self):
        print("Square edge:", self.__edge)

class Circle(Shape):
    "Circle class"
    PI = 3.14 # constant variable
    def __init__(self, radius):
        self.__radius = radius
    def area(self):
        result = self.PI * self.__radius ** 2 # pi*r**2
        print("Circle area: ", result)
    def perimeter(self):
        result = 2 * self.PI * self.__radius
        print("Circle perimeter: ", result)
    # overriding and polymoprfhism
    def toString(self):
        print("Circle edge:", self.__radius)

c = Circle(5)
c.area()
c.perimeter()
c.toString()

s = Square(5)
s.area()
s.perimeter()
s.toString()


# %% 
# Polymorphism

class Employee:
    def raisee(self):
        raise_rate = 0.1
        result = 100 + 100 * raise_rate
        print("Employee: ", result)
class CompEng(Employee):
    def raisee(self):
        raise_rate = 0.2
        result = 100 + 100 * raise_rate
        print("CompEng: ", result)
class EEEng(Employee):
    def raisee(self):
        raise_rate = 0.3
        result = 100 + 100 * raise_rate
        print("EEE: ", result)
e1 = Employee()
ce1 = CompEng()
eee1 = EEEng()

employee_list = [ce1, eee1]
for i in employee_list:
    print(i.raisee())

# %% 
# Overriding (Geçersiz kılma)
class Animal:
    def toString(self):
        print("animal")

class Monkey(Animal):
    def toString(self):
        print("monkey")

a1 = Animal()
a1.toString()

m1 = Monkey()
m1.toString()  # monkey calls overriding method



# %% 
# Abstract Classes (Soyut Klass)

from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def walk(self): pass
    @abstractmethod
    def run(self): pass

class Bird(Animal):
    def __init__(self):
        print("bird")
    def walk(self):
        print("walk")
    def run(self):
        print("run")
    def fly(self):
        print("fly")

b1 = Bird()
b1.walk()
b1.fly()




# %% 
# inheritance (mini project)
class Website:
    "parent"
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
    def loginInfo(self):
        print(self.name + " " + self.surname)

class Website1(Website):
    "child"
    def __init__(self, name, surname, ids):
        Website.__init__(self, name, surname)
        self.ids = ids
    def login(self):
        print(self.name + " " + self.surname + " " + self.ids)

p1 = Website("Serdar", "Durmus")
p2 = Website1("Ömer", "Durmus", "12345")

p1.loginInfo()
p2.login()




# %% 
# inheritance (kalıtım)

# parent
class Animal:
    def __init__(self):
        print("Animal is created")
    def toString(self):
        print("animal")
    def walk(self):
        print("Animal walk")
# child
class Monkey(Animal):
    def __init__(self):
        super().__init__() # use init if parent (animal) class
        print("Monkey is created")
    def toString(self):
        print("monkey")
    def climb(self):
        print("monkey can climb")

#child
class Bird(Animal):
    def __init__(self):
        super().__init__() # use init if parent (animal) class
        print("Bird is created")
    def toString(self):
        print("Bird")
    def fly(self):
        print("Bird can fly")

m1 = Monkey()
m1.toString()
m1.walk()

b1 = Bird()
b1.toString()
b1.fly()




# %% 
# encapsulation
class BankAccount(object):
    def __init__(self, name, money, address):
        self.__name = name
        self.__money = money
        self.__address = address
    
    def getMoney(self):
        return self.__money
    def setMoney(self, amount):
        self.__money = amount
    # private
    def __increase(self):
        self.__money = self.__money + 10000

person1 = BankAccount("Messi", 10000, "Barcelona")
person2 = BankAccount("Neymar", 20000, "Paris")

print("Get Moethod: ", person1.getMoney())
person1.setMoney(50000)
print("After Set Moethod: ", person1.getMoney())
person1.__increase()
print("After Set Moethod: ", person1.getMoney())



# %% 
# calculator project
class Calc(object):

    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2
    def add(self):
        return self.value1 + self.value2
    def multiply(self):
        return self.value2 * self.value1
    def division(self):
        return self.value1 / self.value2

print("Choose add(+), multiply(*), division(/)")
selection = input("select + or * or / ")
v1 = int(input("first value: "))
v2 = int(input("second value: "))

c = Calc(v1, v2)
if selection == "+": print(c.add())
elif selection == "*": print(c.multiply())
elif selection ==  "/": print(c.division())
else: print("Warning")



# %% 
# initializer or contructor

class Animal(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def getAge(self):
        return self.age

a1 = Animal("dog", 2)
print(a1.name)


# %% Question 
# a.getAge() = ?
class A:
    def __init__(self, age):
        self.age = age
        age = 15
    def getAge(self):
        return self.age
a = A(22)
print(a.getAge())


# %% 
# methods vs functions
class Emp(object):
    age = 25
    salary = 1000 # $
    def ageSalaryRation(self):
        print(self.age / self.salary)
# function
def ageSalaryRation(age, salary):
    print(age/salary)

e1 = Emp()
e1.ageSalaryRation()

ageSalaryRation(30, 3000)


# %% 
# methods
class Square(object):
    edge = 5 # meter
    area = 0
    def area1(self):
        self.area = self.edge*self.edge
        print(self.area)
s1 = Square()
print(s1)
print(s1.edge)
print(s1.area1())

s1.edge = 7
s1.area1()


# %% 
# Question: a.age =?
class A:
    global age
    age = 15
    def __init__(self, age):
        self.age = age

a = A(20)
print(a.age)

# %% OOP Tutorial_2

class Footballer:
    football_club = "Barcelona"
    age = 30
f1 = Footballer()
print(f1.age)
print(f1.football_club)

f1.football_club = "Real Madrit"
print(f1.football_club)

 # %% 
 # OOP Tutorial_1

first_name = "serdar"
last_name = "durmus"
mail = "serdardurmus@gmail.com"

class Employee(object):
    def __init__(self, first_name, last_name, mail):
        self.first_name = first_name
        self.last_name = last_name
        self.mail = mail

emp1 = Employee("Serdar","Durmus", "serdardurmus@gmail.com")

