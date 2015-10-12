
from nimbus.hydrology.basin import Basin
from nimbus.reports.report import property_to_string, float_to_string
from nimbus.data.objectlist import ObjectList


class Node:

    def __init__(self, name=None, start_stage=None):
        self.name = name
        self.start_stage = start_stage
        self.basins = ObjectList(Basin)

    def get_input_strings(self):
        inputs = ['Name: ' + property_to_string(self, 'name'),
                  'Starting Stage (ft): ' + float_to_string(self.start_stage, 3)]
        return inputs

    def get_stage(self, storage, time):
        stage = 0.0
        return stage

    def get_storage(self, elevation):
        storage = 0.0
        return storage
