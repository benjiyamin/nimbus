
from nimbus.network import Network
from nimbus.simulation import Simulation
from nimbus.hydrology import UnitHydrograph
from nimbus.storms import RainfallDistribution
from nimbus.reports import show_object_list


class Project:

    def __init__(self, directory, name=None):
        self.directory = directory
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

    def create_network(self, name=None):
        """Create a network, add it to the network list, and return the object."""
        new_network = Network(name)
        self.networks.append(new_network)
        print('Success: New network created.')
        return

    def delete_network(self, index):
        """Remove the network at the specified index from the network list and delete it."""
        network = self.networks[index]
        self.networks.remove(network)
        del network
        print("Success: Network at index %s has been deleted." % index)
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
        simulation = self.simulations[index]
        self.simulations.remove(simulation)
        del simulation
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

    def delete_hydrograph(self, hydrograph):
        """Remove the specified hydrograph from the hydrograph list and delete it."""
        self.hydrographs.remove(hydrograph)
        del hydrograph
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

    def delete_distribution(self, distribution):
        """Remove the specified distribution from the distribution list and delete it."""
        self.distributions.remove(distribution)
        del distribution
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
