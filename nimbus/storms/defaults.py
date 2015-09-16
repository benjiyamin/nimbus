__author__ = 'MillerB'

import os
import csv
from nimbus.storms.distribution import RainfallDistribution


abs_path = os.path.abspath(__file__)
dir_name = os.path.dirname(abs_path)
os.chdir(dir_name)


def tuples_from_csv(filename):
    open_file = open(filename, "rt")
    reader = csv.reader(open_file, delimiter=',')
    list = []
    for row in reader:
        i = float(row[0])
        j = float(row[1])
        list.append((i, j))
    return list


delaney = RainfallDistribution("DELANEY", tuples_from_csv("csv/delaney.csv"))
fdot1 = RainfallDistribution("FDOT-1", tuples_from_csv("csv/fdot1.csv"))
fdot2 = RainfallDistribution("FDOT-2", tuples_from_csv("csv/fdot2.csv"))
fdot4 = RainfallDistribution("FDOT-4", tuples_from_csv("csv/fdot4.csv"))
fdot8 = RainfallDistribution("FDOT-8", tuples_from_csv("csv/fdot8.csv"))
fdot24 = RainfallDistribution("FDOT-24", tuples_from_csv("csv/fdot24.csv"))
fdot72 = RainfallDistribution("FDOT-72", tuples_from_csv("csv/fdot72.csv"))
fdot168 = RainfallDistribution("FDOT-168", tuples_from_csv("csv/fdot168.csv"))
fdot240 = RainfallDistribution("FDOT-240", tuples_from_csv("csv/fdot240.csv"))
flmod = RainfallDistribution("FLMOD", tuples_from_csv("csv/flmod.csv"))
nrcsi24 = RainfallDistribution("SCSI-24", tuples_from_csv("csv/nrcsi24.csv"))
nrcsi48 = RainfallDistribution("SCSI-48", tuples_from_csv("csv/nrcsi48.csv"))
ncrsa24 = RainfallDistribution("SCSIA-24", tuples_from_csv("csv/nrcsia24.csv"))
nrcsii24 = RainfallDistribution("SCSII-24", tuples_from_csv("csv/nrcsii24.csv"))
nrcsii48 = RainfallDistribution("SCSII-48", tuples_from_csv("csv/nrcsii48.csv"))
nrcsiii = RainfallDistribution("SCSIII", tuples_from_csv("csv/nrcsiii.csv"))
orange = RainfallDistribution("ORANGE", tuples_from_csv("csv/orange.csv"))
sfwmd72 = RainfallDistribution("SFWMD72", tuples_from_csv("csv/sfwmd72.csv"))
sjrwmd96 = RainfallDistribution("SJRWMD96", tuples_from_csv("csv/sjrwmd96.csv"))
