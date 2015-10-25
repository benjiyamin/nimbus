
from nimbus.reports import report as rp
from nimbus.reports import progress as prg
from nimbus.reports import input as inp
from nimbus.data import object as ob
from nimbus.network.nodes.basin.shape import Shape


class Basin:

    def __init__(self, name=None, area=None, cn=None, tc=None, uh=None):
        self.name = name
        self.tc = tc  # minutes
        self.uh = uh
        self.shapes = ob.ObjectList(Shape)
        self.report = inp.InputReport(self)

    def get_weighted_cn(self):
        sum_a = sum([shape.area * shape.cn for shape in self.shapes])
        sum_b = sum([shape.area for shape in self.shapes])
        weighted_cn = sum_a / sum_b
        return weighted_cn

    def get_weighted_c(self):
        sum_a = sum([shape.area * shape.c for shape in self.shapes])
        sum_b = sum([shape.area for shape in self.shapes])
        weighted_c = sum_a / sum_b
        return weighted_c

    def get_total_area(self):
        area = sum([shape.area * shape.c for shape in self.shapes])
        return area

    def get_tabulated_runoff(self, rain_tabulation):
        runoff_tabulation = [(0.0, 0.0, 0.0)]
        for index in range(1, len(rain_tabulation)):
            time = rain_tabulation[index][0]
            accumulated_rainfall2 = rain_tabulation[index][1]
            accumulated_runoff1 = runoff_tabulation[index - 1][1]
            accumulated_runoff2 = self.get_runoff(accumulated_rainfall2)
            incremental_runoff = accumulated_runoff2 - accumulated_runoff1
            new_tuple = (time, accumulated_runoff2, incremental_runoff)
            runoff_tabulation.append(new_tuple)
        return runoff_tabulation

    def get_reverse_incremental_runoff(self, rain_tabulation):
        runoff_tabulation = self.get_tabulated_runoff(rain_tabulation)
        incremental_runoff = []
        for index in range(1, len(runoff_tabulation)):
            increment = runoff_tabulation[index][2]
            incremental_runoff.append(increment)
        reverse_incremental_runoff = list(reversed(incremental_runoff))
        return reverse_incremental_runoff

    def get_runoff_volume(self, rainfall):
        runoff = self.get_runoff(rainfall)  # Inches
        area = self.get_total_area()
        runoff_volume = runoff * area * 43560.0 / 12.0
        return runoff_volume  # Cubic Feet

    def get_composite_hydrograph(self, rain_tabulation, time_step):
        area = self.get_total_area()
        flood_hydrograph = self.uh.get_flood_hydrograph(area, self.tc, time_step)
        reverse_incremental_runoff = self.get_reverse_incremental_runoff(rain_tabulation)
        if len(flood_hydrograph) < len(reverse_incremental_runoff):
            for i in range(len(flood_hydrograph), len(reverse_incremental_runoff)):
                time = time_step * i
                flood_hydrograph.append((time, 0.0))
        fh_length = len(flood_hydrograph)
        rir_length = len(reverse_incremental_runoff)
        composite_length = fh_length + rir_length
        composite_hydrograph = []
        start_message = 'Calculating %s runoff...' % self.name
        end_message = "Success: %s runoff calculations complete!" % self.name
        progress_bar = prg.ProgressBar(60, start_message, end_message)
        progress_bar.begin()
        for i in range(1, composite_length + 1):
            if i < rir_length + 1:
                rir_synth = reverse_incremental_runoff[(rir_length - i):rir_length]
                fh_synth = flood_hydrograph[0:i]
            elif i >= fh_length + 1:
                rir_synth = reverse_incremental_runoff[0:(rir_length - (i - fh_length))]
                fh_synth = flood_hydrograph[(i - rir_length):fh_length]
            else:
                rir_synth = reverse_incremental_runoff[0:rir_length]
                fh_synth = flood_hydrograph[(i - rir_length):i]
            composite_runoff = 0.0
            for j in range(len(fh_synth) - 1):
                composite_runoff += rir_synth[j] * fh_synth[j][1]
            time = time_step * (i - 1)
            new_tuple = (time, composite_runoff)
            composite_hydrograph.append(new_tuple)
            progress_bar.update(i, composite_length)
        progress_bar.complete()
        return composite_hydrograph

    def get_runoff(self, rainfall):
        potential_retention = self.get_potential_retention()
        initial_abstraction = self.get_initial_abstraction()
        if rainfall <= initial_abstraction:
            runoff = 0.0
        else:
            a = pow(rainfall - initial_abstraction, 2.0)
            b = rainfall - initial_abstraction + potential_retention
            runoff = a / b
        return runoff

    def get_initial_abstraction(self):
        potential_retention = self.get_potential_retention()
        initial_abstraction = 0.2 * potential_retention
        return initial_abstraction

    def get_potential_retention(self):
        cn = self.get_weighted_cn()
        potential_retention = 1000.0 / cn - 10.0
        return potential_retention

    def get_input_strings(self):
        area = self.get_total_area()
        cn = self.get_weighted_cn()
        inputs = ['Name: ' + rp.property_to_string(self, 'name'),
                  'Area (ac): ' + rp.float_to_string(area, 3),
                  'Curve Number: ' + rp.float_to_string(cn, 2),
                  'Time of Conc (min): ' + rp.float_to_string(self.tc, 2),
                  'Unit Hydrograph: ' + rp.property_to_string(self.uh, 'name'),
                  'Peak Factor: ' + rp.property_to_string(self.uh, 'peak_factor')]
        return inputs
