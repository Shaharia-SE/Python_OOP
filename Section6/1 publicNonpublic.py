class Car:
     def __init__(self, brand, model, year):
         self.brand = brand
         self.model = model
         self.year = year
my_car = Car("Toyota", "xyz", 2020)
print(my_car.year)
my_car.year = 2025
print(my_car.year)
