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