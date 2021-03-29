from random import randint, randrange


class Dice:

    def __init__(self, sides: int):
        self.validate(sides)
        self.__sides = sides

    def validate(self, sides: int):
        if sides <= 1:
            raise ValueError("Dices should have more than one side.")
        return

    def get_sides(self):
        return self.__sides

    def roll(self):
        roll_num = randint(1, self.get_sides())
        return  roll_num


class CrookedDice(Dice):

    def __init__(self, sides: int):
        super().__init__(sides)

    def roll(self):
        # Even random numbers [2, sides]
        roll_num = randrange(2, self.get_sides()+1, 2)
        return roll_num