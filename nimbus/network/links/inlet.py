
from . import weir, pipe
from nimbus.reports import input as inp
from nimbus.data import object as ob


class Inlet(pipe.Pipe):

    def __init__(self, name=None, shape=None, mannings=None,
                 length=None, invert1=None, invert2=None, node1=None, node2=None):
        super(Inlet, self).__init__(name, shape, mannings, length, invert1, invert2, node1, node2)
        self.weirs = ob.ObjectList(weir.Weir)
        self.report = inp.InputReport(self)

    def get_flow(self, stage1, stage2):
        pipe_flow = super(Inlet, self).get_flow(stage1, stage2)
        weir_flow = sum([w.get_flow(stage1, stage2) for w in self.weirs.list])
        if weir_flow > 0.0 and pipe_flow > 0.0:
            flow = min(weir_flow, pipe_flow)
        elif weir_flow < 0.0 and pipe_flow < 0.0:
            flow = max(weir_flow, pipe_flow)
        else:
            flow = weir_flow + pipe_flow
        return flow
