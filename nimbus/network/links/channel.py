
from . import link
from nimbus.reports import input as inp


class Channel(link.Link):

    def __init__(self, name=None, shape=None, mannings=None,
                 length=None, invert1=None, invert2=None, node1=None, node2=None):
        super(Channel, self).__init__(name, node1, node2, shape)
        self.mannings = mannings
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
