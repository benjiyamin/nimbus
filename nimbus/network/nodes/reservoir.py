from math import ceil

from nimbus.network.nodes.node import Node
from nimbus.math import interpolate_from_table, goal_seek
from nimbus.reports import Report


class Reservoir(Node):

    def __init__(self, start_stage=None, contours=None, name=None, basins=None):
        self.start_stage = start_stage
        self.name = name
        if contours is None:
            self.contours = []
        else:
            self.contours = contours
        super(Reservoir, self).__init__(basins)

    def order_contours(self):
        self.contours = sorted(self.contours, key=lambda contour: contour[0])
        return

    def create_contour(self, elevation, area):
        new_contour = (elevation, area)
        self.contours.append(new_contour)
        self.order_contours()
        return new_contour

    def delete_contour(self, contour):
        self.contours.remove(contour)
        del contour
        return

    def get_area(self, elevation):
        if self.contours and len(self.contours) > 1:
            area = interpolate_from_table(elevation, self.contours, 0, 1)
        else:
            area = 0.0
        return area

    def get_storage(self, elevation):
        if self.contours and len(self.contours) > 1:
            min_elevation = min([contour[0] for contour in self.contours])
            max_elevation = max([contour[0] for contour in self.contours])
            if elevation <= min_elevation:
                storage = 0.0
                return storage
            elif elevation >= max_elevation:
                elevation = max_elevation
            new_contour = (elevation, self.get_area(elevation))
            contours = [contour for contour in self.contours if contour[0] < elevation] + [new_contour]
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

    def get_stage(self, storage, time, tolerance=0.0001):
        bound1 = self.contours[0][0]
        bound2 = self.contours[-1][0]
        max_iterations = 100
        stage = goal_seek(self.get_storage, bound1, bound2, storage, max_iterations, tolerance)
        return stage

    '''
    def get_discharge(self, links, stage1, stage2=0.0):
        discharge = 0.0
        for link in links:
            if link.node1 is self:
                discharge += link.get_flow(stage1, stage2)
        return discharge

    def get_discharge_table(self, links, start_stage, time_step, duration):
        len_time_steps = ceil(duration / time_step) + 1
        stage = start_stage
        discharge_table = []
        discharge2 = 0.0  # cfs
        for t in range(len_time_steps):
            discharge1 = discharge2
            if t > 0:
                discharge2 = self.get_discharge(links, stage)
            time = t * time_step
            storage = self.get_storage(stage)  # ac-ft
            discharge = (discharge1 + discharge2) / 2.0
            discharged_volume = discharge * time_step * 3600.0 / 43560.0  # ac-ft
            new_storage = storage - discharged_volume
            stage = self.get_stage(new_storage)
            new_tuple = (time, stage)
            discharge_table.append(new_tuple)
        return discharge_table

    def get_storage_indicator(self, links, time_step, stage1, stage2=0.0):
        discharge = self.get_discharge(links, stage1, stage2)
        storage = self.get_storage(stage1)
        storage_indicator = storage / time_step + discharge / 2.0
        return storage_indicator
    '''

    def report_inputs(self, col_length=15):
        title = ' Reservoir '
        col1_title = 'Stage (ft)'
        col2_title = 'Area (ac)'
        report = Report()
        report.add_title(title)
        report.add_string_line('Name: ' + str(self.name))
        report.add_string_line('Starting Stage: ' + str(self.start_stage))
        report.add_blank_line()
        report.add_two_columns(col1_title, col2_title)
        report.add_two_columns('-' * col_length, '-' * col_length)
        for contour in self.contours:
            report.add_two_columns(str(round(contour[0], 4)), str(round(contour[1], 4)))
        report.output()

    '''
    def get_storage_indicator_table(self, network, stage_step, time_step):
        min_elevation = self.contours[0][0]
        # max_elevation = self.contours[len(self.contours) - 1][0]
        max_elevation = self.contours[-1][0]
        stage_steps = ceil((max_elevation - min_elevation) / stage_step)
        storage_indicator_table = []
        for s in range(stage_steps):
            stage = s * (min_elevation + stage_step)
            discharge = 0.0
            for link in network.links:
                if link.node1 is self:
                    if link.get_flow(stage, stage - link.get_friction_loss()) > 0.0:
                        discharge += link.get_flow(stage, stage - link.get_friction_loss())
                elif link.node2 is self:
                    if link.get_flow(stage, stage + link.get_friction_loss()) < 0.0:
                        discharge += link.get_flow(stage + link.get_friction_loss(), stage)
            storage = self.get_storage(stage)
            storage_indicator = storage / time_step + discharge / 2.0
            new_tuple = (stage, storage_indicator)
            storage_indicator_table.append(new_tuple)
        return storage_indicator_table
    '''
