class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move_up(self, change=5):
        self.y += change

    def move_down(self, change=5):
        self.y -= change

    def move_right(self, change=2):
        self.x += change

    def move_left(self, change=2):
        self.x -= change


my_palyer = Player(5, 10)
print(my_palyer.y)
my_palyer.move_down()
print(my_palyer.y)
