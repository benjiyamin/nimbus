

class Node:

    def __init__(self, basins=None):
        if basins is None:
            self.basins = []
        else:
            self.basins = basins

    def add_basin(self, basin):
        self.basins.append(basin)
        return

    def get_stage(self, storage, time):
        stage = None
        return stage
