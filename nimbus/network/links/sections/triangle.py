
import math

from .section import Section
from . import math as sm


class Triangle(Section):

    def __init__(self, rise, xs_slope, horizontal=False):
        super(Triangle, self).__init__(horizontal)
        self.rise = rise
        self.xs_slope = xs_slope

    def get_flow_area(self, depth):
        """Return the flow area in SF at a given depth from the invert of the shape."""
        if not self.horizontal:
            span = self.get_span()
        else:
            span = self.get_perimeter()
        flow_area = 0.5 * sm.inches2feet(depth) * sm.inches2feet(span)
        return flow_area

    def get_wet_perimeter(self, depth):
        """Return the wet perimeter in LF at a given depth from the invert of the shape."""
        if not self.horizontal:
            if depth >= self.rise:
                wet_perimeter = self.get_perimeter()
            else:
                c = math.hypot(self.get_span(), self.rise)
                wet_perimeter = depth + c
        else:
            wet_perimeter = self.get_perimeter()
        converted_perimeter = sm.inches2feet(wet_perimeter)
        return converted_perimeter

    def get_perimeter(self):
        c = math.hypot(self.get_span(), self.rise)
        perimeter = self.get_span() + self.rise + c
        return perimeter

    def get_rise(self):
        rise = self.rise
        return rise

    def get_span(self):
        span = self.rise / self.xs_slope
        return span
