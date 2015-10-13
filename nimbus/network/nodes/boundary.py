
from . import node
from nimbus.math import math as nm
from nimbus.reports import input as inp
from nimbus.data import couple as cpl


class Boundary(node.Node):

    def __init__(self, name=None, start_stage=None, time_stages=None):
        super(Boundary, self).__init__(name, start_stage)
        self.time_stages = cpl.CoupleList('Time-Stages',
                                             ('Time (hr)', 'Stage (ft)'),
                                             time_stages)
        self.report = inp.InputReport(self, self.time_stages)

    def get_stage(self, storage, time):
        if self.time_stages.length():
            stage = nm.interpolate_from_table(time, self.time_stages.list, 0, 1)
        else:
            stage = 0.0
        return stage
