

class ones_threes_nines:
    def __init__(self, number):
        self.number = number
    def nines(self):
        return int(self.number/9)
    def threes(self):
        return int(self.number/3)
    def ones(self):
        return int(self.number)
n1 = ones_threes_nines(5)
print(n1.nines())
print(n1.threes())
print(n1.ones())