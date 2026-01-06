# Python script to demonstrate decorating a class (using a logger function)

# Define the logger decorator
def log_dimensions(cls):
    def wrapper(*args, **kwargs):
        print(f"Logging dimensions for class: {cls.__name__}")
        rectangle = cls(*args, **kwargs)
        print("Rectangle dimensions logged!")
        return rectangle

    return wrapper


@log_dimensions
class Rectangle:
    def __init__(self, width=0, length=0):
        self.width = width
        self.length = length

    def get_width(self):
        return self.width

    def get_length(self):
        return self.length

    def calculate_perimeter(self):
        return 2 * (self.width + self.length)

    def calculate_area(self):
        return self.width * self.length

    def __str__(self):
        return (
            f"Rectangle's dimensions\n"
            f"{'-' * 45}\n"
            f"Width: {self.width} cm\n"
            f"Length: {self.length} cm\n"
            f"Perimeter: {self.calculate_perimeter()} cm\n"
            f"Area: {self.calculate_area()} cm²"
        )


# Prompt the user for the dimensions of a new rectangle
length = int(input("Enter the length of the rectangle: "))
width = int(input("Enter the width of the rectangle: "))

# Create a rectangle object
rectangle = Rectangle(width, length)

# Print the rectangle
print(rectangle)
