
import math

from .shape import Shape
from .math import get_alpha, inches2feet


class Circle(Shape):

    def __init__(self, diameter, horizontal=False):
        super(Circle, self).__init__(horizontal)
        self.diameter = diameter  # inches
        self.span = diameter      # inches
        self.rise = diameter      # inches

    def get_flow_area(self, depth):
        """Return the flow area in SF at a given depth from the invert of the shape."""
        if not self.horizontal:
            alpha = get_alpha(inches2feet(depth), inches2feet(self.diameter))
            flow_area = (pow(inches2feet(self.diameter), 2.0) / 4.0) * (alpha - (math.sin(2.0 * alpha) / 2.0))
        else:
            span = self.get_perimeter()
            flow_area = inches2feet(depth) * inches2feet(span)
        return flow_area

    def get_wet_perimeter(self, depth):
        """Return the wet perimeter in LF at a given depth from the invert of the shape."""
        if not self.horizontal:
            alpha = get_alpha(inches2feet(depth), inches2feet(self.diameter))
            wet_perimeter = alpha * inches2feet(self.diameter)
        else:
            perimeter = self.get_perimeter()
            wet_perimeter = inches2feet(perimeter)
        return wet_perimeter

    def get_perimeter(self):
        perimeter = 2.0 * math.pi * self.diameter / 2.0
        return perimeter
