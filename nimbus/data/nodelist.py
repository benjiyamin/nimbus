
from nimbus.network.nodes import Node, Reservoir, Boundary
from .objectlist import ObjectList


class NodeList(ObjectList):

    def __init__(self, list_=None):
        super(NodeList, self).__init__(Node, list_, True)

    def create_node(self, *args, **kwargs):
        """Create a node and add it to the node list."""
        self.create(Node, *args, **kwargs)
        return

    def create_reservoir(self, *args, **kwargs):
        """Create a reservoir and add it to the node list."""
        self.create(Reservoir, *args, **kwargs)
        return

    def create_boundary(self, *args, **kwargs):
        """Create a boundary and add it to the node list."""
        self.create(Boundary, *args, **kwargs)
        return
