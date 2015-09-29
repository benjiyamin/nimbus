
from nimbus.math import interpolate_from_table


class RainfallDistribution:

    def __init__(self, name=None, couples=None):
        self.name = name
        self.couples = couples

    def get_rainfall_couple(self, duration, rainfall, time):
        rainfall_ratio = interpolate_from_table(time / duration, self.couples, 0, 1)
        rainfall = rainfall_ratio * rainfall
        couple = time, rainfall
        return couple
