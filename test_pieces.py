import unittest
from random import randint
from pieces import PieceBase, Snake, Ladder, Marker


class PieceBaseTests:

    class BaseTests(unittest.TestCase):

        def setUp(self):
            self.piece = PieceBase

        def get_start_positions(self):
            return [-2, -1, 0, 1, 2, 3, 4, 5, 50, 100, 80]

        def get_end_positions(self):
            return [-3, -1, 0, 5, 50, 66, 92, 70, 82, 25, 20]

        def check_difference(self, start_pos, end_pos):
            if start_pos > 0 and end_pos > 0:
                return True
            return False

        def test_piece(self):

            # Random Position Values
            start_positions = self.get_start_positions()
            end_positions = self.get_end_positions()

            for start_position, end_position in zip(start_positions, end_positions):
                can_use = self.check_difference(start_position, end_position)
                # Testing constructor
                if start_position < 0 or end_position < 0:
                    self.assertRaises(ValueError, self.piece, start_position, end_position)
                # Testing getter methods
                if can_use:
                    piece = self.piece(start_position, end_position)
                    self.assertEqual(start_position, piece.get_start(), "Start position is set to {}, expected {}"
                                     .format(piece.get_start(), start_position))
                    self.assertEqual(end_position, piece.get_end(), "End position is set to {}, expected {}"
                                     .format(piece.get_end(), end_position))

        def get_piece_obj(self, start_pos, end_pos):
            return PieceBase(start_pos, end_pos)

        def test_setter(self):
            # Testing setter methods
            piece = self.get_piece_obj(10, 5)
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

    def get_piece_obj(self, start_pos, end_pos):
        return PieceBase(start_pos, end_pos)


class TestSnake(PieceBaseTests.BaseTests):

    def setUp(self):
        self.piece = Snake

    def get_piece_obj(self, start_pos, end_pos):
        if start_pos > end_pos:
            return PieceBase(start_pos, end_pos)
        else:
            return PieceBase(end_pos, start_pos)

    def get_start_positions(self):
        return [2, 5, 10]

    def get_end_positions(self):
        return [50, 70, 20]

    def check_difference(self, start_pos, end_pos):
        if start_pos < end_pos:
            self.assertRaises(ValueError, self.piece, start_pos, start_pos)
            return False
        return True

class TestLadder(PieceBaseTests.BaseTests):

    def setUp(self):
        self.piece = Ladder

    def get_piece_obj(self, start_pos, end_pos):
        if start_pos < end_pos:
            return PieceBase(start_pos, end_pos)
        else:
            return PieceBase(end_pos, start_pos)

    def get_start_positions(self):
        return [50, 1, 5, 10, 15, 20, 30]

    def get_end_positions(self):
        return [2, 20, 25, 45, 55, 60, 65]

    def check_difference(self, start_pos, end_pos):
        if start_pos > end_pos:
            self.assertRaises(ValueError, self.piece, start_pos, start_pos)
            return False
        return True


class TestMarker(unittest.TestCase):

    def setUp(self) -> None:
        self.piece = Marker

    def test_marker(self):
        positions = [-2, -1, 0, 1, 2, 3, 4, 5, 50, 100]
        for position in positions:
            # Testing constructor
            if position < 0:
                self.assertRaises(ValueError, self.piece, position)
            # Testing getter methods
            else:
                piece = self.piece(position)
                self.assertEqual(position, piece.get_position(), "Position is set to {}, expected {}"
                                 .format(piece.get_position(), position))

    def test_setter(self):
        # Testing setter methods
        piece = self.piece(0)
        new_pos = randint(-100, 100)
        if new_pos < 0:
            self.assertRaises(ValueError, piece.set_position, new_pos)
        else:
            piece.set_position(new_pos)
            self.assertEqual(new_pos, piece.get_position(), "Position is set to {}, expected {}"
                             .format(piece.get_position(), new_pos))


if __name__ == '__main__':
    unittest.main()
