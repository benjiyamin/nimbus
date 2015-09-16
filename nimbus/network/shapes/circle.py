__author__ = 'MillerB'

from math import acos, sin


class Circle:

    def __init__(self, diameter):
        self.diameter = diameter  # inches
        self.span = diameter  # inches
        self.rise = diameter  # inches

    def get_alpha(self, depth):
        """Return the alpha value utilized for circular hydraulics."""
        alpha = acos(1.0 - (depth / 12.0) / (self.diameter / 2.0 / 12.0))
        return alpha

    def get_flow_area(self, depth):
        """Return the flow area in SF at a given depth from the invert of the shape."""
        alpha = self.get_alpha(depth)
        flow_area = (pow(self.diameter / 12.0, 2.0) / 4.0) * (alpha - (sin(2.0 * alpha) / 2.0))
        return flow_area

    def get_wet_perimeter(self, depth):
        """Return the wet perimeter in LF at a given depth from the invert of the shape."""
        alpha = self.get_alpha(depth)
        wet_perimeter = alpha * self.diameter / 12.0
        return wet_perimeter