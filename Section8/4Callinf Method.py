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


my_backpack = Backpack()
print(my_backpack.items)
my_backpack.add_items("Apple")
print(my_backpack.items)
my_backpack.add_items("banana")
print(my_backpack.items)
finditem = my_backpack.has_item("kiwi")
print(finditem)
my_backpack.remove_item("Apple")
print(my_backpack.items)
my_backpack.remove_item("banana")
print(my_backpack.items)
my_backpack.remove_item("lichy")
print(my_backpack.items)
