
from nimbus.network.nodes import Node, Reservoir, Boundary
from nimbus.network.links import Pipe, Weir, Inlet
from nimbus.reports import Report, show_objects_in_list
from nimbus.data import append_to_list_and_print, delete_from_list_and_print, copy_from_list_and_print
import copy


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
        show_objects_in_list('Nodes', self.nodes, True)
        return

    def show_links(self):
        show_objects_in_list('Links', self.links, True)
        return

    def report_node_inputs(self):
        self.report_object_list_inputs('Nodes', self.nodes)
        return
    
    def report_link_inputs(self):
        self.report_object_list_inputs('Links', self.links)
        return

    def report_basin_inputs(self):
        basin_list = []
        for node in self.nodes:
            for basin in node.basins:
                basin_list.append(basin)
        self.report_object_list_inputs('Basins', basin_list)
        return

    '''
    @staticmethod
    def show_objects_in_list(_list):
        report = Report()
        report.add_blank_line()
        report.add_to_columns(['Index', 'Name', 'Class'])
        report.add_break_line()
        report.output()
        show_object_list(None, _list, show_class=True)
        report.add_blank_line()
        return
    '''

    @staticmethod
    def report_object_list_inputs(title, object_list):
        report = Report()
        report.add_blank_line()
        report.add_title(title)
        report.output()
        for thing in object_list:
            thing.report_inputs(show_title=False)
            report.add_break_line()
            report.add_blank_line()
            report.output()
        return
