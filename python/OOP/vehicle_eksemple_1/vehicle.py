import datetime

# parent class
class VehicleRent:

    def __init__(self, stock):
        self.stock = stock
        self.now = 0

    def displayStock(self):
        "display Stock"
        print("{} vehicle available to rent".format(self.stock))
        return self.stock
    def rentHourly(self, n):
        "rent Hourly"
        if n <=0: 
            print("Number should be positive")
            return None
        elif n > self.stock:
            print("Sorry {} vehicle available to rent".format(self.stock))
            return None
        else:
            self.now = datetime.datetime.now()

    def rentDaily(self, n):
        "rent rentDaily"
        pass
    def returnVehicle(self, request, brand):
        "return a bill"
        pass
        

# child class 1
class CarRent(VehicleRent):

    def __init__():
        pass
    def discount():
        "discount "
        pass

# child class 2
class BikeRent(VehicleRent):

    def __init__():
        pass

# customer
class Customer:
    def __init__():
        pass
    def requestVehicle():
        "request vehicle"
        pass
    def returnVehicle():
        "return vehicle"
        pass