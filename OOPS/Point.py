
class Point:
    def __init__(self, a, b):
        self.x = a
        self.y = b

    def display(self):
        print(f"X = {self.x}")
        print(f"X = {self.y}")
    
    def __add__(self, other):
        """Overload the + operator"""
        if isinstance(other, Point):
            temp = Point(self.x + other.x, self.y + other.y)
        elif isinstance(other, str):
            temp = Point(self.x + int(other), self.y + int(other))
        elif isinstance(other, int):
            temp = Point(self.x + other, self.y + other)
        return temp
    
    def __radd__(self, other):
        """Right-side addition (when Point is on right side)"""
        pass

    def __repr__(self):
        return f"Point is ({self.x}, {self.y})"


if __name__ == "__main__":
    X = 1
    Y = 2
    #print(f"X = {X}")
    #print(f"Y = {Y}")

    pt1 = Point(1, 2)
    pt2 = Point(11, 12)
    #print(pt1)

    Z = X + Y
    print(f"Z = {Z}")
    pt3 = pt1 + pt2
    print(pt3)

    pt4 = pt1 + "3"
    print(pt4)
