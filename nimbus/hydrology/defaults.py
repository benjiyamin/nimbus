
import os
import csv

from nimbus.hydrology.uh import UnitHydrograph

abs_path = os.path.abspath(__file__)
dir_name = os.path.dirname(abs_path)


def couples_from_csv(filename):
    open_file = open(filename, "rt")
    reader = csv.reader(open_file, delimiter=',')
    tuple_list = []
    for row in reader:
        i = float(row[0])
        j = float(row[1])
        tuple_list.append((i, j))
    open_file.close()
    return tuple_list


uh256 = UnitHydrograph(256.0, couples_from_csv(dir_name + "/csv/uh256.csv"), "UH256")
uh323 = UnitHydrograph(323.0, couples_from_csv(dir_name + "/csv/uh323.csv"), "UH323")
uh484 = UnitHydrograph(484.0, couples_from_csv(dir_name + "/csv/uh484.csv"), "UH484")
