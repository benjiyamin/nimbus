

from nimbus import Nimbus
nimbus = Nimbus()
nimbus.load_project('examples/test_file.npf')
network = nimbus.project.networks[0]
node = network.nodes[1]
basin = node.basins[0]
basin.report_inputs()
