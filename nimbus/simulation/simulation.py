
from .result import Result
from math import ceil
from nimbus.reports import Report, show_objects_in_list, property_to_string, float_to_string
import copy
from time import time
from .progress import ProgressBar


class Simulation:

    def __init__(self, name=None, duration=None, interval=None,
                 rainfall=None, distribution=None):
        self.name = name
        '''
        self.filepath = filepath
        '''
        self.duration = duration  # hours
        self.interval = interval  # hours
        self.rainfall = rainfall  # inches
        self.distribution = distribution
        self.networks = []
        self.result = None

    def get_tabulated_accumulated_rainfall(self):
        last_time = self.duration
        time_steps = ceil(last_time / self.interval)
        tabulation = []
        for time_step in range(time_steps):
            time = time_step * self.interval
            new_couple = self.distribution.get_rainfall_couple(self.duration, self.rainfall, time)
            tabulation.append(new_couple)
        tabulation.append((tabulation[len(tabulation) - 1][0] + self.interval, self.rainfall))
        return tabulation

    def initialize_and_get_result_lists(self, network_list):
        tabulated_rainfall = self.get_tabulated_accumulated_rainfall()
        result_nodes = []
        result_links = []
        for network in network_list:
            time = 0.0
            for node in network.nodes:
                node.curr_stage = node.start_stage
                node.curr_link_inflow = 0.0
                node.curr_link_outflow = 0.0
                node.results = [(time, node.curr_stage, node.curr_link_inflow, node.curr_link_outflow)]
                node.basin_hydrographs = []
                for basin in node.basins:
                    hydrograph = basin.get_composite_hydrograph(tabulated_rainfall, self.interval)
                    node.basin_hydrographs.append(hydrograph)
                result_nodes.append(node)
            for link in network.links:
                link.curr_flow = 0.0
                link.curr_stage1 = link.node1.start_stage
                link.curr_stage2 = link.node2.start_stage
                link.results = [(time, link.curr_flow, link.curr_stage1, link.curr_stage2)]
                result_links.append(link)
        return result_nodes, result_links

    def set_stage_and_get_node_result_tuple(self, time_step, curr_time, node):
        basin_inflow = sum([hydrograph[time_step - 1][1] for hydrograph in node.basin_hydrographs])
        average_basin_inflow = self.get_average_basin_inflow(node, time_step)                                   # cfs
        delta_storage = average_basin_inflow * self.interval * 60.0 * 60.0 / 43560.0                            # ac-ft
        node_storage = node.get_storage(node.curr_stage) + delta_storage                                        # ac-ft
        node.curr_stage = node.get_stage(node_storage, curr_time)
        result_tuple = (curr_time, node.curr_stage, basin_inflow, 0.0)
        return result_tuple

    def set_flow_and_get_link_result_tuple(self, curr_time, link):
        average_link_flow = self.get_average_link_inflow(link)                                                  # cfs
        delta_storage = average_link_flow * self.interval * 60.0 * 60.0 / 43560.0                               # ac-ft
        node1_storage = link.node1.get_storage(link.node1.curr_stage) - delta_storage                           # ac-ft
        node2_storage = link.node2.get_storage(link.node2.curr_stage) + delta_storage                           # ac-ft
        link.node1.curr_stage = link.node1.get_stage(node1_storage, curr_time)
        link.node2.curr_stage = link.node2.get_stage(node2_storage, curr_time)
        link.curr_flow = link.get_flow(link.node1.curr_stage, link.node2.curr_stage)
        result_tuple = (curr_time, link.curr_flow, link.node1.curr_stage, link.node2.curr_stage)
        return result_tuple

    def run_and_set_result(self):
        last_time = self.duration
        time_steps = ceil(last_time / self.interval)
        sim_networks = copy.deepcopy(self.networks)
        start_time = time()
        result_nodes, result_links = self.initialize_and_get_result_lists(sim_networks)
        start_message = 'Performing routing simulation and calculations...'
        end_message = 'Success: Routing simulation complete!'
        progress_bar = ProgressBar(60, start_message, end_message)
        progress_bar.begin()
        for i in range(1, time_steps):
            curr_time = i * self.interval
            for network in sim_networks:
                for node in network.nodes:
                    result_tuple = self.set_stage_and_get_node_result_tuple(i, curr_time, node)
                    node.results.append(result_tuple)
                for link in network.links:
                    result_tuple = self.set_flow_and_get_link_result_tuple(curr_time, link)
                    link.results.append(result_tuple)
                    self.adjust_link_flows(link)
            progress_bar.update(i, time_steps)
        progress_bar.complete()
        print("\nTotal simulation time: {:.2f} seconds.\n".format(time() - start_time))
        self.result = Result(result_nodes, result_links)
        return

    @staticmethod
    def get_average_basin_inflow(node, time_step):
        basin_inflow1 = sum([hydrograph[time_step - 1][1] for hydrograph in node.basin_hydrographs])
        basin_inflow2 = sum([hydrograph[time_step][1] for hydrograph in node.basin_hydrographs])
        basin_inflow = (basin_inflow1 + basin_inflow2) / 2.0
        return basin_inflow

    @staticmethod
    def get_average_link_inflow(link):
        link_flow1 = link.curr_flow
        link_flow2 = link.get_flow(link.node1.curr_stage, link.node2.curr_stage)
        link_flow = (link_flow1 + link_flow2) / 2.0
        return link_flow

    @staticmethod
    def adjust_link_flows(link):
        if link.curr_flow > 0.0:
            curr_outflow = link.node1.results[-1][3]
            curr_outflow += link.curr_flow
            last_tuple = link.node1.results.pop()
            new_tuple = (last_tuple[0], last_tuple[1], last_tuple[2], curr_outflow)
            link.node1.results.append(new_tuple)
            curr_inflow = link.node2.results[-1][2]
            curr_inflow += link.curr_flow
            last_tuple = link.node2.results.pop()
            new_tuple = (last_tuple[0], last_tuple[1], curr_inflow, last_tuple[3])
            link.node2.results.append(new_tuple)
        elif link.curr_flow < 0.0:
            curr_outflow = link.node2.results[-1][3]
            curr_outflow -= link.curr_flow
            last_tuple = link.node2.results.pop()
            new_tuple = (last_tuple[0], last_tuple[1], last_tuple[2], curr_outflow)
            link.node2.results.append(new_tuple)
            curr_inflow = link.node1.results[-1][2]
            curr_inflow -= link.curr_flow
            last_tuple = link.node1.results.pop()
            new_tuple = (last_tuple[0], last_tuple[1], curr_inflow, last_tuple[3])
            link.node1.results.append(new_tuple)
        else:
            pass
        return

    def report_inputs(self, title=True):
        title = 'Simulation'
        report = Report()
        if title:
            report.add_title(title)
        inputs = self.get_inputs()
        for string in inputs:
            report.add_string_line(string)
        report.output()
        return

    def get_inputs(self):
        inputs = ['Name: ' + property_to_string(self, 'name'),
                  #'Filepath: ' + property_to_string(self, 'filepath'),
                  'Duration (hr): ' + float_to_string(self.duration, 2),
                  'Interval (hr): ' + float_to_string(self.interval, 3),
                  'Rainfall (in): ' + float_to_string(self.rainfall, 2),
                  'Distribution: ' + property_to_string(self.distribution, 'name')]
        return inputs

    def show_networks(self):
        show_objects_in_list('Networks', self.networks)
        return

    def add_network(self, network):
        """Add the specified network to the network list."""
        self.networks.append(network)
        return

    def remove_network(self, network):
        """Remove the specified network from the network list."""
        self.networks.remove(network)
        return

    '''
    def set_path(self, directory, name=None):
        if name is None:
            if self.name is not None:
                name = self.name + '.nsf'
            else:
                raise ValueError("Must define either a file name or a simulation name")
        else:
            if ".nsf" in name:
                pass
            elif "." in name:
                raise ValueError("Filename must have '.nsf' extension!")
            else:
                name += ".nsf"
        self.filepath = directory + name
        return
    '''

    '''
    def write(self, result):
        result.write(self.filepath)
        return

    def run_and_write(self):
        result = self.run_and_set_result()
        self.write(result)
        return
    '''
