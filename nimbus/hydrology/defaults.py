
import os

from nimbus.data.data import couples_from_csv
from nimbus.hydrology.uh import UnitHydrograph

abs_path = os.path.abspath(__file__)
dir_name = os.path.dirname(abs_path)


uh256 = UnitHydrograph("UH256", 256.0, couples_from_csv(dir_name + "/csv/uh256.csv"))
uh323 = UnitHydrograph("UH323", 323.0, couples_from_csv(dir_name + "/csv/uh323.csv"))
uh484 = UnitHydrograph("UH484", 484.0, couples_from_csv(dir_name + "/csv/uh484.csv"))

defaults_list = [uh256, uh323, uh484]
