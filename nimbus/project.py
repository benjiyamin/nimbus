
from nimbus.network.network import Network
from nimbus.simulation.simulation import Simulation
from nimbus.hydrology.uh import UnitHydrograph
from nimbus.storms.distribution import RainfallDistribution
from nimbus.data.nimlist import NimList
import nimbus.storms.defaults as stm
import nimbus.hydrology.defaults as hyd


class Project:

    def __init__(self, name=None):
        self.name = name
        self.networks = NimList(Network)
        self.simulations = NimList(Simulation)
        self.hydrographs = NimList(UnitHydrograph, hyd.defaults_list)
        self.distributions = NimList(RainfallDistribution, stm.defaults_list)

    def clear_all(self):
        """Remove all objects from the project lists and delete them."""
        self.networks.clear_all()
        self.simulations.clear_all()
        self.distributions.clear_all()
        self.hydrographs.clear_all()
        return
