
import unittest


class ReservoirTest(unittest.TestCase):

    def setUp(self):
        pass

    def test_elevation_vs_storage2elevation(self):
        from nimbus.network.nodes import Reservoir
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
        nimbus.project.networks.create(name='Test Network')
        network = nimbus.project.networks.get_object_at(0)
        network.nodes.create(name='Test Node')
        network.nodes.copy_object_at(0)
        self.assertNotEqual(network.nodes.get_object_at(0), network.nodes.get_object_at(1))


class SimulationTest(unittest.TestCase):

    def setUp(self):
        pass

    def test_copy(self):
        from nimbus import Nimbus
        nimbus = Nimbus()
        nimbus.new_project()
        nimbus.project.networks.create(name='Test Network')
        network = nimbus.project.networks.get_object_at(0)
        network.nodes.create(name='Test Node')
        network_node = network.nodes.get_object_at(0)
        network_node.start_stage = 0.0
        nimbus.project.simulations.create(name='Test Simulation')
        simulation = nimbus.project.simulations.get_object_at(0)
        simulation.networks.add_object_at(0, nimbus.project.networks.list)
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
