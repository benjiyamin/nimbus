
from nimbus.network.nodes.node import Node
from nimbus.math import interpolate_from_table, goal_seek
from nimbus.reports import Report, show_objects_in_list


class Reservoir(Node):

    def __init__(self, name=None, start_stage=None, contours=None, basins=None):
        if contours is None:
            self.contours = []
        else:
            self.contours = contours
        super(Reservoir, self).__init__(name, start_stage, basins)

    def create_contour(self, elevation, area):
        """Create a contour, add it to the contour list, and order the list by elevation."""
        new_contour = (elevation, area)
        self.contours.append(new_contour)
        self.order_contours()
        self.show_contours()
        return

    def delete_contour(self, index):
        """Remove the contour at the specified index from the contour list and delete it."""
        contour = self.contours[index]
        self.contours.remove(contour)
        self.show_contours()
        del contour
        return

    def order_contours(self):
        """Order the contour list by time."""
        self.contours = sorted(self.contours, key=lambda contour: contour[0])
        return

    def show_contours(self):
        """Display all contours stored in the reservoir's contour list."""
        show_objects_in_list('Contours', self.contours)
        return

    def report_inputs(self, show_title=True):
        """Report all current inputs of the reservoir"""
        report = Report()
        report.add_blank_line()
        if show_title is True:
            title = 'Reservoir'
            report.add_title(title)
        inputs = self.get_inputs()
        for string in inputs:
            report.add_string_line(string)
        report.add_blank_line()
        entries = ['Stage (ft)', 'Area (ac)']
        report.add_to_columns(entries)
        report.add_columns_line(len(entries))
        for contour in self.contours:
            report.add_to_columns(["{:.3f}".format(contour[0]), "{:.3f}".format(contour[1])])
        report.add_blank_line()
        report.output()
        return

    def get_area(self, elevation):
        if self.contours and len(self.contours) > 1:
            area = interpolate_from_table(elevation, self.contours, 0, 1)
        else:
            area = 0.0
        return area

    def get_storage(self, elevation):
        if self.contours and len(self.contours) > 1:
            min_elevation = min([contour[0] for contour in self.contours])
            max_elevation = max([contour[0] for contour in self.contours])
            if elevation <= min_elevation:
                storage = 0.0
                return storage
            elif elevation >= max_elevation:
                elevation = max_elevation
            new_contour = (elevation, self.get_area(elevation))
            contours = [contour for contour in self.contours if contour[0] < elevation] + [new_contour]
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
        if self.contours and len(self.contours) > 1:
            bound1 = self.contours[0][0]
            bound2 = self.contours[-1][0]
            max_iterations = 100
            stage = goal_seek(self.get_storage, bound1, bound2, storage, max_iterations, tolerance)
        else:
            stage = self.start_stage
        return stage
