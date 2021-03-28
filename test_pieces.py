import unittest
from random import randint
from pieces import PieceBase


class PieceBaseTests:

    class BaseTests(unittest.TestCase):

        def setUp(self):
            self.piece = PieceBase

        def test_PieceBase(self):

            # Random Position Values
            start_positions = [-2, -1, 0, 1, 2, 3, 4, 5, 50, 100, 80]
            end_positions = [-3, -1, 0, 5, 50, 66, 92, 70, 82, 25, 20]

            for start_position, end_position in zip(start_positions, end_positions):
                # Testing constructor
                if start_position < 0 or end_position < 0:
                    self.assertRaises(ValueError, self.piece, start_position, end_position)
                # Testing getter methods
                else:
                    piece = self.piece(start_position, end_position)
                    self.assertEqual(start_position, piece.get_start(), "Start position is set to {}, expected {}"
                                     .format(piece.get_start(), start_position))
                    self.assertEqual(end_position, piece.get_end(), "End position is set to {}, expected {}"
                                     .format(piece.get_end(), end_position))

        def test_setter(self):
            # Testing setter methods
            piece = self.piece(0, 0)
            new_start = randint(-100, 100)
            new_end = randint(-100, 100)
            if new_start < 0:
                self.assertRaises(ValueError, piece.set_start, new_start)
            else:
                piece.set_start(new_start)
                self.assertEqual(new_start, piece.get_start(), "Start position is set to {}, expected {}"
                                 .format(piece.get_start(), new_start))

            if new_end < 0:
                self.assertRaises(ValueError, piece.set_end, new_end)
            else:
                piece.set_end(new_end)
                self.assertEqual(new_end, piece.get_end(), "End position is set to {}, expected {}"
                                 .format(piece.get_end(), new_end))


class TestPiece(PieceBaseTests.BaseTests):

    def setUp(self):
        self.piece = PieceBase


if __name__ == '__main__':
    unittest.main()
