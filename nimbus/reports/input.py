
from nimbus.reports import Report, show_couples_in_list


class InputReport:

    def __init__(self, parent, couple_list=None):
        self.parent = parent
        self.couple_list = couple_list

    def inputs(self, show_title=True):
        report = Report()
        report.add_blank_line()
        if show_title is True:
            report.add_title(self.parent.__class__.__name__)
        for string in self.parent.get_input_strings():
            report.add_string_line(string)
        report.output()
        if self.couple_list:
            show_couples_in_list(None, self.couple_list.headers, self.couple_list.list)
        return
