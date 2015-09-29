
from math import sin

from .shape import Shape
from .math import get_alpha


class Circle(Shape):

    def __init__(self, diameter):
        self.diameter = diameter  # inches
        self.span = diameter  # inches
        self.rise = diameter  # inches
        super(Circle, self).__init__()

    def get_flow_area(self, depth):
        """Return the flow area in SF at a given depth from the invert of the shape."""
        alpha = get_alpha(depth / 12.0, self.diameter / 12.0)
        flow_area = (pow(self.diameter / 12.0, 2.0) / 4.0) * (alpha - (sin(2.0 * alpha) / 2.0))
        return flow_area

    def get_wet_perimeter(self, depth):
        """Return the wet perimeter in LF at a given depth from the invert of the shape."""
        alpha = get_alpha(depth / 12.0, self.diameter / 12.0)
        wet_perimeter = alpha * self.diameter / 12.0
        return wet_perimeter
