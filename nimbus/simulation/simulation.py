
from .result import Result
from math import ceil


class Simulation:

    def __init__(self, filepath, name=None, duration=None, interval=None,
                 rainfall=None, distribution=None, networks=None):
        self.filepath = filepath
        self.name = name
        self.duration = duration
        self.interval = interval
        self.rainfall = rainfall
        self.distribution = distribution
        if networks is None:
            self.networks = []
        else:
            self.networks = networks

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

    def run_and_get_result(self):
        last_time = self.duration
        time_steps = ceil(last_time / self.interval)
        # Time zero adjustments
        result_nodes = []
        result_links = []
        for network in self.networks:
            # Add simulation properties (Make sure to clean up / remove after simulation)
            for node in network.nodes:
                node.curr_stage = node.start_stage
                node.stage_couples = []
                result_nodes.append(node)
            for link in network.links:
                link.curr_flow = 0.0
                link.flow_couples = []
                result_links.append(link)
        for time_step in range(time_steps):
            time = time_step * self.interval
            for network in self.networks:
                for link in network.links:
                    node1 = link.node1
                    node2 = link.node2
                    flow = (link.get_flow(node1.curr_stage, node2.curr_stage) + link.curr_flow) / 2.0   # cfs
                    delta_storage = flow * self.interval / 43560.0 / 60.0 / 60.0                        # ac-ft
                    node1_storage = node1.get_storage(node1.curr_stage) + delta_storage                 # ac-ft
                    node2_storage = node2.get_storage(node2.curr_stage) - delta_storage                 # ac-ft
                    node1.curr_stage = node1.get_stage(node1_storage, time)
                    node2.curr_stage = node2.get_stage(node2_storage, time)
                    link.flow_couples.append((time, link.curr_flow))
                for node in network.nodes:
                    node.stage_couples.append((time, node.curr_stage))
        result = Result(result_nodes, result_links)
        for network in self.networks:
            # Delete simulation properties
            for node in network.nodes:
                del node.curr_stage
                del node.stage_couples
            for link in network.links:
                del link.curr_flow
                del link.flow_couples
        return result

    def write(self, result):
        result.write(self.filepath)
        return

    def run_and_write(self):
        result = self.run_and_get_result()
        self.write(result)
        return

    def add_network(self, network):
        """Add the specified network to the network list."""
        self.networks.append(network)
        return

    def remove_network(self, network):
        """Remove the specified network from the network list."""
        self.networks.remove(network)
        return
