
from .node import Node
from nimbus.math.math import interpolate_from_table
from nimbus.reports import InputReport
from nimbus.data.couplelist import CoupleList


class Boundary(Node):

    def __init__(self, name=None, start_stage=None, time_stages=None):
        super(Boundary, self).__init__(name, start_stage)
        self.time_stages = CoupleList('Time-Stages',
                                      ('Time (hr)', 'Stage (ft)'),
                                      time_stages)
        self.report = InputReport(self, self.time_stages)

    def get_stage(self, storage, time):
        stage = interpolate_from_table(time, self.time_stages.list, 0, 1)
        return stage
