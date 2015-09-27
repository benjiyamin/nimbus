
from nimbus.reports import Report, float_to_string
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
            max_stage = max(node.results,        key=itemgetter(1))[1]
            max_stage_time = max(node.results,   key=itemgetter(1))[0]
            max_inflow = max(node.results,       key=itemgetter(2))[2]
            max_inflow_time = max(node.results,  key=itemgetter(2))[0]
            max_outflow = max(node.results,      key=itemgetter(3))[3]
            max_outflow_time = max(node.results, key=itemgetter(3))[0]
            report.add_to_columns([node.name,
                                   float_to_string(max_stage_time,   2),
                                   float_to_string(max_stage,        3),
                                   float_to_string(max_inflow_time,  2),
                                   float_to_string(max_inflow,       3),
                                   float_to_string(max_outflow_time, 2),
                                   float_to_string(max_outflow,      3)])
        report.output()
        return

    def report_link_maximums(self):
        report = Report()
        report.add_to_columns(['Name', 'Max',  'Max',   'Max',     'Max',     'Max',     'Max'])
        report.add_to_columns(['',     'Flow', 'Flow',  'Stage 1', 'Stage 1', 'Stage 2', 'Stage 2'])
        report.add_to_columns(['',     'Time', '',      'Time',    '',        'Time',    ''])
        report.add_to_columns(['',     '(hr)', '(cfs)', '(hr)',    '(ft)',    '(hr)',    '(ft)'])
        report.add_break_line(length=16 * 7)
        for link in self.links:
            max_flow = max(link.results,        key=itemgetter(1))[1]
            max_flow_time = max(link.results,   key=itemgetter(1))[0]
            max_stage1 = max(link.results,      key=itemgetter(2))[2]
            max_stage1_time = max(link.results, key=itemgetter(2))[0]
            max_stage2 = max(link.results,      key=itemgetter(3))[3]
            max_stage2_time = max(link.results, key=itemgetter(3))[0]
            report.add_to_columns([link.name,
                                   float_to_string(max_flow_time,   2),
                                   float_to_string(max_flow,        3),
                                   float_to_string(max_stage1_time, 2),
                                   float_to_string(max_stage1,      3),
                                   float_to_string(max_stage2_time, 2),
                                   float_to_string(max_stage2,      3)])
        report.output()
        return

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