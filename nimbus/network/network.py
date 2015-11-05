
from nimbus.data import node, link
from nimbus.reports import report as rp


class Network:

    def __init__(self, name=None, intensity_curve=None):
        """Create a network. This is where nodes and links are organized for simulation."""
        self.name = name
        self.intensity_curve = intensity_curve
        self.nodes = node.NodeList()
        self.links = link.LinkList()

    def report_node_inputs(self):
        """Report all current inputs of all nodes in the network"""
        rp.report_object_list_inputs('Nodes', self.nodes.list)
        return
    
    def report_link_inputs(self):
        """Report all current inputs of all links in the network"""
        rp.report_object_list_inputs('Links', self.links.list)
        return

    def report_basin_inputs(self):
        """Report all current inputs of all basins in the network"""
        basin_list = []
        for node in self.nodes.list:
            for basin in node.basins:
                basin_list.append(basin)
        rp.report_object_list_inputs('Basins', basin_list)
        return
