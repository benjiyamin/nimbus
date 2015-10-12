
from nimbus.math import interpolate_from_table
from nimbus.data.couplelist import CoupleList
from nimbus.reports import property_to_string, InputReport


class RainfallDistribution:

    def __init__(self, name=None, rainfall_ratios=None):
        self.name = name
        self.rainfall_ratios = CoupleList('Time-Rainfall Ratios', ('Time', 'Rainfall'), rainfall_ratios)
        self.report = InputReport(self, self.rainfall_ratios)

    def get_input_strings(self):
        inputs = ['Name: ' + property_to_string(self, 'name')]
        return inputs

    def get_rainfall_couple(self, duration, rainfall, time):
        rainfall_ratio = interpolate_from_table(time / duration, self.rainfall_ratios.list, 0, 1)
        rainfall = rainfall_ratio * rainfall
        couple = time, rainfall
        return couple
