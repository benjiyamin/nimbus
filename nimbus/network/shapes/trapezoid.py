
from .shape import Shape
from .math import get_slope_area, get_slope_perimeter, inches2feet


class Trapezoid(Shape):

    def __init__(self, span, rise, left_slope, right_slope, horizontal=False):
        super(Trapezoid, self).__init__(horizontal)
        self.span = span  # inches
        self.rise = rise  # inches
        self.left_slope = left_slope
        self.right_slope = right_slope

    def get_flow_area(self, depth):
        """Return the flow area in SF at a given depth from the invert of the shape."""
        if not self.horizontal:
            a = get_slope_area(self.left_slope, inches2feet(depth))
            b = inches2feet(depth) * inches2feet(self.span)
            c = get_slope_area(self.right_slope, inches2feet(depth))
            flow_area = a + b + c
        else:
            span = self.get_perimeter()
            flow_area = inches2feet(depth) * inches2feet(span)
        return flow_area

    def get_wet_perimeter(self, depth):
        """Return the wet perimeter in LF at a given depth from the invert of the shape."""
        if not self.horizontal:
            converted_depth = inches2feet(depth)
            if depth < self.rise or not self.rise:
                d = 0.0
            else:
                d = inches2feet(self.span) + self.left_slope * converted_depth + self.right_slope * converted_depth
            a = get_slope_perimeter(self.left_slope, converted_depth)
            b = inches2feet(self.span)
            c = get_slope_perimeter(self.right_slope, converted_depth)
            wet_perimeter = a + b + c + d
        else:
            wet_perimeter = self.get_perimeter()
        return wet_perimeter

    def get_perimeter(self):
        converted_rise = inches2feet(self.rise)
        a = get_slope_perimeter(self.left_slope, converted_rise)
        b = inches2feet(self.span)
        c = get_slope_perimeter(self.right_slope, converted_rise)
        d = inches2feet(self.span) + self.left_slope * converted_rise + self.right_slope * converted_rise
        perimeter = a + b + c + d
        return perimeter

    def get_equivalent_head(self, depth, iterations=20):
        pass
