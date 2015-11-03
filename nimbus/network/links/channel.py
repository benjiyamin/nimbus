
from .link import Link
from nimbus.reports import input as inp
from nimbus.math import goal_seek


class Channel(Link):

    def __init__(self, name=None, section=None, mannings=None, intensity_curve=None,
                 length=None, invert1=None, invert2=None, node1=None, node2=None):
        super(Channel, self).__init__(name, node1, node2, section)
        self.mannings = mannings
        self.intensity_curve = intensity_curve
        self.length = length  # feet
        self.invert1 = invert1  # feet
        self.invert2 = invert2  # feet
        self.report = inp.InputReport(self)

    def get_depth(self, stage, invert):
        """Return the depth given a stage and invert."""
        if stage < invert:
            depth = 0.0
        else:
            depth = (stage - invert) * 12.0
        return depth

    def get_depth_from_intensity(self, intensity):
        flow = self.get_flow_from_intensity(intensity)
        return flow

    def get_flow_from_intensity(self, intensity):
        runoff = self.node1.get_runoff_area()
        flow = runoff * intensity * 43560.0 / 12.0 / 60.0 / 60.0
        return flow

    def get_flow_from_depth(self, depth):
        hyd_radius = self.section.get_hyd_radius(depth)
        velocity = self.get_velocity(depth)
        flow = hyd_radius * velocity
        return flow

    def get_slope(self):
        slope = (self.invert1 - self.invert2) / self.length
        return slope

    def get_flow_accuracy(self, depth):
        flow_depth = self.get_flow_from_depth(depth)
        velocity = self.get_velocity(depth)
        tc = self.node1.get_tc()
        travel_time = tc + self.length / (velocity * 60.0)
        intensity = self.intensity_curve.get_intensity(travel_time)
        flow_intensity = self.get_flow_from_intensity(intensity)
        accuracy = flow_depth / flow_intensity
        return accuracy

    def get_velocity(self, depth):
        hyd_radius = self.section.get_hyd_radius(depth)
        slope = self.get_slope()
        a = pow(hyd_radius, 2.0 / 3.0)
        b = pow(slope, 0.5)
        velocity = 1.49 * a * b / self.mannings
        return velocity

    def solve_depth(self):
        depth = goal_seek(self.get_flow_accuracy, 0.0, 100.0, 1.0, 100, 0.00001)
        return depth
