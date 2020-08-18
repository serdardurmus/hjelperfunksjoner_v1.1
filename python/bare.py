class Employee:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
    
    @property
    def fullname(self):
        a = self.firstname + " " + self.lastname
        return a
    @property
    def email(self):
        eposta = (self.firstname+"."+self.lastname+"@company.com").lower()
        return eposta


emp_1 = Employee("John", "Smith")
emp_2 = Employee("Mary",  "Sue")
emp_3 = Employee("Antony", "Walker")

print(emp_1.fullname)
print(emp_2.email)
print(emp_3.firstname)