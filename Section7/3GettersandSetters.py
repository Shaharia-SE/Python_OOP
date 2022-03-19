class Backpack:
    def __init__(self):
        self._items = []

    def get_items(self):
        return self._items

    def set_itms(self, new_items):

        if isinstance(new_items, list):
            self._items = new_items
        else:
            print("Enter valid list of item")


my_backpack = Backpack()
print(my_backpack.get_items())
my_backpack.set_itms(["Md Shaharia Safat Rony", "Sufka", "jony"])
print(my_backpack.get_items())
