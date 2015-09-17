
import os
import csv
from nimbus.hydrology.uh import UnitHydrograph

abs_path = os.path.abspath(__file__)
dir_name = os.path.dirname(abs_path)
os.chdir(dir_name)


def couples_from_csv(filename):
    open_file = open(filename, "rt")
    reader = csv.reader(open_file, delimiter=',')
    list = []
    for row in reader:
        i = float(row[0])
        j = float(row[1])
        list.append((i, j))
    return list


uh256 = UnitHydrograph(256.0, couples_from_csv("csv/uh256.csv"), "UH256")
uh323 = UnitHydrograph(323.0, couples_from_csv("csv/uh323.csv"), "UH323")
uh484 = UnitHydrograph(484.0, couples_from_csv("csv/uh484.csv"), "UH484")
