class Dog:
    # this attribute not instance
    species = "Canis Lupus"

    def __init__(self, name, age, breed, color):
        # (below attribute instance)
        self.name = name
        self.age = age
        self.breed = breed
        self.color = color

