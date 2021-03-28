import unittest
from random import randint
from crooked_dice import CrookedDice


class TestCrookedDice(unittest.TestCase):

    dice_sides = [-100, -10, 5, 0, 20, 5, 6, 1, 2]

    def test_crooked_dice(self):
        for dice_side in TestCrookedDice.dice_sides:
            # Testing constructor
            if dice_side <= 1:
                self.assertRaises(ValueError, CrookedDice, dice_side)
            # Testing getter
            else:
                dice = CrookedDice(dice_side)
                self.assertEqual(dice_side, dice.get_sides())

    def test_get_sides(self):
        dice_sides = randint(3, 100)
        new_dice = CrookedDice(dice_sides)
        self.assertEqual(dice_sides, new_dice.get_sides())

    def test_roll(self):
        for dice_side in TestCrookedDice.dice_sides:
            if dice_side > 1:
                rand_roll = CrookedDice(dice_side).roll()
                self.assertLessEqual(rand_roll, dice_side)
                self.assertGreaterEqual(rand_roll, 1)


if __name__ == '__main__':
    unittest.main()
