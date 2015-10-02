
import os

from nimbus.data import couples_from_csv
from nimbus.hydrology.uh import UnitHydrograph

abs_path = os.path.abspath(__file__)
dir_name = os.path.dirname(abs_path)


uh256 = UnitHydrograph(256.0, couples_from_csv(dir_name + "/csv/uh256.csv"), "UH256")
uh323 = UnitHydrograph(323.0, couples_from_csv(dir_name + "/csv/uh323.csv"), "UH323")
uh484 = UnitHydrograph(484.0, couples_from_csv(dir_name + "/csv/uh484.csv"), "UH484")

defaults_list = [uh256, uh323, uh484]