
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

    def create_network(self, *args, **kwargs):
        """Create a network and add it to the network list."""
        new_network = Network(*args, **kwargs)
        append_to_list_and_print(new_network, self.networks)
        return

    def delete_network(self, index):
        """Remove the network at the specified index from the network list and delete it."""
        delete_from_list_and_print(index, self.networks)
        return
    
    def copy_network(self, index):
        """Create a copy of the network at the specified index 
        from the network list and append it to the list"""
        copy_from_list_and_print(index, self.networks)
        return
    
    def clear_networks(self):
        """Remove all networks from the network list and delete them."""
        clear_list_and_print(self.networks, self.delete_network)
        return
    
    def create_simulation(self, *args, **kwargs):
        """Create a simulation, add it to the simulation list, and return the object."""
        new_simulation = Simulation(*args, **kwargs)
        append_to_list_and_print(new_simulation, self.simulations)
        return

    def delete_simulation(self, index):
        """Remove the simulation at the specified index from the simulation list and delete it."""
        delete_from_list_and_print(index, self.simulations)
        return
    
    def copy_simulation(self, index):
        """Create a copy of the simulation at the specified index 
        from the simulation list and append it to the list"""
        copy_from_list_and_print(index, self.simulations)
        return
    
    def clear_simulations(self):
        """Remove all simulation from the simulation list and delete them."""
        clear_list_and_print(self.simulations, self.delete_simulation)
        return
    
    def create_hydrograph(self, *args, **kwargs):
        """Create a hydrograph, add it to the hydrograph list, and return the object."""
        new_hydrograph = UnitHydrograph(*args, **kwargs)
        append_to_list_and_print(new_hydrograph, self.hydrographs)
        return

    def add_hydrograph(self, hydrograph):
        """Add the specified hydrograph to the hydrograph list."""
        self.hydrographs.append(hydrograph)
        return

    def delete_hydrograph(self, index):
        """Remove the hydrograph at the specified index from the hydrograph list and delete it."""
        delete_from_list_and_print(index, self.hydrographs)
        return
    
    def copy_hydrograph(self, index):
        """Create a copy of the hydrograph at the specified index 
        from the hydrograph list and append it to the list"""
        copy_from_list_and_print(index, self.hydrographs)
        return

    def clear_hydrographs(self):
        """Remove all hydrograph from the hydrograph list and delete them."""
        clear_list_and_print(self.hydrographs, self.delete_hydrograph)
        return
    
    def create_distribution(self, *args, **kwargs):
        """Create a distribution, add it to the distribution list, and return the object."""
        new_distribution = RainfallDistribution(*args, **kwargs)
        append_to_list_and_print(new_distribution, self.distributions)
        return

    def delete_distribution(self, index):
        """Remove the distribution at the specified index from the distribution list and delete it."""
        delete_from_list_and_print(index, self.distributions)
        return
    
    def copy_distribution(self, index):
        """Create a copy of the distribution at the specified index 
        from the distribution list and append it to the list"""
        copy_from_list_and_print(index, self.distributions)
        return
    
    def clear_distributions(self):
        """Remove all distribution from the distribution list and delete them."""
        clear_list_and_print(self.distributions, self.delete_distribution)
        return

    def clear_all(self):
        """Remove all objects from the project lists and delete them."""
        self.clear_networks()
        self.clear_hydrographs()
        self.clear_simulations()
        self.clear_distributions()
        return

    def show_networks(self):
        show_object_list('Networks', self.networks)
        return

    def show_hydrographs(self):
        show_object_list('Hydrographs', self.hydrographs)
        return

    def show_simulations(self):
        show_object_list('Simulations', self.simulations)
        return

    def show_distributions(self):
        show_object_list('Distributions', self.distributions)
        return


def clear_list_and_print(_list, delete_function):
    for i, thing in enumerate(_list):
        delete_function(i)
    return


def delete_from_list_and_print(index, _list):
    thing = _list[index]
    _list.remove(thing)
    class_name = thing.__class__.__name__
    del thing
    print("\nSuccess: %s at index %s has been deleted.\n" % (class_name,  index))
    return


def copy_from_list_and_print(index, _list):
    thing = _list[index]
    copy_thing = copy.deepcopy(thing)
    class_name = copy_thing.__class__.__name__
    _list.append(copy_thing)
    print("\nSuccess: %s at index %s has been copied and appended to the list.\n" % (class_name,  index))
    return


def append_to_list_and_print(_object, _list):
    _list.append(_object)
    class_name = _object.__class__.__name__
    print('\nSuccess: New %s created.\n' % class_name)
    return
