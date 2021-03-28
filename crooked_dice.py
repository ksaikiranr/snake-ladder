from random import randint


class CrookedDice:

    def __init__(self, sides: int):
        CrookedDice.validate(sides)
        self.__sides = sides

    @staticmethod
    def validate(sides: int):
        if sides <= 1:
            raise ValueError("Dices should have more than one side.")
        return

    def get_sides(self):
        return self.__sides

    def roll(self):
        roll_num = randint(1, self.get_sides())
        return  roll_num
