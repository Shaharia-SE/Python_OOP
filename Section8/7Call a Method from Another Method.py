class Backpack:
    def __init__(self):
        self._items = []

    @property
    def items(self):
        return self._items

    def add_multiple_items(self, items):
        for item in items:
            self.add_items(item)

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
my_backpack.add_multiple_items(["apple","banana","orange"])
print(my_backpack.items)
