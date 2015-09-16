__author__ = 'MillerB'


class Node:

    def __init__(self):
        self.basins = []

    def add_basin(self, basin):
        self.basins.append(basin)
        return
