class Backpack:
    def __init__(self):
        self._items = []

    @property
    def items(self):
        return self._items

    def add_items(self, item):
        if isinstance(item, str):
            self._items.append(item)
        else:
            print(" Please enter a valid item")

    def remove_item(self, item):
        if item in self._items:
            self._items.remove(item)
            return 1
        else:
            print("This item is not in the Ackpack")
            return 0

    def has_item(self, item):
        return item in self._items

    def show_items(self, sorted_list=False):
        if sorted_list:
            print(sorted(self._items))
        else:
            print(self._items)
my_backpack = Backpack()
my_backpack.add_items("water")
my_backpack.add_items("apple")
my_backpack.add_items("orange")

print("Not Shorted")
my_backpack.show_items()
print("Sorted")
my_backpack.show_items(True)
