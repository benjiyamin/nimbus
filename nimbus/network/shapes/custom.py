
import math

from . import shape as shp
from . import math as sm
from nimbus.data import point as pt


class Custom(shp.Shape):

    def __init__(self, points=None, horizontal=False):
        super(Custom, self).__init__(horizontal)
        self.points = pt.PointList(self, points)
        self.span = self.rise = 0.0
        self.set_span_and_rise()

    def set_span_and_rise(self):
        if self.points.length() == 0:
            self.span = self.rise = 0.0
        else:
            max_x = max([p[0] for p in self.points.all()])
            min_x = min([p[0] for p in self.points.all()])
            max_y = max([p[1] for p in self.points.all()])
            min_y = min([p[1] for p in self.points.all()])
            self.span = max_x - min_x
            self.rise = max_y - min_y
        return

    def get_flow_area(self, depth):
        """Return the flow area in SF at a given depth from the invert of the shape."""
        if not self.horizontal:
            flow_area = 0.0
            min_y = min(p[1] for p in self.points.all())
            for i, p in self.points.enumerate():
                point1 = self.points.get(i - 1)
                point2 = p
                head1 = depth - sm.inches2feet(point1[1] - min_y)
                head2 = depth - sm.inches2feet(point2[1] - min_y)
                span = sm.inches2feet(abs(point2[0] - point1[0]))
                if head1 <= 0.0 and head2 <= 0.0:
                    flow_area += 0.0
                elif head1 == head2:
                    flow_area += span * head2
                elif head1 <= 0.0 or head2 <= 0.0:
                    max_head = max(head1, head2)
                    min_head = min(head1, head2)
                    ratio = max_head / (max_head - min_head)
                    span *= ratio
                    head2 = max_head
                    flow_area += 0.5 * span * head2
                else:
                    max_head = max(head1, head2)
                    min_head = min(head1, head2)
                    flow_area += span * min_head + 0.5 * span * (max_head - min_head)
        else:
            span = self.get_perimeter()
            flow_area = sm.inches2feet(depth) * sm.inches2feet(span)
        return flow_area

    def get_wet_perimeter(self, depth):
        """Return the wet perimeter in LF at a given depth from the invert of the shape."""
        if not self.horizontal:
            max_y = max(p[1] for p in self.points.all())
            if depth >= max_y:
                wet_perimeter = self.get_perimeter()
            else:
                wet_perimeter = 0.0
                min_y = min(p[1] for p in self.points.all())
                for i, p in self.points.enumerate():
                    point1 = self.points.get(i - 1)
                    point2 = p
                    head1 = depth - sm.inches2feet(point1[1] - min_y)
                    head2 = depth - sm.inches2feet(point2[1] - min_y)
                    span = sm.inches2feet(abs(point2[0] - point1[0]))
                    if head1 <= 0.0 and head2 <= 0.0:
                        wet_perimeter += 0.0
                    elif head1 == head2:
                        wet_perimeter += span
                    elif head1 <= 0.0 or head2 <= 0.0:
                        max_head = max(head1, head2)
                        min_head = min(head1, head2)
                        ratio = max_head / (max_head - min_head)
                        span *= ratio
                        wet_perimeter += math.hypot(span, max_head - min_head)
                    else:
                        max_head = max(head1, head2)
                        min_head = min(head1, head2)
                        wet_perimeter += math.hypot(span, max_head - min_head)
        else:
            perimeter = self.get_perimeter()
            wet_perimeter = sm.inches2feet(perimeter)
        return wet_perimeter

    def get_perimeter(self):
        perimeter = 0.0
        for i, p in self.points.enumerate():
            point1 = self.points.get(i - 1)
            point2 = p
            length = math.hypot(point2[0] - point1[0], point2[1] - point1[1])
            perimeter += length
        return perimeter

    def get_weir_flow(self, coefficient, depth):
        min_y = min(p[1] for p in self.points.all())
        flow = 0.0
        for i, p in self.points.enumerate():
            point1 = self.points.get(i - 1)
            point2 = p
            head1 = depth - sm.inches2feet(point1[1] - min_y)
            head2 = depth - sm.inches2feet(point2[1] - min_y)
            span = sm.inches2feet(abs(point2[0] - point1[0]))
            if head1 <= 0.0 and head2 <= 0.0:
                flow += 0.0
            elif head1 == head2:
                flow += coefficient * span * pow(head2, 1.5)
            elif head1 <= 0.0 or head2 <= 0.0:
                max_head = max(head1, head2)
                min_head = min(head1, head2)
                ratio = max_head / (max_head - min_head)
                span *= ratio
                head1 = 0.0
                head2 = max_head
                flow += coefficient * span * (pow(head2, 2.5) - (pow(head1, 2.5))) / 2.5 / (head2 - head1)
            else:
                flow += coefficient * span * (pow(head2, 2.5) - (pow(head1, 2.5))) / 2.5 / (head2 - head1)
        return flow
