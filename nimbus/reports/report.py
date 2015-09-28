

class Report:

    def __init__(self):
        self.lines = []

    def add_title(self, title, length=50, offset=4):
        a = '=' * length
        b = '=' * offset + ' ' + title + ' ' + '=' * (length - len(title) - offset - 2)
        self.add_string_line(a)
        self.add_string_line(b)
        self.add_string_line(a)
        self.add_blank_line()
        return

    def add_blank_line(self):
        self.lines.append('')
        return

    def add_break_line(self, length=50):
        self.add_string_line('-' * length)
        return

    def add_string_line(self, string):
        self.lines.append(string)
        return

    def clear_lines(self):
        self.lines = []
        return

    def add_to_columns(self, entries, col_length=15):
        string = ''
        for i, entry in enumerate(entries):
            string += (('%' + str(col_length) + 's ') % entries[i])
        self.lines.append(string)
        return

    def add_columns_line(self, col_count, col_length=15):
        line_list = []
        for col in range(col_count):
            line_list.append('-' * col_length)
        self.add_to_columns(line_list)
        return

    def output(self):
        for line in self.lines:
            print(line)
        self.clear_lines()
        return


def show_objects_in_list(title, object_list, show_class=False):
    report = Report()
    report.add_blank_line()
    if title:
        report.add_title(title)
    string_list = ['Index', 'Name']
    if show_class is True:
        string_list.append('Class')
    report.add_to_columns(string_list)
    report.add_break_line()
    for i, thing in enumerate(object_list):
        if not thing.name:
            name_string = 'Unnamed'
        else:
            name_string = thing.name
        string_list = [i, name_string]
        if show_class is True:
            string_list.append(thing.__class__.__name__)
        report.add_to_columns(string_list)
    report.add_blank_line()
    report.output()
    return


def report_object_list_inputs(title, object_list):
    report = Report()
    report.add_blank_line()
    report.add_title(title)
    report.output()
    for thing in object_list:
        thing.report_inputs(show_title=False)
        report.add_break_line()
        report.add_blank_line()
        report.output()
    return


def float_to_string(number, decimals):
    if number is not None:
        string = ("{:.%sf}" % decimals).format(number)
    else:
        string = 'Undefined'
    return string


def property_to_string(thing, property):
    if thing is not None:
        string = str(getattr(thing, property))
    else:
        string = 'Undefined'
    return string


'''
def show_object_list(title, object_list, show_class=False):
    report = Report()
    if title:
        report.add_title(title)
    for i, thing in enumerate(object_list):
        if not thing.name:
            name_string = 'Unnamed'
        else:
            name_string = thing.name
        string_list = [i, name_string]
        if show_class is True:
            string_list.append(thing.__class__.__name__)
        report.add_to_columns(string_list)
    report.output()
    return
'''


'''
def show_couples_in_list(title, col1_name, col2_name, couple_list):
    report = Report()
    report.add_blank_line()
    if title:
        report.add_title(title)
    report.add_to_columns(['Index', col1_name, col2_name])
    report.add_break_line()
    for i, couple in enumerate(couple_list):
        string_list = [i, couple[0], couple[1]]
        report.add_to_columns(string_list)
    report.add_blank_line()
    report.output()
    return
'''