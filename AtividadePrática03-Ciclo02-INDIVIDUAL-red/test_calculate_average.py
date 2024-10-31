import unittest
from main import calculate_average  # Função a ser implementada no próximo passo

class TestCalculateAverage(unittest.TestCase):
    def test_average_of_three_notes(self):
        self.assertEqual(calculate_average(8, 9, 10), 9)

    def test_all_zeros(self):
        self.assertEqual(calculate_average(0, 0, 0), 0)

    def test_max_values(self):
        self.assertEqual(calculate_average(10, 10, 10), 10)

    def test_decimal_values(self):
        self.assertAlmostEqual(calculate_average(7.5, 8.5, 9.0), 8.33, places=2)

if __name__ == '__main__':
    unittest.main()
