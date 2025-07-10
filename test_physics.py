import unittest
import physics
import numpy as np


class testPhysics(unittest.TestCase):
    mass = 100
    volume = 0.1

    def test_calculate_buoyancy(self):
        self.assertEqual(physics.calculate_buoyancy(1, 3), 29.43)

    def test_will_it_float(self):
        self.assertEqual(physics.will_it_float(self.volume, self.mass), False)

    def test_calculate_pressure(self):
        self.assertEqual(physics.calculate_pressure(20), 196200.00000000003)

    def test_calculate_acceleration(self):
        self.assertEqual(physics.calculate_acceleration(20, 5), 4)
