# def calculate_average(note1, note2, note3):
#     # Garantindo que as notas estejam no intervalo válido
#     for note in (note1, note2, note3):
#         if not (0 <= note <= 10):
#             raise ValueError("Notas devem estar entre 0 e 10.")
#     return round((note1 + note2 + note3) / 3, 2)

# class TestCalculateAverage(unittest.TestCase):
#     # ... Testes anteriores

#     def test_invalid_note_value(self):
#         with self.assertRaises(ValueError):
#             calculate_average(11, 9, 8)  # Nota inválida
