# python file to define a sphere class

# import the required modules
from circle import Circle


class Sphere(Circle):
    def __init__(self, radius):
        super().__init__(radius)

    def calc_volume(self):
        """Returns the volume of the sphere."""
        return (4.0 / 3.0) * self.calc_area() * self.radius

    def calc_surface_area(self):
        """Returns the surface area of the sphere."""
        return 4.0 * self.calc_area()

    def __str__(self):
        return (
            f"Sphere Dimensions\n"
            f"{'-' * 40}\n"
            f"Radius: {self.radius}\n"
            f"Surface Area: {self.calc_surface_area():.2f}\n"
            f"Volume: {self.calc_volume():.2f}\n"
            f"{'-' * 40}"
        )
