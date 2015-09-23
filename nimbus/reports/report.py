

class Report:

    def __init__(self):
        self.lines = []
        self.add_blank_line()

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

    '''
    def add_two_columns(self, entry1, entry2, col_length=15):
        string = (('%' + str(col_length) + 's') % entry1) + ' ' + (('%' + str(col_length) + 's') % entry2)
        self.lines.append(string)
        return
    '''

    def add_to_columns(self, entries, col_length=15):
        string = ''
        for i, entry in enumerate(entries):
            string += (('%' + str(col_length) + 's ') % entries[i])
        self.lines.append(string)
        return

    def add_columns_line(self, col_count, col_length=15):
        self.add_to_columns(['-' * col_length, '-' * col_length])
        return

    def output(self):
        self.add_blank_line()
        for line in self.lines:
            print(line)


def show_object_list(title, object_list):
    report = Report()
    report.add_title(title)
    for i, thing in enumerate(object_list):
        if not thing.name:
            name_string = 'Unnamed'
        else:
            name_string = thing.name
        report.add_string_line('%s: %s' % (i, name_string))
    report.output()
    return
