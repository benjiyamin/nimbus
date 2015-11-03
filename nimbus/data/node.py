
from . import object as ob
from nimbus.network.nodes.reservoir import Reservoir
from nimbus.network.nodes.node import Node
from nimbus.network.nodes.boundary import Boundary


class NodeList(ob.ObjectList):

    def __init__(self, network=None, list_=None):
        super(NodeList, self).__init__(Node, list_, True)
        self.network = network

    def create_node(self, *args, **kwargs):
        """Create a node and add it to the node list."""
        self.create(Node, *args, **kwargs)
        self.set_network_of_new()
        return

    def create_reservoir(self, *args, **kwargs):
        """Create a reservoir and add it to the node list."""
        self.create(Reservoir, *args, **kwargs)
        return

    def create_boundary(self, *args, **kwargs):
        """Create a boundary and add it to the node list."""
        self.create(Boundary, *args, **kwargs)
        return

    def set_network_of_new(self):
        new_node = self.list[-1]
        new_node.network = self.network
        return
