
import copy
from nimbus.network import Network
from nimbus.simulation import Simulation
from nimbus.hydrology import UnitHydrograph
from nimbus.storms import RainfallDistribution
from nimbus.reports import show_object_list


class Project:

    def __init__(self, name=None):
        #self.directory = directory
        self.name = name
        self.networks = []
        self.simulations = []
        self.hydrographs = []
        self.distributions = []

    def clear_all(self):
        """Remove all objects from the project lists and delete them."""
        self.clear_networks()
        self.clear_hydrographs()
        self.clear_simulations()
        self.clear_distributions()
        return

    @staticmethod
    def delete_from_list(index, _list):
        thing = _list[index]
        _list.remove(thing)
        del thing
        return
    
    @staticmethod
    def copy_from_list(index, _list):
        thing = _list[index]
        copy_thing = copy.deepcopy(thing)
        _list.append(copy_thing)
        return

    def create_network(self, *args, **kwargs):
        """Create a network, add it to the network list, and return the object."""
        new_network = Network(*args, **kwargs)
        self.networks.append(new_network)
        print('Success: New network created.')
        return

    def delete_network(self, index):
        """Remove the network at the specified index from the network list and delete it."""
        self.delete_from_list(index, self.networks)
        print("Success: Network at index %s has been deleted." % index)
        return
    
    def copy_network(self, index):
        """Create a copy of the network at the specified index from the network list and append it to the list"""
        self.copy_from_list(index, self.networks)
        return
    
    def clear_networks(self):
        """Remove all network from the network list and delete them."""
        for network in self.networks:
            self.delete_network(network)
        print("Success: All Network objects have been deleted.")
        return
    
    def create_simulation(self, *args, **kwargs):
        """Create a simulation, add it to the simulation list, and return the object."""
        new_simulation = Simulation(*args, **kwargs)
        self.simulations.append(new_simulation)
        return

    def delete_simulation(self, index):
        """Remove the simulation at the specified index from the simulation list and delete it."""
        self.delete_from_list(index, self.simulations)
        return
    
    def copy_simulation(self, index):
        """Create a copy of the simulation at the specified index from the simulation list and append it to the list"""
        self.copy_from_list(index, self.simulations)
        return
    
    def clear_simulations(self):
        """Remove all simulation from the simulation list and delete them."""
        for simulation in self.simulations:
            self.delete_simulation(simulation)
        print("Success: All Simulation objects have been deleted.")
        return
    
    def create_hydrograph(self, *args, **kwargs):
        """Create a hydrograph, add it to the hydrograph list, and return the object."""
        new_hydrograph = UnitHydrograph(*args, **kwargs)
        self.hydrographs.append(new_hydrograph)
        return

    def add_hydrograph(self, hydrograph):
        """Add the specified hydrograph to the hydrograph list."""
        self.hydrographs.append(hydrograph)
        return

    def delete_hydrograph(self, index):
        """Remove the hydrograph at the specified index from the hydrograph list and delete it."""
        self.delete_from_list(index, self.hydrographs)
        return
    
    def copy_hydrograph(self, index):
        """Create a copy of the hydrograph at the specified index from the hydrograph list and append it to the list"""
        self.copy_from_list(index, self.hydrographs)
        return

    def clear_hydrographs(self):
        """Remove all hydrograph from the hydrograph list and delete them."""
        for hydrograph in self.hydrographs:
            self.delete_hydrograph(hydrograph)
        print("Success: All Hydrograph objects have been deleted.")
        return
    
    def create_distribution(self, *args, **kwargs):
        """Create a distribution, add it to the distribution list, and return the object."""
        new_distribution = RainfallDistribution(*args, **kwargs)
        self.distributions.append(new_distribution)
        return

    def delete_distribution(self, index):
        """Remove the distribution at the specified index from the distribution list and delete it."""
        self.delete_from_list(index, self.distributions)
        return
    
    def copy_distribution(self, index):
        """Create a copy of the distribution at the specified index from the distribution list and append it to the list"""
        self.copy_from_list(index, self.distributions)
        return
    
    def clear_distributions(self):
        """Remove all distribution from the distribution list and delete them."""
        for distribution in self.distributions:
            self.delete_distribution(distribution)
        print("Success: All Distribution objects have been deleted.")
        return

    def show_networks(self):
        title = 'Networks'
        object_list = self.networks
        show_object_list(title, object_list)
        return

    def show_hydrographs(self):
        title = 'Hydrographs'
        object_list = self.hydrographs
        show_object_list(title, object_list)
        return

    def show_simulations(self):
        title = 'Simulations'
        object_list = self.simulations
        show_object_list(title, object_list)
        return

    def show_distributions(self):
        title = 'Distributions'
        object_list = self.distributions
        show_object_list(title, object_list)
        return


'''
@staticmethod
def report_object_list(title, object_list):
    report = Report()
    report.add_title(title)
    for i, thing in enumerate(object_list):
        if not thing.name:
            name_string = 'Unnamed'
        else:
            name_string = thing.name
        report.add_string_line('%s: %s' % (i, name_string))
    report.output()
    return
'''
