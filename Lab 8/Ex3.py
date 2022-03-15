import random

class Point:
    def __init__(self, X, Y, Z):
        self.X = X
        self.Y = Y
        self.Z = Z
    
    def fill_point(self):
        self.X = random.randrange(0, 100)
        self.Y = random.randrange(0, 100)
        self.Z = random.randrange(0, 100)

def distance_between_points(p1, p2):
    return pow(pow(p1.X - p2.X, 2) + pow(p1.Y - p2.Y, 2) + pow(p1.Z - p2.Z, 2), 0.5)

def main():
    p1 = Point(0, 0, 0)
    p2 = Point(0, 0, 0)
    p1.fill_point()
    p2.fill_point()
    d = distance_between_points(p1, p2)
    print("The distance between the two points is: ", d)

if __name__ == "__main__":
    main()


