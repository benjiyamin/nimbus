
import operator as op

from nimbus.reports import report as rp


class ResultReport:

    def __init__(self, parent):
        self.parent = parent

    def node_maximums(self):
        report = rp.Report()
        report.add_blank_line()
        report.add_to_columns(['Name', 'Max',   'Max',   'Max',    'Max',    'Max',     'Max'])
        report.add_to_columns(['',     'Stage', 'Stage', 'Inflow', 'Inflow', 'Outflow', 'Outflow'])
        report.add_to_columns(['',     'Time',  '',      'Time',   '',       'Time',    ''])
        report.add_to_columns(['',     '(hr)',  '(ft)',  '(hr)',   '(cfs)',  '(hr)',    '(cfs)'])
        report.add_break_line(length=16 * 7)
        for node in self.parent.nodes:
            max_stage = max(node.results,        key=op.itemgetter(1))[1]
            max_stage_time = max(node.results,   key=op.itemgetter(1))[0]
            max_inflow = max(node.results,       key=op.itemgetter(2))[2]
            max_inflow_time = max(node.results,  key=op.itemgetter(2))[0]
            max_outflow = max(node.results,      key=op.itemgetter(3))[3]
            max_outflow_time = max(node.results, key=op.itemgetter(3))[0]
            report.add_to_columns([node.name,
                                   rp.float_to_string(max_stage_time,   2),
                                   rp.float_to_string(max_stage,        3),
                                   rp.float_to_string(max_inflow_time,  2),
                                   rp.float_to_string(max_inflow,       3),
                                   rp.float_to_string(max_outflow_time, 2),
                                   rp.float_to_string(max_outflow,      3)])
        report.add_blank_line()
        report.output()
        return

    def link_maximums(self):
        report = rp.Report()
        report.add_blank_line()
        report.add_to_columns(['Name', 'Max',  'Max',   'Max',     'Max',     'Max',     'Max'])
        report.add_to_columns(['',     'Flow', 'Flow',  'Stage 1', 'Stage 1', 'Stage 2', 'Stage 2'])
        report.add_to_columns(['',     'Time', '',      'Time',    '',        'Time',    ''])
        report.add_to_columns(['',     '(hr)', '(cfs)', '(hr)',    '(ft)',    '(hr)',    '(ft)'])
        report.add_break_line(length=16 * 7)
        for link in self.parent.links:
            max_flow = max(link.results,        key=op.itemgetter(1))[1]
            max_flow_time = max(link.results,   key=op.itemgetter(1))[0]
            max_stage1 = max(link.results,      key=op.itemgetter(2))[2]
            max_stage1_time = max(link.results, key=op.itemgetter(2))[0]
            max_stage2 = max(link.results,      key=op.itemgetter(3))[3]
            max_stage2_time = max(link.results, key=op.itemgetter(3))[0]
            report.add_to_columns([link.name,
                                   rp.float_to_string(max_flow_time,   2),
                                   rp.float_to_string(max_flow,        3),
                                   rp.float_to_string(max_stage1_time, 2),
                                   rp.float_to_string(max_stage1,      3),
                                   rp.float_to_string(max_stage2_time, 2),
                                   rp.float_to_string(max_stage2,      3)])
        report.add_blank_line()
        report.output()
        return
