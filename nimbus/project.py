
from nimbus.network.network import Network
from nimbus.simulation.simulation import Simulation
from nimbus.hydrology.uh import UnitHydrograph
from nimbus.storms.distribution import RainfallDistribution
from nimbus.data.objectlist import ObjectList
import nimbus.storms.defaults as storms
import nimbus.hydrology.defaults as hydro


class Project:

    def __init__(self, name=None):
        self.name = name
        self.networks = ObjectList(Network)
        self.simulations = ObjectList(Simulation)
        self.hydrographs = ObjectList(UnitHydrograph, hydro.defaults_list)
        self.distributions = ObjectList(RainfallDistribution, storms.defaults_list)
