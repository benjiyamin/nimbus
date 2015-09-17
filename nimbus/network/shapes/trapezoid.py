
from math import pow
from nimbus.network.shapes import Shape


class Trapezoid(Shape):

    def __init__(self, span, rise, left_slope, right_slope):
        self.span = span  # inches
        self.rise = rise  # inches
        self.left_slope = left_slope
        self.right_slope = right_slope
        super(Trapezoid, self).__init__(geometry='Trapezoid')

    def get_flow_area(self, depth):
        """Return the flow area in SF at a given depth from the invert of the shape."""
        left_area = self.left_slope * pow(depth / 12.0, 2.0) / 2.0
        center_area = depth * self.span / 12.0
        right_area = self.right_slope * pow(depth / 12.0, 2.0) / 2.0
        flow_area = left_area + center_area + right_area
        return flow_area

    def get_wet_perimeter(self, depth):
        """Return the wet perimeter in LF at a given depth from the invert of the shape."""
        if depth < self.rise:
            top_perimeter = 0.0
        else:
            top_perimeter = self.span + self.left_slope * depth + self.right_slope * depth
        left_perimeter = pow(pow(depth * self.left_slope, 2.0) + pow(depth, 2.0), 0.5)
        center_perimeter = self.span
        right_perimeter = pow(pow(depth * self.right_slope, 2.0) + pow(depth, 2.0), 0.5)
        wet_perimeter = left_perimeter + center_perimeter + right_perimeter + top_perimeter
        return wet_perimeter