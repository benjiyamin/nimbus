
from .weir import Weir
from .pipe import Pipe
from nimbus.reports import Report, show_object_list


class Inlet(Pipe):

    def __init__(self, name=None, node1=None, node2=None):
        self.weirs = []
        super(Inlet, self).__init__(name, node1, node2)

    def create_weir(self, *args, **kwargs):
        """Create a weir and add it to the weir list."""
        new_weir = Weir(*args, **kwargs)
        self.weirs.append(new_weir)
        return

    def show_weirs(self):
        title = 'Weir'
        object_list = self.weirs
        show_object_list(title, object_list)
        return

    def get_flow(self, stage1, stage2):
        pipe_flow = super(Inlet, self).get_flow(stage1, stage2)
        weir_flow = sum([weir.get_flow(stage1, stage2) for weir in self.weirs])
        if weir_flow > 0.0 and pipe_flow > 0.0:
            flow = min(weir_flow, pipe_flow)
        elif weir_flow < 0.0 and pipe_flow < 0.0:
            flow = max(weir_flow, pipe_flow)
        else:
            flow = weir_flow + pipe_flow
        return flow

    def report_inputs(self, show_title=True):
        report = Report()
        if show_title is True:
            title = 'Inlet'
            report.add_title(title)
        inputs = self.get_inputs()
        for string in inputs:
            report.add_string_line(string)
        report.output()
        for i, weir in enumerate(self.weirs):
            report.clear_lines()
            report.add_string_line('Weir %s of %s' % (i + 1, len(self.weirs)))
            report.output()
            weir.report_inputs(show_title=False)
            report.add_blank_line()
        return
