class Circel:
    def __init__(self, radius):
        self._radius = radius

    def get_radius(self):
        return self._radius

    def set_radius(self, new_radius):
        if isinstance(new_radius, float) and new_radius > 0:
            self._radius = new_radius
        else:
            print("Enter valid value for radius number:")


my_circel = Circel(5.1)
print(my_circel.get_radius())
my_circel.set_radius(63.21)
print(my_circel.get_radius())