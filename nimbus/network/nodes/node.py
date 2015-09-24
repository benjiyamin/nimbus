
import copy
from nimbus.hydrology import Basin
from nimbus.reports import show_object_list


class Node:

    def __init__(self, name=None, basins=None):
        self.name = name
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

    '''
    def copy_basin(self, index):
        """Create a copy of the basin at the specified index from the basin list and add it to the basin list"""
        basin = self.basins[index]
        copy_basin = copy.copy(basin)
        self.basins.append(copy_basin)
        return
    '''

    def get_stage(self, storage, time):
        stage = None
        return stage

    def show_basins(self):
        title = 'Basins'
        object_list = self.basins
        show_object_list(title, object_list)
        return
