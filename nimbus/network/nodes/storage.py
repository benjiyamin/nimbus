
import math
import time as ti

from . import node
from nimbus.math import math as nm
from nimbus.reports import input as inp
from nimbus.data import couple as cpl


class Storage(node.Node):

    def __init__(self, name=None, start_stage=None, stage_volumes=None):
        super(Storage, self).__init__(name, start_stage)
        self.stage_volumes = cpl.CoupleList('Stage-Volumes',
                                            ('Stage (ft)', 'Volume (ac-ft)'),
                                            stage_volumes)
        self.report = inp.InputReport(self, self.stage_volumes)

    def get_storage(self, elevation):
        if self.stage_volumes.length():
            storage = nm.interpolate_from_table(elevation, self.stage_volumes.all(), 0, 1)
        else:
            storage = 0.0
        return storage

    def get_stage(self, storage, time=None):
        if self.stage_volumes.length():
            stage = nm.interpolate_from_table(storage, self.stage_volumes.all(), 1, 0)
        else:
            stage = 0.0
        return stage
