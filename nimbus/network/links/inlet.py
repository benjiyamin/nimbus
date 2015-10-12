
from .weir import Weir
from .pipe import Pipe
from nimbus.reports import InputReport
from nimbus.data.objectlist import ObjectList


class Inlet(Pipe):

    def __init__(self, name=None, shape=None, mannings=None,
                 length=None, invert1=None, invert2=None, node1=None, node2=None):
        super(Inlet, self).__init__(name, shape, mannings, length, invert1, invert2, node1, node2)
        self.weirs = ObjectList(Weir)
        self.report = InputReport(self)

    def get_flow(self, stage1, stage2):
        pipe_flow = super(Inlet, self).get_flow(stage1, stage2)
        weir_flow = sum([weir.get_flow(stage1, stage2) for weir in self.weirs.list])
        if weir_flow > 0.0 and pipe_flow > 0.0:
            flow = min(weir_flow, pipe_flow)
        elif weir_flow < 0.0 and pipe_flow < 0.0:
            flow = max(weir_flow, pipe_flow)
        else:
            flow = weir_flow + pipe_flow
        return flow
