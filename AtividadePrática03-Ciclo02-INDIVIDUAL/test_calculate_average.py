# test_calculate_average.py
import unittest
from main import calculate_average

class TestCalculateAverage(unittest.TestCase):
    def test_calculate_average(self):
        # Teste padrão com valores dentro do intervalo de 0 a 10
        self.assertEqual(calculate_average(6, 8, 10), 8.0)
        self.assertEqual(calculate_average(0, 0, 0), 0.0)
        self.assertEqual(calculate_average(5, 7.5, 10), 7.5)

    def test_invalid_note_value(self):
        # Teste para valor inválido
        with self.assertRaises(ValueError):
            calculate_average(11, 9, 8)  # Nota inválida, maior que 10
        with self.assertRaises(ValueError):
            calculate_average(-1, 5, 7)  # Nota inválida, menor que 0

if __name__ == '__main__':
    unittest.main()
