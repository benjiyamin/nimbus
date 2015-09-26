
from math import pow
from nimbus.reports import Report, property_to_string, float_to_string


class Basin:

    def __init__(self, name=None, area=None, cn=None, tc=None, uh=None):
        self.name = name
        self.area = area  # acres
        self.cn = cn
        self.tc = tc  # minutes
        self.uh = uh

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
        runoff_volume = runoff * self.area * 43560.0 / 12.0
        return runoff_volume  # Cubic Feet

    def get_composite_hydrograph(self, rain_tabulation, time_step):
        flood_hydrograph = self.uh.get_flood_hydrograph(self.area, self.tc, time_step)
        reverse_incremental_runoff = self.get_reverse_incremental_runoff(rain_tabulation)
        if len(flood_hydrograph) < len(reverse_incremental_runoff):
            for i in range(len(flood_hydrograph), len(reverse_incremental_runoff)):
                time = time_step * i
                flood_hydrograph.append((time, 0.0))
        fh_length = len(flood_hydrograph)
        rir_length = len(reverse_incremental_runoff)
        composite_length = fh_length + rir_length
        composite_hydrograph = []
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
        potential_retention = 1000.0 / self.cn - 10.0
        return potential_retention

    def report_inputs(self, show_title=True):
        title = 'Basin'
        report = Report()
        if show_title is True:
            report.add_title(title)
        inputs = self.get_inputs()
        for string in inputs:
            report.add_string_line(string)
        report.output()
        return

    def get_inputs(self):
        inputs = ['Name: ' + property_to_string(self, 'name'),
                  'Area (ac): ' + float_to_string(self.area, 3),
                  'Curve Number: ' + float_to_string(self.cn, 2),
                  'Time of Conc (min): ' + float_to_string(self.tc, 2),
                  'Unit Hydrograph: ' + property_to_string(self.uh, 'name'),
                  'Peak Factor: ' + property_to_string(self.uh, 'peak_factor')]
        return inputs
