import unittest
from random import randint
from dice import Dice, CrookedDice


class TestDice:

    class TestBasicDice(unittest.TestCase):

        dice_sides = [-100, -10, 5, 0, 20, 5, 6, 1, 2]

        def setUp(self) -> None:
            self.dice = Dice

        def test_dice(self):
            for dice_side in TestDice.TestBasicDice.dice_sides:
                # Testing constructor
                if dice_side <= 1:
                    self.assertRaises(ValueError, self.dice, dice_side)
                # Testing getter
                else:
                    dice = self.dice(dice_side)
                    self.assertEqual(dice_side, dice.get_sides())

        def test_get_sides(self):
            dice_sides = randint(3, 100)
            new_dice = self.dice(dice_sides)
            self.assertEqual(dice_sides, new_dice.get_sides())

        def test_roll(self):
            for dice_side in TestDice.TestBasicDice.dice_sides:
                if dice_side > 1:
                    rand_roll = self.dice(dice_side).roll()
                    self.assertLessEqual(rand_roll, dice_side)
                    self.assertGreaterEqual(rand_roll, 1)


class TestCrookedDice(TestDice.TestBasicDice):

    def setUp(self) -> None:
        self.dice = CrookedDice

    def test_roll(self):
        for dice_side in TestDice.TestBasicDice.dice_sides:
            if dice_side > 1:
                rand_roll = self.dice(dice_side).roll()
                self.assertEqual(rand_roll%2, 0)



if __name__ == '__main__':
    unittest.main()
