import unittest

from tire.Octoprime import Octoprime


class TestOctoprime(unittest.TestCase):
    def test_needs_services_true(self):
        condition = [1.0, 0.1, 0.9, 1.0]
        tire = Octoprime(condition)
        self.assertTrue(tire.needs_service())
    def test_needs_services_false(self):
        condition = [1.0, 0.1, 0.8, 1.0]
        tire = Octoprime(condition)
        self.assertFalse(tire.needs_service())

