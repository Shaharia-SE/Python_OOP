class Pizza:
    price = 12.5

    def __init__(self, description, toppling, crust):
        self.description = description
        self.toppling = toppling
        self.crust = crust


print(Pizza.price)
my_pizza = Pizza("Margherita", ["Basil", "Mushrooms"], "New York Style")
print(my_pizza.price)
Pizza.price = 16.87
print(Pizza.price)
print(my_pizza.price)