
import math


class IntensityCurve:

    def __init__(self, name, zone, coefficients):
        self.name = name
        self.zone = zone
        self.coefficients = coefficients

    def get_intensity(self, time):
        intensity = sum(coef * math.log(time) ** i for i, coef in enumerate(self.coefficients))
        return intensity
