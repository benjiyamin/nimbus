
import os

from . import intensity as inte
from nimbus.math import matrix as mat
from nimbus.data import data


abs_path = os.path.abspath(__file__)
dir_name = os.path.dirname(abs_path)

fdot01 = inte.Intensity("FDOT ZONE 01", 1, mat.Matrix(data.tuples_from_csv(dir_name + "/csv/zone01.csv")))
fdot02 = inte.Intensity("FDOT ZONE 02", 2, mat.Matrix(data.tuples_from_csv(dir_name + "/csv/zone02.csv")))
fdot03 = inte.Intensity("FDOT ZONE 03", 3, mat.Matrix(data.tuples_from_csv(dir_name + "/csv/zone03.csv")))
fdot04 = inte.Intensity("FDOT ZONE 04", 4, mat.Matrix(data.tuples_from_csv(dir_name + "/csv/zone04.csv")))
fdot05 = inte.Intensity("FDOT ZONE 05", 5, mat.Matrix(data.tuples_from_csv(dir_name + "/csv/zone05.csv")))
fdot06 = inte.Intensity("FDOT ZONE 06", 6, mat.Matrix(data.tuples_from_csv(dir_name + "/csv/zone06.csv")))
fdot07 = inte.Intensity("FDOT ZONE 07", 7, mat.Matrix(data.tuples_from_csv(dir_name + "/csv/zone07.csv")))
fdot08 = inte.Intensity("FDOT ZONE 08", 8, mat.Matrix(data.tuples_from_csv(dir_name + "/csv/zone08.csv")))
fdot09 = inte.Intensity("FDOT ZONE 09", 9, mat.Matrix(data.tuples_from_csv(dir_name + "/csv/zone09.csv")))
fdot10 = inte.Intensity("FDOT ZONE 10", 10, mat.Matrix(data.tuples_from_csv(dir_name + "/csv/zone10.csv")))
fdot11 = inte.Intensity("FDOT ZONE 11", 11, mat.Matrix(data.tuples_from_csv(dir_name + "/csv/zone11.csv")))

defaults_list = [fdot01, fdot02, fdot03, fdot04, fdot05, fdot06, fdot07, fdot08, fdot09, fdot10, fdot11]

