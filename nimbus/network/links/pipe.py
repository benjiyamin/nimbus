import math

from . import link, weir
from nimbus.reports import report as rp
from nimbus.reports import input as inp
from nimbus.network.links.sections import circle as cir
from nimbus.network.links.sections import rectangle as rct


class Pipe(link.Link):

    def __init__(self, name=None, section=None, mannings=None,
                 length=None, invert1=None, invert2=None, node1=None, node2=None):
        super(Pipe, self).__init__(name, node1, node2, section)
        self.mannings = mannings
        self.length = length  # feet
        self.invert1 = invert1  # feet
        self.invert2 = invert2  # feet
        self.report = inp.InputReport(self)

    def get_wet_perimeter(self, depth):
        """Return the wet perimeter in LF at a given depth from the invert of the pipe."""
        wet_perimeter = self.section.get_wet_perimeter(depth)
        return wet_perimeter

    def get_hyd_radius(self, depth):
        """Return the hydraulic radius in LF at a given depth from the invert of the pipe."""
        wet_perimeter = self.get_wet_perimeter(depth)
        if wet_perimeter == 0.0:
            hyd_radius = 0.0
        else:
            flow_area = self.get_flow_area(depth)
            hyd_radius = flow_area / wet_perimeter
        return hyd_radius

    def get_depth(self, stage, invert):
        """Return the depth given a stage and invert."""
        if stage < invert:
            depth = 0.0
        elif stage > invert + self.section.rise / 12.0:
            depth = self.section.rise
        else:
            depth = (stage - invert) * 12.0
        return depth

    def get_flow(self, stage1, stage2=None):
        if not stage2:
            stage2 = stage1 - self.invert1 + self.invert2
        if stage1 > stage2:                                                             # stage 1 higher
            if self.invert1 > self.invert2:                                             # pipe declined
                crown1 = self.invert1 + self.section.rise / 12.0
                if stage1 > crown1:                                                     # full flow
                    depth = self.get_depth(stage1, self.invert1)
                    center2 = self.invert2 + self.section.rise / 12.0 / 2.0
                    hg2 = max(stage2, center2)
                    velocity = self.get_velocity(stage1, hg2, depth)
                else:                                                                   # partial flow
                    depth1 = self.get_depth(stage1, self.invert1)
                    depth2 = self.get_depth(stage2, self.invert2)
                    depth = max(depth1, depth2)
                    velocity = self.get_velocity(self.invert1, self.invert2, depth)
                area = self.get_flow_area(depth)
                flow = velocity * area
            else:                                                                       # pipe inclined
                weir_flow = weir.Weir(section=self.section, orif_coef=1.0,
                                      weir_coef=2.63, invert=self.invert2)
                flow = weir_flow.get_flow(stage1, stage2)
        elif stage2 > stage1:                                                           # stage 2 higher
            if self.invert2 > self.invert1:                                             # pipe declined
                crown2 = self.invert2 + self.section.rise / 12.0
                if stage2 > crown2:                                                     # full flow
                    depth = self.get_depth(stage2, self.invert2)
                    center1 = self.invert1 + self.section.rise / 12.0 / 2.0
                    hg1 = max(stage1, center1)
                    velocity = self.get_velocity(stage2, hg1, depth)
                else:                                                                   # partial flow
                    depth1 = self.get_depth(stage1, self.invert1)
                    depth2 = self.get_depth(stage2, self.invert2)
                    depth = max(depth1, depth2)
                    velocity = self.get_velocity(self.invert2, self.invert1, depth)
                area = self.get_flow_area(depth)
                flow = velocity * area
            else:                                                                       # pipe inclined
                weir_flow = weir.Weir(section=self.section, orif_coef=1.0,
                                      weir_coef=2.63, invert=self.invert1)
                flow = -weir_flow.get_flow(stage2, stage1)
        else:
            flow = 0.0
        return flow

    def get_velocity(self, upper_el, lower_el, depth):
        hyd_radius = self.get_hyd_radius(depth)
        if hyd_radius == 0.0:
            velocity = 0.0
        else:
            a = (upper_el - lower_el) * 2.0 * 32.2
            b = 2.0 * 32.2 / pow(1.486, 2.0) * pow(self.mannings, 2.0) * self.length / pow(hyd_radius, 4.0 / 3.0)
            velocity = math.sqrt(a / b)
        return velocity

    '''
    def report_inputs(self, show_title=True):
        report = Report()
        if show_title is True:
            title = 'Pipe'
            report.add_title(title)
        inputs = self.get_inputs()
        for string in inputs:
            report.add_string_line(string)
        report.output()
        return
    '''

    def get_input_strings(self):
        if self.section:
            shape_type = rp.property_to_string(self.section.__class__, '__name__')
            shape_span = rp.float_to_string(self.section.span, 3)
            shape_rise = rp.float_to_string(self.section.rise, 3)
        else:
            shape_type = shape_span = shape_rise = 'Undefined'
        inputs = ['Name: ' + rp.property_to_string(self, 'name'),
                  'Node 1: ' + rp.property_to_string(self.node1, 'name'),
                  'Node 2: ' + rp.property_to_string(self.node2, 'name'),
                  'Shape Type: ' + shape_type,
                  'Span (in): ' + shape_span,
                  'Rise (in): ' + shape_rise,
                  'Mannings: ' + rp.float_to_string(self.mannings, 3),
                  'Length (ft): ' + rp.float_to_string(self.length, 3),
                  'Invert 1 (ft): ' + rp.float_to_string(self.invert1, 3),
                  'Invert 2 (ft): ' + rp.float_to_string(self.invert2, 3)]
        return inputs

    def set_shape_as_rectangle(self, span, rise, horizontal=False):
        self.section = rct.Rectangle(span, rise, horizontal)
        return

    def set_shape_as_circle(self, diameter, horizontal=False):
        self.section = cir.Circle(diameter, horizontal)
        return

    '''
    def get_average_depth(self, stage1, stage2):
        """Return the average depth given the stages on both sides of the link."""
        depth1 = self.get_depth(stage1, self.invert1)
        depth2 = self.get_depth(stage2, self.invert2)
        average_depth = (depth1 + depth2) / 2.0
        return average_depth
    '''

    '''
    def get_physical_slope(self):
        """Return the physical slope of the pipe based on length and inverts."""
        physical_slope = (self.invert1 - self.invert2) / self.length
        return physical_slope
    '''
    '''
    def get_friction_loss(self):
        """Return the friction loss of the pipe based on length and inverts."""
        friction_loss = self.get_physical_slope() * self.length
        return friction_loss
    '''
    '''
    def get_hgls(self, stage1, stage2):
        """Return the hgls given the stages on either side of the link."""
        friction_loss = self.get_friction_loss()
        if stage1 > stage2:                                                     # stage 1 higher
            if self.invert1 > self.invert2:                                     # pipe declined
                crown1 = self.invert1 + self.shape.rise / 12.0
                if stage1 > crown1:                                             # full flow
                    crown2 = self.invert2 + self.shape.rise / 12.0
                    hgl2 = max(stage2, crown2)
                else:                                                           # partial flow
                    depth = self.get_depth(stage1, self.invert1)
                    hgl2 = max(stage2, depth + self.invert2)
                hgl1 = max(stage1, hgl2 + friction_loss)
            else:                                                               # pipe inclined
                crown2 = self.invert2 + self.shape.rise / 12.0
                if stage1 > crown2:                                             # full flow
                    hgl2 = max(stage2, crown2)
                else:                                                           # partial flow
                    hgl2 = stage2
                hgl1 = stage1
        else:                                                                   # stage 2 higher
            if self.invert2 > self.invert1:                                     # pipe inclined
                crown2 = self.invert2 + self.shape.rise / 12.0
                if stage2 > crown2:                                             # full flow
                    crown1 = self.invert1 + self.shape.rise / 12.0
                    hgl1 = max(stage1, crown1)
                else:                                                           # partial flow
                    depth = self.get_depth(stage2, self.invert2)
                    hgl1 = max(stage1, depth + self.invert1)
                hgl2 = max(stage2, hgl1 - friction_loss)
            else:                                                               # pipe declined
                crown1 = self.invert1 + self.shape.rise / 12.0
                if stage2 > crown1:                                             # full flow
                    hgl1 = max(stage1, crown1)
                else:                                                           # partial flow
                    hgl1 = stage1
                hgl2 = stage2
        return hgl1, hgl2
    '''

    '''
    def get_gradient(self, stage1, stage2):
        """Return the hydraulic gradient given the stages on both sides of the link."""
        hgls = self.get_hgls(stage1, stage2)
        gradient = (hgls[0] - hgls[1]) / self.length
        return gradient
    '''

    '''
    def get_flow(self, stage1, stage2):
        """Return the flow of the pipe given the stages on both sides of the link."""
        hgls = self.get_hgls(stage1, stage2)
        depth = self.get_average_depth(hgls[0], hgls[1])
        gradient = self.get_gradient(stage1, stage2)
        flow_area = self.get_flow_area(depth)
        hyd_radius = self.get_hyd_radius(depth)
        head_loss = gradient * self.length
        a = head_loss * pow(flow_area, 2.0) * pow(hyd_radius, 4.0 / 3.0)
        b = 0.453
        c = pow(self.mannings, 2.0)
        d = self.length
        flow = sqrt(a / b / c / d)
        return flow
    '''
