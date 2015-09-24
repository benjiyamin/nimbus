
import unittest


class ReservoirTest(unittest.TestCase):

    def setUp(self):
        from nimbus.network.nodes import Reservoir
        self.reservoir = Reservoir()
        self.reservoir.create_contour(14.0, 0.75)
        self.reservoir.create_contour(17.0, 0.81)
        self.reservoir.create_contour(17.0, 2.95)
        self.reservoir.create_contour(26.0, 4.46)
        self.reservoir.create_contour(30.5, 5.10)
        self.reservoir.create_contour(31.5, 6.07)

    def test_elevation_vs_storage2elevation(self):
        test_elevation = 20.0
        storage = self.reservoir.get_storage(test_elevation)
        elevation = self.reservoir.get_stage(storage)
        self.assertAlmostEqual(test_elevation, elevation, 3)


class SimulationTest(unittest.TestCase):

    def setUp(self):
        pass

    def test_copy(self):
        from nimbus import Nimbus
        import os
        nimbus = Nimbus()
        nimbus.new_project(os.getcwd())
        nimbus.project.create_network(name='Test Network')
        network = nimbus.project.networks[0]
        network.create_node(name='Test Node')
        network_node = network.nodes[0]
        network_node.start_stage = 0.0
        nimbus.project.create_simulation(name='Test Simulation')
        simulation = nimbus.project.simulations[0]
        simulation.add_network(network)
        simulation.duration = 1.0
        simulation.interval = 1.0
        simulation.rainfall = 1.0
        from nimbus.storms.defaults import sfwmd72
        simulation.distribution = sfwmd72
        result = simulation.run_and_get_result()
        result_node = result.nodes[0]
        self.assertNotEqual(network_node, result_node)


if __name__ == '__main__':
    unittest.main()
