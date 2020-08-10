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
            print("Rented a {} vehicle for hourly at {} hours".format(n, self.now.hour))
            self.stock -= n
            return self.now

    def rentDaily(self, n):
        "rent rentDaily"
        if n <=0: 
            print("Number should be positive")
            return None
        elif n > self.stock:
            print("Sorry {} vehicle available to rent".format(self.stock))
            return None
        else:
            self.now = datetime.datetime.now()
            print("Rented a {} vehicle for daily at {} hours".format(n, self.now.hour))
            self.stock -= n
            return self.now        

    def returnVehicle(self, request, brand):
        "return a bill"
        car_hours_price = 10
        car_daily_price = car_hours_price * 8 / 10 * 24
        bike_hours_price = 5 
        bike_daily_price =bike_hours_price * 7 / 10 * 24

        rentalTime, rentalBasis, numOfVehicle = request
        bill = 0

        if brand ==  "car":
            if rentalTime and rentalBasis and numOfVehicle:
                self.stock += numOfVehicle
                now = datetime.datetime.now()
                rentalPeriod = now - rentalTime

                if rentalBasis == 1:  # hourly
                    bill = rentalPeriod.second/3600*car_hours_price*numOfVehicle
                elif rentalBasis == 2:  # daily
                    bill = rentalPeriod.second/(3600*24)*car_daily_price*numOfVehicle
                if (2 <= numOfVehicle):
                    print("You have extra 20% discount")
                    bill = bill * 0.8
                print("Thank yo for returning your car")
                print("Price: $ {}".format(bill))
                return bill
        elif brand ==  "bike":
            if rentalTime and rentalBasis and numOfVehicle:
                self.stock += numOfVehicle
                now = datetime.datetime.now()
                rentalPeriod = now - rentalTime

                if rentalBasis == 1:  # hourly
                    bill = rentalPeriod.second/3600*bike_hours_price*numOfVehicle
                elif rentalBasis == 2:  # daily
                    bill = rentalPeriod.second/(3600*24)*bike_daily_price*numOfVehicle
                if (4 <= numOfVehicle):
                    print("You have extra 20% discount")
                    bill = bill * 0.8
                print("Thank yo for returning your bike")
                print("Price: $ {}".format(bill))
                return bill
        else:
            print("YOu do not rent a vehicle")
            return None
        

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