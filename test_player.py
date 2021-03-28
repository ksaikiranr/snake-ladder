import unittest
from player import Player


class TestPlayer(unittest.TestCase):
    def test_player(self):
        names = [ "ABC", "DEF", False]
        marker_pos = [-100, 0 , 100, 20]
        for name, pos in zip(names, marker_pos):
            if not isinstance(name, str):
                self.assertRaises(ValueError, Player, name, 0)
            if isinstance(name, str) and pos < 0:
                self.assertRaises(ValueError, Player, name, pos)


if __name__ == '__main__':
    unittest.main()
