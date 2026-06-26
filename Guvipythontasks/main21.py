#Vehicle task
class Vehicle:
    def __init__(self, model, rental_rate):
        self.model = model
        self.rental_rate = rental_rate

    def calculate_rental(self, days):
        return self.rental_rate * days

class Car(Vehicle):
    def calculate_rental(self, days):
        return self.rental_rate * days + 500   # extra charge

class Bike(Vehicle):
    def calculate_rental(self, days):
        return self.rental_rate * days

class Truck(Vehicle):
    def calculate_rental(self, days):
        return self.rental_rate * days + 1000  # extra charge


car = Car("Honda City", 2000)
bike = Bike("Royal Enfield", 500)
truck = Truck("Tata Truck", 5000)

days = 3

vehicles = [car, bike, truck]

for vehicle in vehicles:
    print(f"{vehicle.model} Rental Cost for {days} days = ₹{vehicle.calculate_rental(days)}")