__author__ = 'MillerB'

import unittest
from nimbus.network import Reservoir


class ReservoirTest(unittest.TestCase):

    def setUp(self):
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



if __name__ == '__main__':
    unittest.main()