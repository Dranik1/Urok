class Vehicle:
    def __init__(self, make, model, year, price):
        self.make=make
        self.model=model
        self.year=year
        self.price=price

    def total_vehicles(self):
        Vehicle.total+=self.price
        print(f"Auto cena ir {Vehicle.total}")
        return Vehicle.total

    def display_info(self):
        print(f"Marka: {self.make}"
              f"\nModele: {self.model}"
              f"\nIzlaiduma gads: {self.year}"
              f"\nCena: {self.price} euro")

class Car(Vehicle):
    def __init__(self, make, model, year, price, num_doors, body_style):
        super().__init__(make, model, year, price)
        self.num_doors=num_doors
        self.body_style=body_style

class Truck(Vehicle):
    def __init__(self, make, model, year, price, bed_length, towing_capacity):
        super().__init__(make, model, year, price)
        self.bed_length=bed_length
        self.towing_capacity=towing_capacity

car=Car("Toyota", "Camry", 2022, 29000, 4, "sedan")
car.display_info()

truck=Truck("Ford", "F-Max", 2013, 30000, "6162", "13 t")
truck.display_info()