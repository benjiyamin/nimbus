import copy

from nimbus.network.nodes.reservoir import Reservoir
from nimbus.network.links.pipe import Pipe
from nimbus.network.links.weir import Weir
from nimbus.reports import Report


class Network:

    def __init__(self, name=None):
        """Create a catchment. This is where nodes and links are organized for simulation."""
        self.name = name
        self.nodes = []
        self.links = []

    def create_reservoir(self, *args, **kwargs):
        """Create a reservoir, add it to the node list, and return the object."""
        new_reservoir = Reservoir(*args, **kwargs)
        self.nodes.append(new_reservoir)
        return new_reservoir

    def create_pipe(self, *args, **kwargs):
        """Create a pipe, add it to the link list, and return the object."""
        new_pipe = Pipe(*args, **kwargs)
        self.links.append(new_pipe)
        return new_pipe

    def create_weir(self, *args, **kwargs):
        """Create a weir, add it to the link list, and return the object."""
        new_weir = Weir(*args, **kwargs)
        self.links.append(new_weir)
        return new_weir

    def delete_node(self, node):
        """Remove the specified node from the node list and delete it."""
        self.nodes.remove(node)
        del node
        return

    def copy_node(self, node):
        """Create a copy of the specified node, add it to the node list, and return the object."""
        copy_node = copy.copy(node)
        self.nodes.append(copy_node)
        return copy_node

    def delete_link(self, link):
        """Remove the specified link from the link list and delete it."""
        self.links.remove(link)
        del link
        return

    def copy_link(self, link):
        """Create a copy of the specified link, add it to the link list, and return the object."""
        copy_link = copy.copy(link)
        self.links.append(copy_link)
        return copy_link

    def report_basins(self, col_length=15):
        title = ' Basins '
        report = Report()
        report.add_title(title)
        for node in self.nodes:
            for basin in node:
                basin_inputs = basin.get_inputs()
                for string in basin_inputs:
                    report.add_string_line(string)
                report.add_blank_line()
        report.output()
        return