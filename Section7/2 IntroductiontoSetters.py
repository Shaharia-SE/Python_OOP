class Dog:
    def __init__(self, name, age):
        self._name = name
        self.age = age

    def get_name(self):
        return self._name

    def set_name(self, new_name):
        if isinstance(new_name, str) and new_name.isalnum():
            self._name = new_name
        else:
            print("Enter valid name")


my_dog = Dog("Kukur", 14)

print("My Dog name is:", my_dog.get_name())
my_dog.set_name(545)
print("Her new name is:", my_dog.get_name())
