
from . import section as shp
from . import math as sm


class Rectangle(shp.Shape):

    def __init__(self, span, rise, horizontal=False):
        super(Rectangle, self).__init__(horizontal)
        self.span = span  # inches
        self.rise = rise  # inches

    def get_flow_area(self, depth):
        """Return the flow area in SF at a given depth from the invert of the shape."""
        if not self.horizontal:
            span = self.span
        else:
            span = self.get_perimeter()
        flow_area = sm.inches2feet(depth) * sm.inches2feet(span)
        return flow_area

    def get_wet_perimeter(self, depth):
        """Return the wet perimeter in LF at a given depth from the invert of the shape."""
        if not self.horizontal:
            if depth >= self.rise:
                wet_perimeter = self.get_perimeter()
            else:
                wet_perimeter = self.span + 2.0 * depth
        else:
            wet_perimeter = self.get_perimeter()
        converted_perimeter = sm.inches2feet(wet_perimeter)
        return converted_perimeter

    def get_perimeter(self):
        perimeter = 2.0 * self.span + 2.0 * self.rise
        return perimeter

    def get_weir_flow(self, coefficient, depth):
        converted_head = sm.inches2feet(depth)
        converted_span = sm.inches2feet(self.span)
        flow = coefficient * converted_span * pow(converted_head, 1.5)
        return flow
