class Polygon:
    def __init__(self, side1=0, side2=0):  # zero for default meaning
        self.side1 = side1
        self.side2 = side2

    def compute_area(self):
        print(self.side1 * self.side2)

class Rectangle(Polygon):
    def __init__(self, side1, side2):
        super().__init__(side1, side2)

    def compute_area(self):
        print(self.side1 * self.side2)

try:
    side1, side2 = map(int, input("Enter two sides separated by space: ").split())
except ValueError:
    print("Please enter two integers separated by space.")
    side1, side2 = 0, 0

myRectangle = Rectangle(side1=side1, side2=side2)
myRectangle.compute_area()

