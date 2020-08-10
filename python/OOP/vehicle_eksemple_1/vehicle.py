
# parent class
class VehicleRent:

    def __init__(self, stock):
        pass
    def displayStock(self):
        "display Stock"
        pass
    def rentHourly(self, n):
        "rent Hourly"
        pass
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
        pass
    def returnVehicle():
        pass