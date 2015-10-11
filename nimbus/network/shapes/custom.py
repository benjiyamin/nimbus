
from .shape import Shape
from .math import inches2feet
import math


class Custom(Shape):

    def __init__(self, points, horizontal=False):
        super(Custom, self).__init__(horizontal)
        self.points = []

    def get_flow_area(self, depth):
        """Return the flow area in SF at a given depth from the invert of the shape."""
        if not self.horizontal:
            span = self.span
        else:
            span = self.get_perimeter()
        flow_area = inches2feet(depth) * inches2feet(span)
        return flow_area

    def get_wet_perimeter(self, depth):
        """Return the wet perimeter in LF at a given depth from the invert of the shape."""
        if not self.horizontal:
            max_y = max(point[1] for point in self.points)
            if depth >= max_y:
                wet_perimeter = self.get_perimeter()
            else:
                wet_perimeter = inches2feet(self.span) + 2.0 * inches2feet(depth)
        else:
            perimeter = self.get_perimeter()
            wet_perimeter = inches2feet(perimeter)
        return wet_perimeter

    def get_perimeter(self):
        perimeter = 0.0
        for i, point in enumerate(self.points):
            point1 = self.points[i - 1]
            point2 = point
            length = math.hypot(point2[0] - point1[0], point2[1] - point1[1])
            perimeter += length
        return perimeter

    def get_weir_flow(self, coefficient, depth):
        head = depth
        flow = coefficient * self.span * pow(head, 1.5)
        return flow
