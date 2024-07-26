# polymorphism_demo.py
import math

class Shape:
    def area(self):
        """Method to be overridden by derived classes to calculate the area."""
        raise NotImplementedError("Subclasses must override the area() method.")

class Rectangle(Shape):
    def __init__(self, length, width):
        """Initializes a Rectangle instance with length and width."""
        self.length = length
        self.width = width

    def area(self):
        """Calculates and returns the area of the rectangle."""
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        """Initializes a Circle instance with radius."""
        self.radius = radius

    def area(self):
        """Calculates and returns the area of the circle."""
        return math.pi * (self.radius ** 2)
