class PieceBase:

    def __init__(self, pos_start: int, pos_end: int) -> None:
        """
        Constructor of the class
        :param pos_start: starting position
        :param pos_end: ending position
        """
        PieceBase.validate_pos(pos_start, pos_end)
        self.__pos_x = pos_start
        self.__pos_y = pos_end

    @staticmethod
    def validate_pos(pos_start, pos_end):
        """
        Validates the starting and ending positions.
        :param pos_start: starting position
        :param pos_end: ending position
        :return:
        """
        if pos_start < 0 or pos_end < 0:
            raise ValueError("Position should be greater than 0")
        return

    def get_start(self) -> int:
        """
        Getter method to get the starting position of the piece.
        :return: starting position
        """
        return self.__pos_x

    def get_end(self) -> int:
        """
        Getter method to get the ending position of the piece.
        :return: ending position
        """
        return self.__pos_y

    def set_start(self, pos_start: int) -> None:
        """
        Setter method for start position
        :param pos_start: new starting position to be used.
        :return: None
        """
        PieceBase.validate_pos(pos_start, self.get_end())
        self.__pos_x = pos_start

    def set_end(self, pos_end: int) -> None:
        """
        Setter method for end position
        :param pos_end: new ending position to be used.
        :return: None
        """
        PieceBase.validate_pos(self.get_start(), pos_end)
        self.__pos_y = pos_end