
from . import section as shp
from . import math as sm


class Trapezoid(shp.Shape):

    def __init__(self, span, rise, left_slope, right_slope, horizontal=False):
        super(Trapezoid, self).__init__(horizontal)
        self.span = span  # inches
        self.rise = rise  # inches
        self.left_slope = left_slope
        self.right_slope = right_slope

    def get_flow_area(self, depth):
        """Return the flow area in SF at a given depth from the invert of the shape."""
        if not self.horizontal:
            a = sm.get_slope_area(self.left_slope, sm.inches2feet(depth))
            b = sm.inches2feet(depth) * sm.inches2feet(self.span)
            c = sm.get_slope_area(self.right_slope, sm.inches2feet(depth))
            flow_area = a + b + c
        else:
            span = self.get_perimeter()
            flow_area = sm.inches2feet(depth) * sm.inches2feet(span)
        return flow_area

    def get_wet_perimeter(self, depth):
        """Return the wet perimeter in LF at a given depth from the invert of the shape."""
        if not self.horizontal:
            if depth < self.rise or not self.rise:
                d = 0.0
            else:
                d = self.span + self.left_slope * depth + self.right_slope * depth
            a = sm.get_slope_perimeter(self.left_slope, depth)
            b = sm.inches2feet(self.span)
            c = sm.get_slope_perimeter(self.right_slope, depth)
            wet_perimeter = a + b + c + d
        else:
            wet_perimeter = self.get_perimeter()
        converted_wet_perimeter = sm.inches2feet(wet_perimeter)
        return converted_wet_perimeter

    def get_perimeter(self):
        a = sm.get_slope_perimeter(self.left_slope, self.rise)
        b = sm.inches2feet(self.span)
        c = sm.get_slope_perimeter(self.right_slope, self.rise)
        d = sm.inches2feet(self.span) + self.left_slope * self.rise + self.right_slope * self.rise
        perimeter = a + b + c + d
        return perimeter

    def get_weir_flow(self, coefficient, depth):
        head1 = 0.0
        head2 = sm.inches2feet(depth)
        converted_span = sm.inches2feet(self.span)
        flow1 = coefficient * head2 * self.left_slope * (pow(head2, 2.5) - (pow(head1, 2.5))) / 2.5 / (head2 - head1)
        flow2 = coefficient * converted_span * pow(head2, 1.5)
        flow3 = coefficient * head2 * self.right_slope * (pow(head2, 2.5) - (pow(head1, 2.5))) / 2.5 / (head2 - head1)
        flow = flow1 + flow2 + flow3
        return flow
