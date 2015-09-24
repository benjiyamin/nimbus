
import os
import csv
from nimbus.storms.distribution import RainfallDistribution


abs_path = os.path.abspath(__file__)
dir_name = os.path.dirname(abs_path)


def tuples_from_csv(filename):
    open_file = open(filename, "rt")
    reader = csv.reader(open_file, delimiter=',')
    tuple_list = []
    for row in reader:
        i = float(row[0])
        j = float(row[1])
        tuple_list.append((i, j))
    open_file.close()
    return tuple_list


delaney = RainfallDistribution("DELANEY", tuples_from_csv(dir_name + "/csv/delaney.csv"))
fdot1 = RainfallDistribution("FDOT-1", tuples_from_csv(dir_name + "/csv/fdot1.csv"))
fdot2 = RainfallDistribution("FDOT-2", tuples_from_csv(dir_name + "/csv/fdot2.csv"))
fdot4 = RainfallDistribution("FDOT-4", tuples_from_csv(dir_name + "/csv/fdot4.csv"))
fdot8 = RainfallDistribution("FDOT-8", tuples_from_csv(dir_name + "/csv/fdot8.csv"))
fdot24 = RainfallDistribution("FDOT-24", tuples_from_csv(dir_name + "/csv/fdot24.csv"))
fdot72 = RainfallDistribution("FDOT-72", tuples_from_csv(dir_name + "/csv/fdot72.csv"))
fdot168 = RainfallDistribution("FDOT-168", tuples_from_csv(dir_name + "/csv/fdot168.csv"))
fdot240 = RainfallDistribution("FDOT-240", tuples_from_csv(dir_name + "/csv/fdot240.csv"))
flmod = RainfallDistribution("FLMOD", tuples_from_csv(dir_name + "/csv/flmod.csv"))
nrcsi24 = RainfallDistribution("SCSI-24", tuples_from_csv(dir_name + "/csv/nrcsi24.csv"))
nrcsi48 = RainfallDistribution("SCSI-48", tuples_from_csv(dir_name + "/csv/nrcsi48.csv"))
ncrsa24 = RainfallDistribution("SCSIA-24", tuples_from_csv(dir_name + "/csv/nrcsia24.csv"))
nrcsii24 = RainfallDistribution("SCSII-24", tuples_from_csv(dir_name + "/csv/nrcsii24.csv"))
nrcsii48 = RainfallDistribution("SCSII-48", tuples_from_csv(dir_name + "/csv/nrcsii48.csv"))
nrcsiii = RainfallDistribution("SCSIII", tuples_from_csv(dir_name + "/csv/nrcsiii.csv"))
orange = RainfallDistribution("ORANGE", tuples_from_csv(dir_name + "/csv/orange.csv"))
sfwmd72 = RainfallDistribution("SFWMD72", tuples_from_csv(dir_name + "/csv/sfwmd72.csv"))
sjrwmd96 = RainfallDistribution("SJRWMD96", tuples_from_csv(dir_name + "/csv/sjrwmd96.csv"))
