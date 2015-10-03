
from math import pow, sqrt

from .link import Link
from nimbus.reports import property_to_string, float_to_string, InputReport


class Weir(Link):

    def __init__(self, name=None, shape=None, orif_coef=None, weir_coef=None, invert=None, node1=None, node2=None):
        super(Weir, self).__init__(name, node1, node2, shape)
        self.orif_coef = orif_coef
        self.weir_coef = weir_coef
        self.invert = invert
        self.report = InputReport(self)

    def get_flow(self, stage1, stage2):
        """Return the flow of the weir given the stages on both sides of the link."""
        crown = self.invert + self.shape.rise / 12.0
        center = self.invert + self.shape.rise / 12.0 / 2.0
        if stage1 > stage2:                                                             # stage 1 higher
            if stage1 > crown:                                                          # orifice flow
                if stage2 < self.invert:                                                # free flow
                    eff_head = stage1 - center
                else:                                                                   # submerged flow
                    eff_head = stage1 - stage2
                area = self.shape.get_flow_area(self.shape.rise)
                flow = self.orif_coef * area * sqrt(2.0 * 32.2 * eff_head)
            elif stage1 > self.invert:                                                  # weir flow
                eff_head = stage1 - self.invert
                flow = self.weir_coef * self.shape.span / 12.0 * pow(eff_head, 1.5)
                if stage2 > self.invert:                                                # submerged flow
                    flow *= 1.0 - pow(pow(stage2 / stage1, 1.5), 0.385)
            else:
                flow = 0.0
        else:                                                                           # stage 2 higher
            if stage2 > crown:                                                          # orifice flow
                if stage1 < self.invert:                                                # free flow
                    eff_head = stage2 - center
                else:                                                                   # submerged flow
                    eff_head = stage2 - stage1
                area = self.shape.get_flow_area(self.shape.rise)
                flow = -self.orif_coef * area * sqrt(2.0 * 32.2 * eff_head)
            elif stage2 > self.invert:                                                  # weir flow
                eff_head = stage2 - self.invert
                flow = -self.weir_coef * self.shape.span / 12.0 * pow(eff_head, 1.5)
                if stage1 > self.invert:                                                # submerged flow
                    flow *= 1.0 - pow(pow(stage1 / stage2, 1.5), 0.385)
            else:
                flow = 0.0
        return flow

    def get_input_strings(self):
        if self.shape:
            shape_type = property_to_string(self.shape.__class__, '__name__')
            shape_span = float_to_string(self.shape.span, 3)
            shape_rise = float_to_string(self.shape.rise, 3)
        else:
            shape_type = 'Undefined'
            shape_span = 'Undefined'
            shape_rise = 'Undefined'
        inputs = ['Name: ' + property_to_string(self, 'name'),
                  'Shape Type: ' + shape_type,
                  'Span (in): ' + shape_span,
                  'Rise (in): ' + shape_rise,
                  'Orifice Coef.: ' + float_to_string(self.orif_coef, 3),
                  'Weir. Coef: ' + float_to_string(self.weir_coef, 3),
                  'Invert: ' + float_to_string(self.invert, 3)]
        return inputs
