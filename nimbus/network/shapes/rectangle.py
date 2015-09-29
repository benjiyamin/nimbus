
from .shape import Shape


class Rectangle(Shape):

    def __init__(self, span, rise):
        self.span = span  # inches
        self.rise = rise  # inches
        super(Rectangle, self).__init__()

    def get_flow_area(self, depth):
        """Return the flow area in SF at a given depth from the invert of the shape."""
        flow_area = depth / 12.0 * self.span / 12.0
        return flow_area

    def get_wet_perimeter(self, depth):
        """Return the wet perimeter in LF at a given depth from the invert of the shape."""
        if depth == self.rise:
            wet_perimeter = 2.0 * self.span / 12.0 + 2.0 * self.rise / 12.0
        else:
            wet_perimeter = self.span / 12.0 + 2.0 * depth / 12.0
        return wet_perimeter
