# %%
class ones_threes_nines:
    def __init__(self, number):
        self.number = number
    def nines(self):
        return (self.number//9)
    def threes(self):
        return (self.number//3)
    def ones(self):
        return (self.number)
n1 = ones_threes_nines(5)
print(n1.nines())
print(n1.threes())
print(n1.ones())
# %%
class ones_threes_nines:
    def __init__(self, number):
        self.number = number
    @property
    def nines(self):
        a = self.number // 9
        return a
    @property
    def threes(self):
        a = self.number // 3
        return a
    @property
    def ones(self):
        a = self.number
        return a

n1 = ones_threes_nines(5)
print(n1.nines)
print(n1.threes)
print(n1.ones)

# %%
class Employee:
	def __init__(self, firstname, lastname):
		self.firstname = firstname
		self.lastname = lastname
    @property
    def fullname(self):
        fullname = self.firstname + " " + self.lastname
        return fullname
    @property
    def email(self):
        eposta = self.firstname+"."+self.lastname+"@company.com"
        return eposta


emp_1 = Employee("John", "Smith")
emp_2 = Employee("Mary",  "Sue")
emp_3 = Employee("Antony", "Walker")

print(emp_1.fullname)
print(emp_2.email)
print(emp_3.firstname)
# %%
