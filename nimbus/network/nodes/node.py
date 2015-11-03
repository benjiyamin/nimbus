from nimbus.network.nodes.basin import basin as bsn
from nimbus.reports import report as rp
from nimbus.data import object as ob


class Node:

    def __init__(self, name=None, start_stage=None, network=None):
        self.name = name
        self.start_stage = start_stage
        self.network = network
        self.basins = ob.ObjectList(bsn.Basin)

    def get_input_strings(self):
        inputs = ['Name: ' + rp.property_to_string(self, 'name'),
                  'Starting Stage (ft): ' + rp.float_to_string(self.start_stage, 3)]
        return inputs

    def get_stage(self, storage, time):
        stage = 0.0
        return stage

    def get_storage(self, elevation):
        storage = 0.0
        return storage

    def get_area(self, elevation):
        area = 0.0
        return area

    def get_upstream_nodes(self):
        available_nodes = self.network.nodes.all()
        available_links = self.network.links.all()
        upstream_nodes = [self]
        trigger = True
        while trigger:
            trigger = False
            for to_node in upstream_nodes:
                for from_node in available_nodes:
                    from_node_link = [link for link in available_links if link.node1 is from_node][0]
                    if from_node_link.node2 is to_node and from_node not in upstream_nodes:
                        upstream_nodes.append(from_node)
                        trigger = True
        upstream_nodes.remove(self)
        return upstream_nodes

    def get_upstream_area(self):
        upstream_nodes = self.get_upstream_nodes()
        area = 0.0
        for node in upstream_nodes:
            basins = node.basins.all()
            for basin in basins:
                shapes = basin.shapes.all()
                area = sum(shape.area for shape in shapes)
        return area

    def get_upstream_imp_area(self):
        upstream_nodes = self.get_upstream_nodes()
        imp_area = 0.0
        for node in upstream_nodes:
            basins = node.basins.all()
            for basin in basins:
                shapes = basin.shapes.all()
                imp_area = sum(shape.area * shape.imp for shape in shapes)
        return imp_area
    
    def get_imp_area(self):
        basins = self.basins.all()
        imp_area = 0.0
        for basin in basins:
            shapes = basin.shapes.all()
            imp_area = sum(shape.area * shape.imp for shape in shapes)
        return imp_area
    
    def get_total_imp_area(self):
        upstream_imp_area = self.get_upstream_imp_area()
        imp_area = self.get_imp_area()
        total_imp_area = upstream_imp_area + imp_area
        return total_imp_area

    def get_upstream_runoff_area(self):
        upstream_nodes = self.get_upstream_nodes()
        runoff_area = sum(node.get_runoff_area() for node in upstream_nodes)
        return runoff_area
    
    def get_runoff_area(self):
        basins = self.basins.all()
        runoff_area = 0.0
        for basin in basins:
            shapes = basin.shapes.all()
            runoff_area = sum(shape.area * shape.c for shape in shapes)
        return runoff_area
    
    def get_total_runoff_area(self):
        upstream_runoff_area = self.get_upstream_runoff_area()
        runoff_area = self.get_runoff_area()
        total_runoff_area = upstream_runoff_area + runoff_area
        return total_runoff_area

    def get_tc(self):
        basins = self.basins.all()
        tc = max(basin.tc for basin in basins)
        return tc

    def get_travel_time(self):
        pass
