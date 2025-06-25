import math

class Circle:
    def __init__(self, radius=None, diameter=None):
        if radius is not None:
            self.radius = float(radius)
        elif diameter is not None:
            self.radius = float(diameter) / 2
        else:
            raise ValueError("You must specify radius or diameter")

    @property
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diameter(self, value):
        self.radius = float(value) / 2

    @property
    def area(self):
        return math.pi * self.radius ** 2

    def __str__(self):
        return f"Circle(radius={self.radius:.2f}, diameter={self.diameter:.2f}, area={self.area:.2f})"

    def __repr__(self):
        return f"Circle(radius={self.radius})"

    def __add__(self, other):
        if isinstance(other, Circle):
            return Circle(radius=self.radius + other.radius)
        return NotImplemented

    def __gt__(self, other):
        return isinstance(other, Circle) and self.radius > other.radius

    def __lt__(self, other):
        return isinstance(other, Circle) and self.radius < other.radius

    def __eq__(self, other):
        return isinstance(other, Circle) and math.isclose(self.radius, other.radius, rel_tol=1e-9)


# Example usage
if __name__ == "__main__":
    c1 = Circle(radius=5)
    c2 = Circle(diameter=10)
    c3 = Circle(radius=7)

    print(c1)         
    print(c2)         
    print(c1 == c2)   
    print(c1 < c3)    

    c4 = c1 + c3
    print(c4)         

    circles = [c3, c1, c4, c2]
    circles.sort()
    print("Sorted circles:", circles)
