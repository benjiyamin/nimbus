
from nimbus.network import Network
from nimbus.simulation import Simulation
from nimbus.hydrology import UnitHydrograph
from nimbus.storms import RainfallDistribution
from nimbus.reports import Report


class Project:

    def __init__(self, directory, name=None):
        self.directory = directory
        self.name = name
        self.networks = []
        self.simulations = []
        self.hydrographs = []
        self.distributions = []
        #self.saved = False

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
        return new_network

    def delete_network(self, network):
        """Remove the specified network from the network list and delete it."""
        self.networks.remove(network)
        del network
        return
    
    def clear_networks(self):
        """Remove all network from the network list and delete them."""
        for network in self.networks:
            self.delete_network(network)
        return
    
    def create_simulation(self, *args, **kwargs):
        """Create a simulation, add it to the simulation list, and return the object."""
        new_simulation = Simulation(*args, **kwargs)
        self.simulations.append(new_simulation)
        return new_simulation

    def delete_simulation(self, simulation):
        """Remove the specified simulation from the simulation list and delete it."""
        self.simulations.remove(simulation)
        del simulation
        return
    
    def clear_simulations(self):
        """Remove all simulation from the simulation list and delete them."""
        for simulation in self.simulations:
            self.delete_simulation(simulation)
        return
    
    def create_hydrograph(self, *args, **kwargs):
        """Create a hydrograph, add it to the hydrograph list, and return the object."""
        new_hydrograph = UnitHydrograph(*args, **kwargs)
        self.hydrographs.append(new_hydrograph)
        return new_hydrograph

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
        return
    
    def create_distribution(self, *args, **kwargs):
        """Create a distribution, add it to the distribution list, and return the object."""
        new_distribution = RainfallDistribution(*args, **kwargs)
        self.distributions.append(new_distribution)
        return new_distribution

    def delete_distribution(self, distribution):
        """Remove the specified distribution from the distribution list and delete it."""
        self.distributions.remove(distribution)
        del distribution
        return
    
    def clear_distributions(self):
        """Remove all distribution from the distribution list and delete them."""
        for distribution in self.distributions:
            self.delete_distribution(distribution)
        return

    def report(self, title, report_list):
        report = Report()
        report.add_title(title)
        for i, thing in enumerate(report_list):
            if not thing.name:
                name_string = 'Unnamed'
            else:
                name_string = thing.name
            report.add_string_line(str(i) + ': ' + name_string)
        report.output()
        return

    def report_networks(self):
        title = ' Networks '
        report_list = self.networks
        self.report(title, report_list)
        return

    def report_hydrographs(self):
        title = ' Hydrographs '
        report_list = self.hydrographs
        self.report(title, report_list)
        return

    def report_simulations(self):
        title = ' Simulations '
        report_list = self.simulations
        self.report(title, report_list)
        return

    def report_distributions(self):
        title = ' Distributions '
        report_list = self.distributions
        self.report(title, report_list)
        return
