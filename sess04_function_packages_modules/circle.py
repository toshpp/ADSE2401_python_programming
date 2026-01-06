# python file to define a circle class

# Import the required module(s)
import math   # allows the inbuilt pi and pow

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calc_area(self):
        # return math.pi * self.radius ** 2   # same as below line
        return math.pi * math.pow(self.radius, 2)

    def calc_perimeter(self):
        return math.pi * (2 * self.radius)

    def __str__(self):
        return (
            f"Circle Dimensions\n"
            f"{'-' * 40}\n"
            f"Radius: {self.radius}\n"
            f"Area: {self.calc_area():.2f}\n"
            f"Perimeter: {self.calc_perimeter():.2f}\n"
            f"{'-' * 40}"
        )
print(f"the documentation string of the calc_area() method is : \n{Circle(1).calc_area.__doc__}")