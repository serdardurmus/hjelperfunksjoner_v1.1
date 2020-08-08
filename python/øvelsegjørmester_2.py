



# %% 
# inheritance (mini project)





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

