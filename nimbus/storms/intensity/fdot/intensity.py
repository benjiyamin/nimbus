
import math


class Intensity:

    def __init__(self, name, zone, matrix):
        self.name = name
        self.zone = zone
        self.matrix = matrix

    def get_intensity(self, time, row):
        a = self.matrix.get(row, 1)
        b = self.matrix.get(row, 2) * math.log(time)
        c = self.matrix.get(row, 3) * math.log(time) ** 2
        d = self.matrix.get(row, 4) * math.log(time) ** 3
        intensity = a + b + c + d
        return intensity
