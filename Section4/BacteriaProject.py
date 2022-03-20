"""

You have been hired to develop educational software for a small school district. This particular software teaches microbiology using interactive games.


--------------

For this assignment, you need to write a Bacteria class to represent the enemies. This class must have 5 instance attributes. You must research online and determine which instance attributes you would like to include in the class. This simulates a real world scenario where you would need to determine the instance attributes of your class.

You also need to include these instance attributes: self.x and self.y to represent the coordinates of the instance on the computer screen. The values of x and y should be passed as arguments to __init__() and then assigned.

After defining your Bacteria class, you need to create 3 instances of this class. You can choose the initial values that will be passed as arguments to create the instance.

Note: the class will have 5 attributes total. To help you choose the instance attributes, think about the most useful attributes for an enemy in a game that explains microbiology. For example, you could add a life_counter attribute as a generic attribute that is not specific to bacteria. You could also add attributes that are specific to bacteria, such as their classification or shape.

--------------

You are in complete control of this assignment, so customize it to your liking. There is a Bacteria.py file included with this assignment (below) that you can download to write your class.

Submit your class to complete the assignment.

"""

class Bacteria:
    def __init__(self, x, y, shape, resistant, is_gram_positive):
        self.x = x
        self.y = y
        self.shape = shape
        self.resistant = resistant  # True if resistant to antibiotics; otherwise False.
        self.is_gram_positive = is_gram_positive


bacteria1 = Bacteria(50, 60, "coccus", True, True)
bacteria2 = Bacteria(50, 260, "bacillus", False, False)
bacteria3 = Bacteria(150, 200, "tetrad", True, True)
print(bacteria1.x)
print(bacteria2.y)
print(bacteria3.shape)