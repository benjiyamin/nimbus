
from math import acos


def get_alpha(height, diameter):
    """Return the alpha value utilized for circular hydraulics."""
    alpha = acos(1.0 - height / (diameter / 2.0))
    return alpha


def get_slope_area(slope, height):
    area = slope * pow(height, 2.0) / 2.0
    return area


def get_slope_perimeter(slope, height):
    perimeter = pow(pow(height * slope, 2.0) + pow(height, 2.0), 0.5)
    return perimeter
