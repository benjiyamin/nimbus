
from math import ceil

from nimbus.math import interpolate_from_table


class UnitHydrograph:

    def __init__(self, peak_factor=None, couples=None, name=None):
        self.peak_factor = peak_factor
        if couples is None:
            self.couples = []
        else:
            self.couples = couples
        self.name = name

    def order_couples(self):
        self.couples = sorted(self.couples, key=lambda t: t[0])
        return

    def create_couple(self, time_ratio, runoff_ratio):
        new_couple = (time_ratio, runoff_ratio)
        self.couples.append(new_couple)
        self.order_couples()
        return new_couple

    def delete_couple(self, couple):
        self.couples.remove(couple)
        del couple
        return

    def get_flood_hydrograph(self, area, tc, time_step=None):
        delta = 0.133 * tc / 60.0  # hours
        lag = 0.6 * tc / 60.0  # hours
        peak_time = (delta / 2.0) + lag  # hours
        peak_runoff = self.peak_factor * (area / 640.0) / peak_time  # cfs
        flood_hydrograph = []
        uh_couples = self.couples
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
        uh_couples = self.couples
        runoff_ratio = interpolate_from_table(time / peak_time, uh_couples, 0, 1)
        return runoff_ratio
