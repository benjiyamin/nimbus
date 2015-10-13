
from nimbus.network import network as nw
from nimbus.simulation import simulation as sm
from nimbus.hydrology import uh
from nimbus.storms import distribution as ds
from nimbus.data import object as ob
import nimbus.storms.defaults as sd
import nimbus.hydrology.defaults as hd


class Project:

    def __init__(self, name=None):
        self.name = name
        self.networks = ob.ObjectList(nw.Network)
        self.simulations = ob.ObjectList(sm.Simulation)
        self.hydrographs = ob.ObjectList(uh.UnitHydrograph, hd.defaults_list)
        self.distributions = ob.ObjectList(ds.RainfallDistribution, sd.defaults_list)
