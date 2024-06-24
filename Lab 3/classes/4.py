class Location:
    def __init__(self, coordinates=[0, 0], shift=[0, 0], travel=0):
        self.coordinates = coordinates
        self.shift = shift
        self.travel = travel

    def display(self):
        print(self.coordinates)

    def relocate(self, delta_x, delta_y):
        self.travel = (((self.coordinates[0] - delta_x) ** 2) + ((self.coordinates[1] - delta_y) ** 2)) ** 0.5
        self.coordinates[0] += delta_x
        self.coordinates[1] += delta_y

    def distance(self):
        print(self.travel)

# Create an instance of Location
loc = Location(coordinates=[1, 1], shift=[0, 0], travel=0)
loc.display()
loc.relocate(delta_x=2, delta_y=6)
loc.display()
loc.distance()
