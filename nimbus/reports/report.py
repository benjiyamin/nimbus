__author__ = 'MillerB'


class Report:

    def __init__(self):
        self.lines = []
        self.add_blank_line()

    def add_title(self, title, length=50, offset=4):
        a = '=' * length
        b = '=' * offset + title + '=' * (length - len(title) - offset)
        self.add_string_line(a)
        self.add_string_line(b)
        self.add_string_line(a)
        self.add_blank_line()
        return

    def add_blank_line(self):
        self.lines.append('')
        return

    def add_string_line(self, string):
        self.lines.append(string)
        return

    def add_two_columns(self, entry1, entry2, col_length=15):
        string = (('%' + str(col_length) + 's') % entry1) + ' ' + (('%' + str(col_length) + 's') % entry2)
        self.lines.append(string)
        return

    def output(self):
        for line in self.lines:
            print(line)