class Rectangle:
    def __init__(self, height=0, breadth=0):  # zero for default meaning
        self.height = height
        self.breadth = breadth

    def compute_area(self):
        print(self.height * self.breadth)

class Cube(Rectangle):
    def __init__(self, height=0):
        super().__init__(height, height)

        # because the parent class                                
        # needs two arguments
        # we pass height=height and breadth=height

    def compute_area(self):
        print(self.height ** 2)

try:
    height, breadth = map(int, input("Enter height and breadth separated by space: ").split())
except ValueError:
    print("Please enter two integers separated by space.")
    height, breadth = 0, 0

myRectangle = Rectangle(height=height, breadth=breadth)
myRectangle.compute_area()

myCube = Cube(height=height)
myCube.compute_area()

myDefaultCube = Cube()
myDefaultCube.compute_area()
