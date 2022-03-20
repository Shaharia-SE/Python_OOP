class Dog:
    def __init__(self, age):
        self._age = age

    def get_age(self):
        print("calling getter......")
        return self._age

    def set_age(self, new_age):
        print("calling the setters......")
        if isinstance(new_age, int) and 0 < new_age < 30:
            self._age = new_age
        else:
            print(" Please enter valid age ")

    age = property(get_age, set_age)


my_dog = Dog(20)
print(f"my dog is {my_dog.get_age()}years old")
print("one year leter.......")
my_dog.age += 1
print(f"my dog is {my_dog.get_age()}years old")
