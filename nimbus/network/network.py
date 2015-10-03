
from nimbus.network.nodes import Node, Reservoir, Boundary
from nimbus.network.links import Link, Pipe, Weir, Inlet
from nimbus.reports.report import report_object_list_inputs
from nimbus.data.nimlist import NimList


class Network:

    def __init__(self, name=None):
        """Create a network. This is where nodes and links are organized for simulation."""
        self.name = name
        self.nodes = NodeList()
        self.links = LinkList()

    def report_node_inputs(self):
        """Report all current inputs of all nodes in the network"""
        report_object_list_inputs('Nodes', self.nodes.list)
        return
    
    def report_link_inputs(self):
        """Report all current inputs of all links in the network"""
        report_object_list_inputs('Links', self.links.list)
        return

    def report_basin_inputs(self):
        """Report all current inputs of all basins in the network"""
        basin_list = []
        for node in self.nodes.list:
            for basin in node.basins:
                basin_list.append(basin)
        report_object_list_inputs('Basins', basin_list)
        return


class NodeList(NimList):

    def __init__(self, list_=None):
        if not list_:
            list_ = []
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


class LinkList(NimList):

    def __init__(self, list_=None):
        if not list_:
            list_ = []
        super(LinkList, self).__init__(Link, list_, True)

    def create_pipe(self, *args, **kwargs):
        """Create a pipe and add it to the link list."""
        self.create(Pipe, *args, **kwargs)
        return

    def create_weir(self, *args, **kwargs):
        """Create a weir and add it to the link list."""
        self.create(Weir, *args, **kwargs)
        return

    def create_inlet(self, *args, **kwargs):
        """Create an inlet and add it to the link list."""
        self.create(Inlet, *args, **kwargs)
        return
