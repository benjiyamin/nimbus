
from .link import Link
from math import pow, sqrt


class Weir(Link):

    def __init__(self, name=None, shape=None, orif_coef=None, weir_coef=None, invert=None, node1=None, node2=None):
        self.name = name
        self.shape = shape
        self.orif_coef = orif_coef
        self.weir_coef = weir_coef
        self.invert = invert
        super(Weir, self).__init__(node1, node2)

    def get_flow_area(self, depth):
        """Return the flow area in SF at a given depth from the invert of the pipe."""
        flow_area = self.shape.get_flow_area(depth)
        return flow_area

    def get_flow(self, stage1, stage2):
        """Return the flow of the weir given the stages on both sides of the link."""
        crown = self.invert + self.shape.rise / 12.0
        center = self.invert + self.shape.rise / 12.0 / 2.0
        if stage1 > stage2:                                                     # stage 1 higher
            if stage1 > crown:                                                  # orifice flow
                if stage2 < self.invert:                                        # free flow
                    eff_head = stage1 - center
                else:                                                           # submerged flow
                    eff_head = stage1 - stage2
                area = self.shape.get_flow_area(self.shape.rise)
                flow = self.orif_coef * area * sqrt(2.0 * 32.2 * eff_head)
            else:                                                               # weir flow
                eff_head = stage1 - self.invert
                flow = self.weir_coef * self.shape.span * pow(eff_head, 1.5)
                if stage2 > self.invert:                                        # submerged flow
                    flow *= 1.0 - pow(pow(stage2 / stage1, 1.5), 0.385)
        else:                                                                   # stage 2 higher
            if stage2 > crown:                                                  # orifice flow
                if stage1 < self.invert:                                        # free flow
                    eff_head = stage2 - center
                else:                                                           # submerged flow
                    eff_head = stage2 - stage1
                area = self.shape.get_flow_area(self.shape.rise)
                flow = -self.orif_coef * area * sqrt(2.0 * 32.2 * eff_head)
            else:                                                               # weir flow
                eff_head = stage2 - self.invert
                flow = -self.weir_coef * self.shape.span * pow(eff_head, 1.5)
                if stage1 > self.invert:                                        # submerged flow
                    flow *= 1.0 - pow(pow(stage1 / stage2, 1.5), 0.385)
        return flow
