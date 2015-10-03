
from .node import Node
from nimbus.math.math import interpolate_from_table, goal_seek
from nimbus.reports import InputReport
from nimbus.data.couplelist import CoupleList


class Reservoir(Node):

    def __init__(self, name=None, start_stage=None, contours=None):
        super(Reservoir, self).__init__(name, start_stage)
        self.contours = CoupleList('Contours', ('Stage (ft)', 'Area (ac)'), contours)
        self.report = InputReport(self, self.contours)

    def get_area(self, elevation):
        if len(self.contours.list) > 1:
            area = interpolate_from_table(elevation, self.contours.list, 0, 1)
        else:
            area = 0.0
        return area

    def get_storage(self, elevation):
        if len(self.contours.list) > 1:
            min_elevation = min([contour[0] for contour in self.contours.list])
            max_elevation = max([contour[0] for contour in self.contours.list])
            if elevation <= min_elevation:
                storage = 0.0
                return storage
            elif elevation >= max_elevation:
                elevation = max_elevation
            new_contour = (elevation, self.get_area(elevation))
            contours = [contour for contour in self.contours.list if contour[0] < elevation] + [new_contour]
            storage = 0.0
            for i in range(1, len(contours)):
                prev_elevation = contours[i - 1][0]
                prev_area = contours[i - 1][1]
                elevation = contours[i][0]
                area = contours[i][1]
                storage += ((prev_area + area) / 2.0) * (elevation - prev_elevation)
        else:
            storage = 0.0
        return storage

    def get_stage(self, storage, time=None, tolerance=0.0001):
        if self.contours.list and len(self.contours.list) > 1:
            bound1 = self.contours.list[0][0]
            bound2 = self.contours.list[-1][0]
            max_iterations = 100
            stage = goal_seek(self.get_storage, bound1, bound2, storage, max_iterations, tolerance)
        else:
            stage = self.start_stage
        return stage
