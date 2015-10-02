
import os

from nimbus.data import couples_from_csv
from nimbus.storms.distribution import RainfallDistribution


abs_path = os.path.abspath(__file__)
dir_name = os.path.dirname(abs_path)


delaney = RainfallDistribution("DELANEY", couples_from_csv(dir_name + "/csv/delaney.csv"))
fdot1 = RainfallDistribution("FDOT-1", couples_from_csv(dir_name + "/csv/fdot1.csv"))
fdot2 = RainfallDistribution("FDOT-2", couples_from_csv(dir_name + "/csv/fdot2.csv"))
fdot4 = RainfallDistribution("FDOT-4", couples_from_csv(dir_name + "/csv/fdot4.csv"))
fdot8 = RainfallDistribution("FDOT-8", couples_from_csv(dir_name + "/csv/fdot8.csv"))
fdot24 = RainfallDistribution("FDOT-24", couples_from_csv(dir_name + "/csv/fdot24.csv"))
fdot72 = RainfallDistribution("FDOT-72", couples_from_csv(dir_name + "/csv/fdot72.csv"))
fdot168 = RainfallDistribution("FDOT-168", couples_from_csv(dir_name + "/csv/fdot168.csv"))
fdot240 = RainfallDistribution("FDOT-240", couples_from_csv(dir_name + "/csv/fdot240.csv"))
flmod = RainfallDistribution("FLMOD", couples_from_csv(dir_name + "/csv/flmod.csv"))
nrcsi24 = RainfallDistribution("SCSI-24", couples_from_csv(dir_name + "/csv/nrcsi24.csv"))
nrcsi48 = RainfallDistribution("SCSI-48", couples_from_csv(dir_name + "/csv/nrcsi48.csv"))
nrcsa24 = RainfallDistribution("SCSIA-24", couples_from_csv(dir_name + "/csv/nrcsia24.csv"))
nrcsii24 = RainfallDistribution("SCSII-24", couples_from_csv(dir_name + "/csv/nrcsii24.csv"))
nrcsii48 = RainfallDistribution("SCSII-48", couples_from_csv(dir_name + "/csv/nrcsii48.csv"))
nrcsiii = RainfallDistribution("SCSIII", couples_from_csv(dir_name + "/csv/nrcsiii.csv"))
orange = RainfallDistribution("ORANGE", couples_from_csv(dir_name + "/csv/orange.csv"))
sfwmd72 = RainfallDistribution("SFWMD72", couples_from_csv(dir_name + "/csv/sfwmd72.csv"))
sjrwmd96 = RainfallDistribution("SJRWMD96", couples_from_csv(dir_name + "/csv/sjrwmd96.csv"))

defaults_list = [
    delaney,
    fdot1,
    fdot2,
    fdot4,
    fdot8,
    fdot24,
    fdot72,
    fdot168,
    fdot240,
    flmod,
    nrcsi24,
    nrcsi48,
    nrcsa24,
    nrcsii24,
    nrcsii48,
    nrcsiii,
    orange,
    sfwmd72,
    sjrwmd96,
]
