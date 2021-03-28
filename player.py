from pieces import Marker

class Player:

    def __init__(self, name: str, position: int =0):
        Player.validate(name, position)
        self.player_name = name
        self.__marker = Marker(position)

    @staticmethod
    def validate(name, position):
        if not isinstance(name, str):
            raise ValueError("Player name {} is not valid string".format(name))
        if isinstance(position, int):
            if position < 0:
                raise ValueError("Player position {} should be greater than or equal to 0".format(position))
        else:
            print(type(position), position)
            raise TypeError("Invalid type supplied for player position.")

    def get_name(self):
        return self.player_name

    def get_position(self):
        return self.__marker.get_position()

    def set_position(self, val):
        self.validate(self.player_name, val)
        self.__marker.set_position(val)

    def move(self, val):
        self.set_position(val)
