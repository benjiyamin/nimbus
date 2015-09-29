
from .node import Node
from nimbus.math import interpolate_from_table
from nimbus.reports import Report, show_objects_in_list


class Boundary(Node):

    def __init__(self, name=None, start_stage=None, time_stages=None, basins=None):
        if time_stages is None:
            self.time_stages = []
        else:
            self.time_stages = time_stages
        super(Boundary, self).__init__(name, start_stage, basins)

    def create_time_stage(self, time, stage):
        """Create a time-stage, add it to the time-stage list, and order the list by time."""
        new_time_stage = (time, stage)
        self.time_stages.append(new_time_stage)
        self.order_time_stages()
        self.show_time_stages()
        return

    def delete_time_stage(self, index):
        """Remove the time-stage at the specified index from the time-stage list and delete it."""
        time_stage = self.time_stages[index]
        self.time_stages.remove(time_stage)
        del time_stage
        self.show_time_stages()
        return

    def order_time_stages(self):
        """Order the time-stage list by time."""
        self.time_stages = sorted(self.time_stages, key=lambda time_stage: time_stage[0])
        return

    def show_time_stages(self):
        """Display all time-stages stored in the boundary's time-stage list."""
        show_objects_in_list('Time-Stages', self.time_stages)
        return

    def report_inputs(self, show_title=True):
        """Report all current inputs of the boundary"""
        report = Report()
        report.add_blank_line()
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
        report.add_blank_line()
        report.output()
        return

    def get_stage(self, storage, time):
        stage = interpolate_from_table(time, self.time_stages, 0, 1)
        return stage
