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
print(dev_1.prog_language)