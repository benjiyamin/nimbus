
import pickle
from nimbus.reports import Report
from operator import itemgetter


class Result:

    def __init__(self, nodes, links):
        self.nodes = nodes
        self.links = links

    def report_node_maximums(self):
        report = Report()
        report.add_to_columns(['Name', 'Max',   'Max',   'Max',    'Max',    'Max',     'Max'])
        report.add_to_columns(['',     'Stage', 'Stage', 'Inflow', 'Inflow', 'Outflow', 'Outflow'])
        report.add_to_columns(['',     'Time',  '',      'Time',   '',       'Time',    ''])
        report.add_to_columns(['',     '(hr)',  '(ft)',  '(hr)',   '(cfs)',  '(hr)',    '(cfs)'])
        report.add_break_line(length=16 * 7)
        for node in self.nodes:
            max_stage = max(node.results, key=itemgetter(1))[1]
            max_stage_time = max(node.results, key=itemgetter(1))[0]
            max_inflow = max(node.results, key=itemgetter(2))[2]
            max_inflow_time = max(node.results, key=itemgetter(2))[0]
            max_outflow = max(node.results, key=itemgetter(3))[3]
            max_outflow_time = max(node.results, key=itemgetter(3))[0]
            '''
            max_stage = max([result[1] for result in node.results])
            max_stage_index = [i for i, j in enumerate(node.results) if j[1] == max_stage][0]
            max_stage_time = node.results[max_stage_index][0]
            max_inflow = max([result[2] for result in node.results])
            max_inflow_index = [i for i, j in enumerate(node.results) if j[2] == max_inflow][0]
            max_inflow_time = node.results[max_inflow_index][0]
            max_outflow = max([result[3] for result in node.results])
            max_outflow_index = [i for i, j in enumerate(node.results) if j[3] == max_outflow][0]
            max_outflow_time = node.results[max_outflow_index][0]
            '''
            report.add_to_columns([node.name,
                                   "{:.2f}".format(max_stage_time),
                                   "{:.3f}".format(max_stage),
                                   "{:.2f}".format(max_inflow_time),
                                   "{:.3f}".format(max_inflow),
                                   "{:.2f}".format(max_outflow_time),
                                   "{:.3f}".format(max_outflow)])
        report.output()
        return

    def report_link_maximums(self):
        pass

    '''
    def write(self, filepath):
        """Pickle self to a save file"""
        if ".nrf" in filepath:
            pass
        elif "." in filepath:
            raise ValueError("Filename must have '.nrf' extension!")
        else:
            filepath += ".nrf"
        open_file = open(filepath, "wb")
        pickle.dump(self, open_file)
        open_file.close()
        return

    @staticmethod
    def load(self, filepath):
        """Unpickle result object from a save file"""
        try:
            open_file = open(filepath, "rb")
            result = pickle.load(open_file)
        except:
            raise ValueError("Not a valid file!")
        open_file.close()
        return result
    '''