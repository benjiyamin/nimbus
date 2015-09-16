__author__ = 'MillerB'

from nimbus.math import interpolate_from_table
from math import ceil


class Simulation:

    def __init__(self, name=None, duration=None, interval=None,
                 rainfall=None, distribution=None):
        self.name = name
        self.duration = duration
        self.interval = interval
        self.rainfall = rainfall
        self.distribution = distribution
        self.networks = []

    def get_tabulated_accumulated_rainfall(self):
        last_time = self.duration
        time_steps = ceil(last_time / self.interval)
        distribution_couples = self.distribution.couples
        tabulation = []
        for time_step in range(time_steps):
            time = time_step * self.interval
            rainfall_ratio = interpolate_from_table(time / self.duration, distribution_couples, 0, 1)
            rainfall = rainfall_ratio * self.rainfall
            new_couple = (time, rainfall)
            tabulation.append(new_couple)
        tabulation.append((tabulation[len(tabulation) - 1][0] + self.interval, self.rainfall))
        return tabulation

    def add_network(self, network):
        self.networks.append(network)
        return

    def remove_network(self, network):
        """Remove the specified network from the network list."""
        self.networks.remove(network)
        return
