from math import ceil

from nimbus.network.nodes.node import Node
from nimbus.math import interpolate_from_table
from nimbus.reports import Report, float_to_string, property_to_string


class Boundary(Node):

    def __init__(self, start_stage=None, time_stages=None, name=None, basins=None):
        self.start_stage = start_stage
        if time_stages is None:
            self.time_stages = []
        else:
            self.time_stages = time_stages
        super(Boundary, self).__init__(name, basins)

    def get_stage(self, storage, time):
        stage = interpolate_from_table(time, self.time_stages, 0, 1)
        return stage
    
    def order_time_stages(self):
        self.time_stages = sorted(self.time_stages, key=lambda time_stage: time_stage[0])
        return

    def create_time_stage(self, time, stage):
        new_time_stage = (time, stage)
        self.time_stages.append(new_time_stage)
        self.order_time_stages()
        return

    def delete_time_stage(self, index):
        time_stage = self.time_stages[index]
        self.time_stages.remove(time_stage)
        del time_stage
        return

    def report_inputs(self, title=True):
        title = 'Boundary'
        col1_title = 'Time (hr)'
        col2_title = 'Stage (ft)'
        report = Report()
        if title:
            report.add_title(title)
        inputs = self.get_inputs()
        for string in inputs:
            report.add_string_line(string)
        report.add_blank_line()
        entries = [col1_title, col2_title]
        report.add_to_columns(entries)
        report.add_columns_line(len(entries))
        for time_stage in self.time_stages:
            report.add_to_columns(["{:.3f}".format(time_stage[0]), "{:.3f}".format(time_stage[1])])
        report.output()
        return

    def get_inputs(self):
        inputs = ['Name: ' + property_to_string(self, 'name'),
                  'Starting Stage (ft): ' + float_to_string(self.start_stage, 3)]
        return inputs
