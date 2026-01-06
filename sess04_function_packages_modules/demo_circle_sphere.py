# python file to demonstrate working with user-defined custom class and instantiating them

# import the required modules
from circle import Circle
from sphere import Sphere

# prompt the user for the circles radius
radius = int(input(" PLease Enter radius of the circle: "))

# create/instantiate  a circles object
circle = Circle(radius)
circle2 = Sphere(radius)

# prompt the user for the speres radius
radius = int(input(" PLease Enter radius of the circle in cm: "))

# Create/instantiate a sphere object
sphere = Sphere(radius)

# Display the circles sphere dimensions
print(circle)
print(circle2)
