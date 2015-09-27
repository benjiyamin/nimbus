
import copy
from nimbus.hydrology import Basin
from nimbus.reports import show_object_list, property_to_string, float_to_string


class Node:

    def __init__(self, name=None, start_stage=None, basins=None):
        self.name = name
        self.start_stage = start_stage
        if basins is None:
            self.basins = []
        else:
            self.basins = basins

    def create_basin(self, *args, **kwargs):
        """Create a basin and add it to the basin list."""
        new_basin = Basin(*args, **kwargs)
        self.basins.append(new_basin)
        return
    
    def delete_basin(self, index):
        """Remove the basin at the specified index from the basin list and delete it."""
        basin = self.basins[index]
        self.basins.remove(basin)
        del basin
        return

    def copy_basin(self, index):
        """Create a copy of the basin at the specified index from the basin list and add it to the basin list"""
        basin = self.basins[index]
        copy_basin = copy.deepcopy(basin)
        self.basins.append(copy_basin)
        return

    def get_stage(self, storage, time):
        stage = 0.0
        return stage

    def get_storage(self, elevation):
        storage = 0.0
        return storage

    def show_basins(self):
        show_object_list('Basins', self.basins)
        return

    def get_inputs(self):
        inputs = ['Name: ' + property_to_string(self, 'name'),
                  'Starting Stage (ft): ' + float_to_string(self.start_stage, 3)]
        return inputs
