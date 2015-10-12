
from .couplelist import CoupleList


class PointList(CoupleList):

    def __init__(self, parent, list_):
        self.parent = parent
        super(PointList, self).__init__('Points', ('X (in)', 'Y (in)'), list_)

    def create(self, value1, value2, order=False):
        """Create a new point and add it to the list."""
        super(PointList, self).create(value1, value2, order)
        self.parent.set_span_and_rise()
        return

    def delete(self, index):
        """Remove the point at the specified index from the list and delete it."""
        super(PointList, self).delete(index)
        self.parent.set_span_and_rise()
        return

    def copy(self, index, order=False):
        """Create a copy of the point at the specified index
        from the list and append it to the end of the list"""
        super(PointList, self).copy(index, order)
        self.parent.set_span_and_rise()
        return
