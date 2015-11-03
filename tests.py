
import unittest


class ReservoirTest(unittest.TestCase):

    def setUp(self):
        pass

    def test_elevation_vs_storage2elevation(self):
        from nimbus.network.nodes.reservoir import Reservoir
        reservoir = Reservoir()
        reservoir.contours.create(14.0, 0.75)
        reservoir.contours.create(17.0, 0.81)
        reservoir.contours.create(17.0, 2.95)
        reservoir.contours.create(26.0, 4.46)
        reservoir.contours.create(30.5, 5.10)
        reservoir.contours.create(1.5, 6.07)
        test_elevation = 20.0
        storage = reservoir.get_storage(test_elevation)
        elevation = reservoir.get_stage(storage)
        self.assertAlmostEqual(test_elevation, elevation, 3)


class NetworkTest(unittest.TestCase):

    def setUp(self):
        pass

    def test_copy_node(self):
        from nimbus import Nimbus
        nimbus = Nimbus()
        nimbus.new_project()
        nimbus.project.networks.create()
        network = nimbus.project.networks.get(0)
        network.nodes.create()
        network.nodes.copy(0)
        self.assertNotEqual(network.nodes.get(0), network.nodes.get(1))


class GutterTest(unittest.TestCase):

    def setUp(self):
        pass

    def test_get_spread(self):
        from nimbus import Nimbus
        nimbus = Nimbus()
        nimbus.new_project()
        nimbus.project.networks.create()
        network = nimbus.project.networks.get(0)
        network.nodes.create_node()
        node = network.nodes.get(0)
        node.basins.create()
        basin = node.basins.get(0)
        network.links.create_gutter()
        gutter = network.links.get(0)
        basin.shapes.create()
        basin.shapes.create()
        shape1 = basin.shapes.get(0)
        shape1.area = 0.23
        shape1.c = 0.95
        shape2 = basin.shapes.get(1)
        shape2.area = 0.02
        shape2.c = 0.20
        gutter.node1 = node
        gutter.mannings = 0.016
        gutter.long_slope = 0.003
        gutter.section.xs_slope = 0.03
        spread = gutter.get_spread(4.0)
        self.assertAlmostEqual(spread, 6.71, 1)


class SimulationTest(unittest.TestCase):

    def setUp(self):
        pass

    def test_copy(self):
        from nimbus import Nimbus
        nimbus = Nimbus()
        nimbus.new_project()
        nimbus.project.networks.create()
        network = nimbus.project.networks.get(0)
        network.nodes.create()
        network_node = network.nodes.get(0)
        network_node.start_stage = 0.0
        nimbus.project.simulations.create()
        simulation = nimbus.project.simulations.get(0)
        simulation.networks.add_from(0, nimbus.project.networks.list)
        simulation.duration = 1.0
        simulation.interval = 1.0
        simulation.rainfall = 1.0
        from nimbus.storms.defaults import sfwmd72
        simulation.distribution = sfwmd72
        simulation.run_and_set_result()
        result_node = simulation.result.nodes[0]
        self.assertNotEqual(network_node, result_node)


if __name__ == '__main__':
    unittest.main()
