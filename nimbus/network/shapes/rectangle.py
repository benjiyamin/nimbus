
from .shape import Shape
from .math import inches2feet


class Rectangle(Shape):

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
        flow_area = inches2feet(depth) * inches2feet(span)
        return flow_area

    def get_wet_perimeter(self, depth):
        """Return the wet perimeter in LF at a given depth from the invert of the shape."""
        if not self.horizontal:
            if depth == self.rise:
                wet_perimeter = 2.0 * inches2feet(self.span) + 2.0 * inches2feet(self.rise)
            else:
                wet_perimeter = inches2feet(self.span) + 2.0 * inches2feet(depth)
        else:
            perimeter = self.get_perimeter()
            wet_perimeter = inches2feet(perimeter)
        return wet_perimeter

    def get_perimeter(self):
        perimeter = 2.0 * self.span + 2.0 * self.rise
        return perimeter

    def get_equivalent_head(self, depth):
        equivalent_head = depth
        return equivalent_head
