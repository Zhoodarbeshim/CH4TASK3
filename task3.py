class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0
        self.fuel = 70
    
    def drive(self, km):
        self.km = km
        self.add_distance(km)
        
        self.subtract_fuel(km)
        if self.fuel > 0:

            return f"{self.make}--{self.model}--{self.year}. Let's drive! You can drive {self.fuel * 10} km more!"
        else:
            return f"Need more fuel, please fill more!"

    def add_distance(self, km):
        self.odometer += km

    def subtract_fuel(self,km):
        self.fuel -= km/10

car = Car(
    "Honda", "Jazz", "2009")
car.drive(250)
print(car.drive(250))