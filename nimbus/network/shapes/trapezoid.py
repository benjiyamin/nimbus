
from .shape import Shape
from .math import get_slope_area, get_slope_perimeter


class Trapezoid(Shape):

    def __init__(self, span, rise, left_slope, right_slope):
        self.span = span  # inches
        self.rise = rise  # inches
        self.left_slope = left_slope
        self.right_slope = right_slope
        super(Trapezoid, self).__init__()

    def get_flow_area(self, depth):
        """Return the flow area in SF at a given depth from the invert of the shape."""
        a = get_slope_area(self.left_slope, depth / 12.0)
        b = depth / 12.0 * self.span / 12.0
        c = get_slope_area(self.right_slope, depth / 12.0)
        flow_area = a + b + c
        return flow_area

    def get_wet_perimeter(self, depth):
        """Return the wet perimeter in LF at a given depth from the invert of the shape."""
        if depth < self.rise or not self.rise:
            d = 0.0
        else:
            d = self.span / 12.0 + self.left_slope * depth / 12.0 + self.right_slope * depth / 12.0
        a = get_slope_perimeter(self.left_slope, depth / 12.0)
        b = self.span
        c = get_slope_perimeter(self.right_slope, depth / 12.0)
        wet_perimeter = a + b + c + d
        return wet_perimeter

