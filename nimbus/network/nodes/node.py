from nimbus.network.nodes.basin import basin as bsn
from nimbus.reports import report as rp
from nimbus.data import object as ob


class Node:

    def __init__(self, name=None, start_stage=None):
        self.name = name
        self.start_stage = start_stage
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
