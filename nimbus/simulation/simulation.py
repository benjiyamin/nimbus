
from .result import Result
from math import ceil
from nimbus.reports import Report, show_object_list, property_to_string, float_to_string
import copy


class Simulation:

    def __init__(self, name=None, filepath=None, duration=None, interval=None,
                 rainfall=None, distribution=None):
        self.name = name
        self.filepath = filepath
        self.duration = duration  # hours
        self.interval = interval  # hours
        self.rainfall = rainfall  # inches
        self.distribution = distribution
        self.networks = []

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
            for node in network.nodes:
                node.curr_stage = node.start_stage
                node.curr_basin_inflow = 0.0
                node.curr_link_inflow = 0.0
                node.curr_link_outflow = 0.0
                curr_inflow = node.curr_basin_inflow + node.curr_link_inflow
                node.results = [(0.0, node.curr_stage, curr_inflow, node.curr_link_outflow)]
                node.basin_hydrographs = []
                for basin in node.basins:
                    hydrograph = basin.get_composite_hydrograph(tabulated_rainfall, self.interval)
                    node.basin_hydrographs.append(hydrograph)
                result_nodes.append(node)
            for link in network.links:
                link.curr_flow = 0.0
                link.curr_stage1 = link.node1.start_stage
                link.curr_stage2 = link.node2.start_stage
                link.results = [(0.0, link.curr_flow, link.curr_stage1, link.curr_stage2)]
                result_links.append(link)
        return result_nodes, result_links

    def run_and_get_result(self):
        last_time = self.duration
        time_steps = ceil(last_time / self.interval)
        sim_networks = copy.deepcopy(self.networks)
        result_nodes, result_links = self.initialize_and_get_result_lists(sim_networks)
        for i in range(1, time_steps):
            time = i * self.interval
            for network in sim_networks:
                for link in network.links:
                    flow = (link.get_flow(link.node1.curr_stage, link.node2.curr_stage) + link.curr_flow) / 2.0  # cfs
                    delta_storage = flow * self.interval / 43560.0 / 60.0 / 60.0                                 # ac-ft
                    node1_storage = link.node1.get_storage(link.node1.curr_stage) - delta_storage                # ac-ft
                    node2_storage = link.node2.get_storage(link.node2.curr_stage) + delta_storage                # ac-ft
                    link.node1.curr_stage = link.node1.get_stage(node1_storage, time)
                    link.node2.curr_stage = link.node2.get_stage(node2_storage, time)
                    link.results.append((time, link.curr_flow))
                for node in network.nodes:
                    node.curr_basin_inflow = sum([hydrograph[i][1] for hydrograph in node.basin_hydrographs])
                    node.results.append((time, node.curr_stage, node.curr_basin_inflow))
        result = Result(result_nodes, result_links)
        return result

    def write(self, result):
        result.write(self.filepath)
        return

    def run_and_write(self):
        result = self.run_and_get_result()
        self.write(result)
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
                  'Filepath: ' + property_to_string(self, 'filepath'),
                  'Duration (hr): ' + float_to_string(self.duration, 2),
                  'Interval (hr): ' + float_to_string(self.interval, 3),
                  'Rainfall (in): ' + float_to_string(self.rainfall, 2),
                  'Distribution: ' + property_to_string(self.distribution, 'name')]
        return inputs

    def show_networks(self):
        title = 'Networks'
        object_list = self.networks
        show_object_list(title, object_list)
        return

    def add_network(self, network):
        """Add the specified network to the network list."""
        self.networks.append(network)
        return

    def remove_network(self, network):
        """Remove the specified network from the network list."""
        self.networks.remove(network)
        return

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
                raise ValueError("Filename must have '.npf' extension!")
            else:
                name += ".npf"
        self.filepath = directory + name
        return
