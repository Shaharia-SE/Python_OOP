class Backpack:
    def __init__(self):
        self._items = []

    @property
    def items(self):
        print("calling getter.....")
        return self._items

    @items.setter
    def items(self, new_items):
        print("calling setter .........")
        if isinstance(new_items, list):
            self._items = new_items
        else:
            print("Please Enter a valid list of items")


my_backpack = Backpack()

print(my_backpack.items)
my_backpack.items = ["water", "suger", "pepsi"]
print(my_backpack.items)