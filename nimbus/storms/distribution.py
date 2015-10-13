
from nimbus import math as nm
from nimbus.data import couple as cpl
from nimbus.reports import report as rp
from nimbus.reports import input as inp


class RainfallDistribution:

    def __init__(self, name=None, rainfall_ratios=None):
        self.name = name
        self.rainfall_ratios = cpl.CoupleList('Time-Rainfall Ratios', ('Time', 'Rainfall'), rainfall_ratios)
        self.report = inp.InputReport(self, self.rainfall_ratios)

    def get_input_strings(self):
        inputs = ['Name: ' + rp.property_to_string(self, 'name')]
        return inputs

    def get_rainfall_couple(self, duration, rainfall, time):
        rainfall_ratio = nm.interpolate_from_table(time / duration, self.rainfall_ratios.list, 0, 1)
        rainfall = rainfall_ratio * rainfall
        couple = time, rainfall
        return couple
