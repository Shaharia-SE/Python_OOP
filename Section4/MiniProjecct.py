"""
Welcome to this Mini Project.

This time, you are hired to fix the software that was developed for your local bakery store. The previous developer added many bugs on purpose due to conflicts with the manager. The store owner is extremely worried that this failure will seriously affect her business and sales.

But you can save the day by fixing the classes that throw errors.


------------------

- Your job is to fix the existing code.

- You have determined that three classes throw errors: Donuts, Customer, Cake. Their files are included as downloadable resources below. The code is also included right here as formatted text. You must fix the errors on each one of them to restore the system.

- Submit the classes after fixing the errors.

------------------

"""


class Donut:
    def _ini__(self, flavor, toppings, filling, size):
        self.flavor = flavor
        self.toppings = toppings
        self.filling = filling
        self.size = size


class Customer:
    def __init__(self, name, age, address, favorite_dessert):
        self.name = name
        self.age = age
        self.address = address
        self.favorite_dessert = favorite_dessert


class Cake:
    def __init__(self, flavor, price, quality):
        self.flavor = flavor
        self.price = price
        self.quality = quality
