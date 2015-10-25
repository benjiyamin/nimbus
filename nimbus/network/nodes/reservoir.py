
import math
import time as ti

from . import node
from . import storage as sto
from nimbus.math import math as nm
from nimbus.reports import progress as prg
from nimbus.reports import input as inp
from nimbus.data import couple as cpl


class Reservoir(node.Node):

    def __init__(self, name=None, start_stage=None, contours=None):
        super(Reservoir, self).__init__(name, start_stage)
        self.contours = cpl.CoupleList('Contours',
                                       ('Stage (ft)', 'Area (ac)'),
                                       contours)
        self.report = inp.InputReport(self, self.contours)

    def get_area(self, elevation):
        if self.contours.length():
            area = nm.interpolate_from_table(elevation, self.contours.all(), 0, 1)
        else:
            area = 0.0
        return area

    def get_storage(self, elevation):
        if self.contours.length() > 1:
            contour_list = self.contours.all()
            min_elevation = min([contour[0] for contour in contour_list])
            max_elevation = max([contour[0] for contour in contour_list])
            if elevation <= min_elevation:
                storage = 0.0
                return storage
            elif elevation >= max_elevation:
                new_elevation = max_elevation
            else:
                new_elevation = elevation
            new_contour = (new_elevation, self.get_area(new_elevation))
            contours = [c for c in contour_list if c[0] < new_elevation] + [new_contour]
            storage = 0.0
            for i in range(1, len(contours)):
                prev_elevation = contours[i - 1][0]
                prev_area = contours[i - 1][1]
                elevation = contours[i][0]
                area = contours[i][1]
                storage += ((prev_area + area) / 2.0) * (elevation - prev_elevation)
        else:
            storage = 0.0
        return storage

    def get_stage(self, storage, time=None, tolerance=0.0001):
        if self.contours.length() > 1:
            contour_list = self.contours.all()
            bound1 = contour_list[0][0]
            bound2 = contour_list[-1][0]
            max_iterations = 100
            stage = nm.goal_seek(self.get_storage, bound1, bound2, storage, max_iterations, tolerance)
        else:
            stage = self.start_stage
        return stage

    def get_outgoing_links(self, network):
        links = []
        for link in network.links.all():
            links.append(link)
        return

    def run_drawdown_analysis_and_get_time(self, network, start_stage, goal_stage, interval=0.01, max_time=1000.0):
        sim_network = network
        sim_node = [n for n in sim_network.nodes.all() if n is self][0]
        sim_links = []
        sim_node.curr_stage = start_stage
        for link in sim_network.links.all():
            if link.node1 is sim_node:
                sim_links.append(link)
        for link in sim_links:
            link.curr_flow = 0.0
        time_steps = math.ceil(max_time / interval)
        start_time = ti.time()
        start_message = 'Performing drawdown simulation and calculations...'
        end_message = 'Success: Drawdown simulation complete!'
        progress_bar = prg.ProgressBar(60, start_message, end_message)
        progress_bar.begin()
        for i in range(1, time_steps):
            curr_time = i * interval
            curr_flow = 0.0
            for link in sim_links:
                flow1 = link.curr_flow
                flow2 = link.get_flow(sim_node.curr_stage, link.node2.start_stage)
                link.curr_flow = flow2
                curr_flow += (flow1 + flow2) / 2.0
            delta_storage = curr_flow * interval * 60.0 * 60.0 / 43560.0                           # ac-ft
            node_storage = sim_node.get_storage(sim_node.curr_stage) - delta_storage               # ac-ft
            sim_node.curr_stage = sim_node.get_stage(node_storage, curr_time)
            current_progress_int = int((start_stage - sim_node.curr_stage) * 100.0)
            total_progress_int = int((start_stage - goal_stage) * 100.0)
            progress_bar.update(current_progress_int, total_progress_int)
            if sim_node.curr_stage <= goal_stage:
                progress_bar.complete()
                print("\nTotal Calculation time: {:.2f} seconds.\n".format(ti.time() - start_time))
                print('Drawdown Calculated: From {:.2f} ft to {:.2f} ft in {:.2f} hrs\n'.format(start_stage,
                                                                                                sim_node.curr_stage,
                                                                                                curr_time))
                return
        print('Error: Max Time reached')
        for link in sim_links:
            link.curr_flow = None
        sim_node.curr_stage = None
        return
