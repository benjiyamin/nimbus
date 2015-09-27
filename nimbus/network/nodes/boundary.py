
from nimbus.network.nodes.node import Node
from nimbus.math import interpolate_from_table
from nimbus.reports import Report, show_object_list


class Boundary(Node):

    def __init__(self, name=None, start_stage=None, time_stages=None, basins=None):
        if time_stages is None:
            self.time_stages = []
        else:
            self.time_stages = time_stages
        super(Boundary, self).__init__(name, start_stage, basins)

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
        self.show_time_stages()
        return

    def delete_time_stage(self, index):
        time_stage = self.time_stages[index]
        self.time_stages.remove(time_stage)
        del time_stage
        self.show_time_stages()
        return

    def show_time_stages(self):
        show_object_list('Time-Stages', self.time_stages)
        return

    def report_inputs(self, show_title=True):
        report = Report()
        if show_title is True:
            title = 'Boundary'
            report.add_title(title)
        inputs = self.get_inputs()
        for string in inputs:
            report.add_string_line(string)
        report.add_blank_line()
        entries = ['Time (hr)', 'Stage (ft)']
        report.add_to_columns(entries)
        report.add_columns_line(len(entries))
        for time_stage in self.time_stages:
            report.add_to_columns(["{:.3f}".format(time_stage[0]), "{:.3f}".format(time_stage[1])])
        report.output()
        return
