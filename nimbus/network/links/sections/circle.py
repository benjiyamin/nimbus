
import math

from . import section as shp
from . import math as sm


class Circle(shp.Shape):

    def __init__(self, diameter, horizontal=False):
        super(Circle, self).__init__(horizontal)
        self.diameter = diameter  # inches
        self.span = diameter      # inches
        self.rise = diameter      # inches

    def get_flow_area(self, depth):
        """Return the flow area in SF at a given depth from the invert of the shape."""
        if not self.horizontal:
            alpha = sm.get_alpha(sm.inches2feet(depth), sm.inches2feet(self.diameter))
            flow_area = (pow(sm.inches2feet(self.diameter), 2.0) / 4.0) * (alpha - (math.sin(2.0 * alpha) / 2.0))
        else:
            span = self.get_perimeter()
            flow_area = sm.inches2feet(depth) * sm.inches2feet(span)
        return flow_area

    def get_wet_perimeter(self, depth):
        """Return the wet perimeter in LF at a given depth from the invert of the shape."""
        if not self.horizontal:
            alpha = sm.get_alpha(sm.inches2feet(depth), sm.inches2feet(self.diameter))
            wet_perimeter = alpha * sm.inches2feet(self.diameter)
        else:
            perimeter = self.get_perimeter()
            wet_perimeter = sm.inches2feet(perimeter)
        return wet_perimeter

    def get_perimeter(self):
        perimeter = 2.0 * math.pi * self.diameter / 2.0
        return perimeter
