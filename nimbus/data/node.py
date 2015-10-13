
from . import object as ob
from nimbus.network import nodes


class NodeList(ob.ObjectList):

    def __init__(self, list_=None):
        super(NodeList, self).__init__(nodes.Node, list_, True)

    def create_node(self, *args, **kwargs):
        """Create a node and add it to the node list."""
        self.create(nodes.Node, *args, **kwargs)
        return

    def create_reservoir(self, *args, **kwargs):
        """Create a reservoir and add it to the node list."""
        self.create(nodes.Reservoir, *args, **kwargs)
        return

    def create_boundary(self, *args, **kwargs):
        """Create a boundary and add it to the node list."""
        self.create(nodes.Boundary, *args, **kwargs)
        return
