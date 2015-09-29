
from .link import Link


class Channel(Link):

    def __init__(self, name=None, shape=None, mannings=None,
                 length=None, invert1=None, invert2=None, node1=None, node2=None):

        self.name = name
        self.shape = shape
        self.mannings = mannings
        self.length = length  # feet
        self.invert1 = invert1  # feet
        self.invert2 = invert2  # feet
        super(Channel, self).__init__(node1=node1, node2=node2)