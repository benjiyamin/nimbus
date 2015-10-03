
from math import ceil

from nimbus.math.math import interpolate_from_table
from nimbus.data.couplelist import CoupleList
from nimbus.reports import float_to_string, property_to_string, InputReport


class UnitHydrograph:

    def __init__(self, name=None, peak_factor=None, runoff_ratios=None):
        self.name = name
        self.peak_factor = peak_factor
        self.runoff_ratios = CoupleList('Time-Runoff Ratios', ('Time', 'Runoff'), runoff_ratios)
        self.report = InputReport(self, self.runoff_ratios)

    def get_flood_hydrograph(self, area, tc, time_step=None):
        delta = 0.133 * tc / 60.0  # hours
        lag = 0.6 * tc / 60.0  # hours
        peak_time = (delta / 2.0) + lag  # hours
        peak_runoff = self.peak_factor * (area / 640.0) / peak_time  # cfs
        flood_hydrograph = []
        uh_couples = self.runoff_ratios.list
        if time_step is None:
            for index in range(len(uh_couples)):
                time_ratio = uh_couples[index][0]
                time = time_ratio * peak_time
                runoff_ratio = uh_couples[index][1]
                runoff = runoff_ratio * peak_runoff
                new_couple = (time, runoff)
                flood_hydrograph.append(new_couple)
        else:
            last_time_ratio = uh_couples[-1][0]
            last_time = last_time_ratio * peak_time
            len_time_steps = ceil(last_time / time_step)
            for t in range(len_time_steps):
                time = t * time_step
                runoff_ratio = self.get_runoff_ratio(time, peak_time)
                runoff = runoff_ratio * peak_runoff
                new_couple = (time, runoff)
                flood_hydrograph.append(new_couple)
            flood_hydrograph.append((flood_hydrograph[-1][0] + time_step, 0.0))
        return flood_hydrograph

    def get_runoff_ratio(self, time, peak_time):
        uh_couples = self.runoff_ratios.list
        runoff_ratio = interpolate_from_table(time / peak_time, uh_couples, 0, 1)
        return runoff_ratio

    def get_input_strings(self):
        inputs = ['Name: ' + property_to_string(self, 'name'),
                  'Peak Factor: ' + float_to_string(self.peak_factor, 3)]
        return inputs