# %% 
# calculator project

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

