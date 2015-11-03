
from .link import Link
from nimbus.network.links.sections.triangle import Triangle


class Gutter(Link):

    def __init__(self, name=None, long_slope=None, xs_slope=None, mannings=None, node1=None, node2=None):
        super(Gutter, self).__init__(name, node1, node2, Triangle(100.0, xs_slope, horizontal=False))
        self.long_slope = long_slope
        self.mannings = mannings

    def get_depth_from_intensity(self, intensity):
        spread = self.get_spread(intensity)
        depth = spread * self.section.xs_slope
        return depth

    def get_spread(self, intensity):
        flow = self.get_flow_from_intensity(intensity)
        a = flow * self.mannings
        b = pow(self.long_slope, 0.5)
        c = pow(self.section.xs_slope, 5.0 / 3.0)
        spread = pow(a / (0.56 * b * c), 3.0 / 8.0)
        return spread

    def get_flow_from_intensity(self, intensity):
        runoff = self.node1.get_runoff_area()
        flow = runoff * intensity * 43560.0 / 12.0 / 60.0 / 60.0
        return flow
