
import os

from . import uh
from nimbus.data import data


abs_path = os.path.abspath(__file__)
dir_name = os.path.dirname(abs_path)

uh256 = uh.UnitHydrograph("UH256", 256.0, data.tuples_from_csv(dir_name + "/csv/uh256.csv"))
uh323 = uh.UnitHydrograph("UH323", 323.0, data.tuples_from_csv(dir_name + "/csv/uh323.csv"))
uh484 = uh.UnitHydrograph("UH484", 484.0, data.tuples_from_csv(dir_name + "/csv/uh484.csv"))

defaults_list = [uh256, uh323, uh484]
