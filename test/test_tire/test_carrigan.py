import unittest

from tire.carrigan import Carrigan


class TestCarrigan(unittest.TestCase):
    def test_needs_service_true(self):
        condition = [0.8,0.1,0.9,1.0]
        tire = Carrigan(condition)
        self.assertTrue(tire.needs_service())

    def test_needs_service_false(self):
        condition = [0.8, 0.1, 0.8, 0.7]
        tire = Carrigan(condition)
        self.assertFalse(tire.needs_service())