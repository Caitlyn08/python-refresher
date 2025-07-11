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

    def test_calculate_angular_acceleration(self):
        self.assertEqual(physics.calculate_angular_acceleration(20, 5), 4)

    def test_calculate_torque(self):
        self.assertEqual(physics.calculate_torque(20, 30, 4), 39.99999999999999)

    def test_calculate_moment_of_inertia(self):
        self.assertEqual(physics.calculate_moment_of_inertia(2, 3), 18)
