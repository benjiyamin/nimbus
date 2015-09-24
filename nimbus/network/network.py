
import copy
from nimbus.network.nodes import Node, Reservoir, Boundary
from nimbus.network.links import Pipe, Weir
from nimbus.reports import Report, show_object_list


class Network:

    def __init__(self, name=None):
        """Create a catchment. This is where nodes and links are organized for simulation."""
        self.name = name
        self.nodes = []
        self.links = []
    
    def create_node(self, *args, **kwargs):
        """Create a node and add it to the node list."""
        new_node = Node(*args, **kwargs)
        self.nodes.append(new_node)
        return

    def create_reservoir(self, *args, **kwargs):
        """Create a reservoir and add it to the node list."""
        new_reservoir = Reservoir(*args, **kwargs)
        self.nodes.append(new_reservoir)
        return

    def create_boundary(self, *args, **kwargs):
        """Create a boundary and add it to the node list."""
        new_boundary = Boundary(*args, **kwargs)
        self.nodes.append(new_boundary)
        return

    def create_pipe(self, *args, **kwargs):
        """Create a pipe and add it to the link list."""
        new_pipe = Pipe(*args, **kwargs)
        self.links.append(new_pipe)
        return

    def create_weir(self, *args, **kwargs):
        """Create a weir and add it to the link list."""
        new_weir = Weir(*args, **kwargs)
        self.links.append(new_weir)
        return

    def delete_node(self, index):
        """Remove the node at the specified index from the node list and delete it."""
        node = self.nodes[index]
        self.nodes.remove(node)
        del node
        return

    '''
    def copy_node(self, index):
        """Create a copy of the node at the specified index from the node list and add it to the node list"""
        node = self.nodes[index]
        copy_node = copy.copy(node)
        self.nodes.append(copy_node)
        return
    '''

    def delete_link(self, index):
        """Remove the link at the specified index from the link list and delete it."""
        link = self.links[index]
        self.links.remove(link)
        del link
        return

    '''
    def copy_link(self, index):
        """Create a copy of the link at the specified index from the link list and add it to the link list"""
        link = self.links[index]
        copy_link = copy.copy(link)
        self.links.append(copy_link)
        return
    '''

    def show_nodes(self):
        title = 'Nodes'
        object_list = self.nodes
        show_object_list(title, object_list, show_class=True)
        return

    def show_links(self):
        title = 'Links'
        object_list = self.links
        show_object_list(title, object_list, show_class=True)
        return

    def report_node_inputs(self):
        title = 'Nodes'
        report = Report()
        report.add_title(title)
        report.output()
        for node in self.nodes:
            report = Report()
            node.report_inputs(title=False)
            report.add_break_line()
            report.output()
        return

    def report_basin_inputs(self):
        title = 'Basins'
        report = Report()
        report.add_title(title)
        report.output()
        for node in self.nodes:
            for basin in node.basins:
                report = Report()
                basin.report_inputs(title=False)
                report.add_break_line()
                report.output()
        return
