
from nimbus.network.nodes import Node, Reservoir, Boundary
from nimbus.network.links import Pipe, Weir, Inlet
from nimbus.reports import show_objects_in_list, report_object_list_inputs
from nimbus.data import append_to_list_and_print, delete_from_list_and_print, copy_from_list_and_print


class Network:

    def __init__(self, name=None):
        """Create a network. This is where nodes and links are organized for simulation."""
        self.name = name
        self.nodes = []
        self.links = []
    
    def create_node(self, *args, **kwargs):
        """Create a node and add it to the node list."""
        new_node = Node(*args, **kwargs)
        append_to_list_and_print(new_node, self.nodes)
        return

    def create_reservoir(self, *args, **kwargs):
        """Create a reservoir and add it to the node list."""
        new_reservoir = Reservoir(*args, **kwargs)
        append_to_list_and_print(new_reservoir, self.nodes)
        return

    def create_boundary(self, *args, **kwargs):
        """Create a boundary and add it to the node list."""
        new_boundary = Boundary(*args, **kwargs)
        append_to_list_and_print(new_boundary, self.nodes)
        return

    def create_pipe(self, *args, **kwargs):
        """Create a pipe and add it to the link list."""
        new_pipe = Pipe(*args, **kwargs)
        append_to_list_and_print(new_pipe, self.nodes)
        return

    def create_weir(self, *args, **kwargs):
        """Create a weir and add it to the link list."""
        new_weir = Weir(*args, **kwargs)
        append_to_list_and_print(new_weir, self.nodes)
        return
    
    def create_inlet(self, *args, **kwargs):
        """Create an inlet and add it to the link list."""
        new_inlet = Inlet(*args, **kwargs)
        append_to_list_and_print(new_inlet, self.nodes)
        return

    def delete_node(self, index):
        """Remove the node at the specified index from the node list and delete it."""
        delete_from_list_and_print(index, self.nodes)
        return

    def copy_node(self, index):
        """Create a copy of the node at the specified index from the node list and add it to the list"""
        copy_from_list_and_print(index, self.nodes)
        return

    def delete_link(self, index):
        """Remove the link at the specified index from the link list and delete it."""
        delete_from_list_and_print(index, self.links)
        return

    def copy_link(self, index):
        """Create a copy of the link at the specified index from the link list and add it to the list"""
        copy_from_list_and_print(index, self.links)
        return

    def show_nodes(self):
        """Display all nodes stored in the network's node list."""
        show_objects_in_list('Nodes', self.nodes, True)
        return

    def show_links(self):
        """Display all links stored in the network's link list."""
        show_objects_in_list('Links', self.links, True)
        return

    def report_node_inputs(self):
        """Report all current inputs of all nodes in the network"""
        report_object_list_inputs('Nodes', self.nodes)
        return
    
    def report_link_inputs(self):
        """Report all current inputs of all links in the network"""
        report_object_list_inputs('Links', self.links)
        return

    def report_basin_inputs(self):
        """Report all current inputs of all basins in the network"""
        basin_list = []
        for node in self.nodes:
            for basin in node.basins:
                basin_list.append(basin)
        report_object_list_inputs('Basins', basin_list)
        return

