import unittest
from main import Resistor


class TestResistor(unittest.TestCase):
    def test_get_res_3_band(self):
        r = Resistor(['brown', 'black', 'red'])
        self.assertAlmostEqual(r.get_res(), 1000.0, places=4)

    def test_get_res_4_band(self):
        r = Resistor(['brown', 'black', 'red', 'gold'])
        self.assertAlmostEqual(r.get_res(), 100.0, places=4)

    def test_get_res_5_band(self):
        r = Resistor(['brown', 'black', 'red', 'orange', 'brown'])
        self.assertAlmostEqual(r.get_res(), 0.1, places=4)

    def test_get_res_6_band(self):
        r = Resistor(['brown', 'black', 'red', 'orange', 'brown', 'brown'])
        self.assertAlmostEqual(r.get_res(), 0.01, places=4)

    def test_get_tol_no_band(self):
        r = Resistor(['brown', 'black', 'red'])
        self.assertIsNone(r.get_tol())

    def test_get_tol_4_band(self):
        r = Resistor(['brown', 'black', 'red', 'gold'])
        self.assertEqual(r.get_tol(), '5%')

    def test_get_tol_5_band(self):
        r = Resistor(['brown', 'black', 'red', 'orange', 'brown'])
        self.assertEqual(r.get_tol(), '1%')

    def test_get_tol_6_band(self):
        r = Resistor(['brown', 'black', 'red', 'orange', 'brown', 'silver'])
        self.assertEqual(r.get_tol(), '10%')


if __name__ == '__main__':
    unittest.main()
