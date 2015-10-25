
import os

from nimbus.data import data as dt
from . import distribution as ds


abs_path = os.path.abspath(__file__)
dir_name = os.path.dirname(abs_path)

delaney = ds.RainfallDistribution("DELANEY", dt.tuples_from_csv(dir_name + "/csv/delaney.csv"))
fdot1 = ds.RainfallDistribution("FDOT-1", dt.tuples_from_csv(dir_name + "/csv/fdot1.csv"))
fdot2 = ds.RainfallDistribution("FDOT-2", dt.tuples_from_csv(dir_name + "/csv/fdot2.csv"))
fdot4 = ds.RainfallDistribution("FDOT-4", dt.tuples_from_csv(dir_name + "/csv/fdot4.csv"))
fdot8 = ds.RainfallDistribution("FDOT-8", dt.tuples_from_csv(dir_name + "/csv/fdot8.csv"))
fdot24 = ds.RainfallDistribution("FDOT-24", dt.tuples_from_csv(dir_name + "/csv/fdot24.csv"))
fdot72 = ds.RainfallDistribution("FDOT-72", dt.tuples_from_csv(dir_name + "/csv/fdot72.csv"))
fdot168 = ds.RainfallDistribution("FDOT-168", dt.tuples_from_csv(dir_name + "/csv/fdot168.csv"))
fdot240 = ds.RainfallDistribution("FDOT-240", dt.tuples_from_csv(dir_name + "/csv/fdot240.csv"))
flmod = ds.RainfallDistribution("FLMOD", dt.tuples_from_csv(dir_name + "/csv/flmod.csv"))
nrcsi24 = ds.RainfallDistribution("SCSI-24", dt.tuples_from_csv(dir_name + "/csv/nrcsi24.csv"))
nrcsi48 = ds.RainfallDistribution("SCSI-48", dt.tuples_from_csv(dir_name + "/csv/nrcsi48.csv"))
nrcsa24 = ds.RainfallDistribution("SCSIA-24", dt.tuples_from_csv(dir_name + "/csv/nrcsia24.csv"))
nrcsii24 = ds.RainfallDistribution("SCSII-24", dt.tuples_from_csv(dir_name + "/csv/nrcsii24.csv"))
nrcsii48 = ds.RainfallDistribution("SCSII-48", dt.tuples_from_csv(dir_name + "/csv/nrcsii48.csv"))
nrcsiii = ds.RainfallDistribution("SCSIII", dt.tuples_from_csv(dir_name + "/csv/nrcsiii.csv"))
orange = ds.RainfallDistribution("ORANGE", dt.tuples_from_csv(dir_name + "/csv/orange.csv"))
sfwmd72 = ds.RainfallDistribution("SFWMD72", dt.tuples_from_csv(dir_name + "/csv/sfwmd72.csv"))
sjrwmd96 = ds.RainfallDistribution("SJRWMD96", dt.tuples_from_csv(dir_name + "/csv/sjrwmd96.csv"))

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
