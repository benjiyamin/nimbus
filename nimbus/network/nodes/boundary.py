from math import ceil

from nimbus.network.nodes.node import Node
from nimbus.math import interpolate_from_table, goal_seek
from nimbus.reports import Report


class Boundary(Node):

    def __init__(self, start_stage=None, time_stages=None, name=None, basins=None):
        self.start_stage = start_stage
        self.name = name
        if time_stages is None:
            self.time_stages = []
        else:
            self.time_stages = time_stages
        super(Boundary, self).__init__(basins)

    def get_stage(self, storage, time):
        stage = interpolate_from_table(time, self.time_stages, 0, 1)
        return stage

    def report_inputs(self, col_length=15):
        title = ' Boundary '
        col1_title = 'Time (hr)'
        col2_title = 'Stage (ac)'
        report = Report()
        report.add_title(title)
        report.add_string_line('Name: ' + str(self.name))
        report.add_string_line('Starting Stage: ' + str(self.start_stage))
        report.add_blank_line()
        report.add_two_columns(col1_title, col2_title)
        report.add_two_columns('-' * col_length, '-' * col_length)
        for contour in self.time_stages:
            report.add_two_columns(str(round(contour[0], 4)), str(round(contour[1], 4)))
        report.output()
