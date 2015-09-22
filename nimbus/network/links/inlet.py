
from nimbus.network.links.weir import Weir
from nimbus.network.links.link import Link


class Inlet(Link):

    def __init__(self, name=None, shape=None, pipe=None, node1=None, node2=None):
        self.name = name
        self.shape = shape
        self.pipe = pipe
        self.weirs = []
        super(Inlet, self).__init__(node1, node2)

    def create_weir(self, *args, **kwargs):
        """Create a weir, add it to the weir list, and return the object."""
        new_weir = Weir(*args, **kwargs)
        self.weirs.append(new_weir)
        return new_weir

    def get_flow(self, stage1, stage2):
        pipe_flow = self.pipe.get_flow(stage1, stage2)
        inlet_weirs = [weir.get_flow(stage1, stage2) for weir in self.weirs]
        weir_flow = sum(inlet_weirs)
        if weir_flow > 0.0 and pipe_flow > 0.0:
            flow = min(weir_flow, pipe_flow)
        elif weir_flow < 0.0 and pipe_flow < 0.0:
            flow = max(weir_flow, pipe_flow)
        else:
            flow = weir_flow + pipe_flow
        return flow