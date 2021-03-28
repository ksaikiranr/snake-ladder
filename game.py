from crooked_dice import CrookedDice
from player import Player
from pieces import Snake, Ladder

class SnakeLadderException(Exception):

    def __init__(self, msg):
        Exception.__init__(self, msg)

class SnakeLadderGame:

    def __init__(self, board_size, player_name, snakes_config, ladders_config):
        self.board_size = board_size
        self.snakes = self.load_snakes(snakes_config)
        self.ladders = self.load_ladders(ladders_config)
        self.player = Player(player_name)
        self.dice = CrookedDice(6)

    def load_snakes(self, snakes_data):
        snakes = []
        for snake_data in snakes_data:
            snakes.append(Snake(snake_data['start'], snake_data['end']))
        return snakes

    def load_ladders(self, ladders_data):
        ladders = []
        for ladder_data in ladders_data:
            ladders.append(Ladder(ladder_data['start'], ladder_data['end']))
        return ladders

    def is_game_over(self):
        player_pos = self.player.get_position()
        if player_pos >= self.board_size:
            return True
        return False

    def is_snake(self, pos):
        for snake in self.snakes:
            if pos == snake.get_start():
                return True
        return False

    def is_ladder(self, pos):
        for ladder in self.ladders:
            if pos == ladder.get_start():
                return True
        return False

    def get_new_pos(self, pos, snake_ladder):
        if snake_ladder:
            for snake in self.snakes:
                if snake.get_start() == pos:
                    return snake.get_end()
        else:
            for ladder in self.ladders:
                if ladder.get_start() == pos:
                    return ladder.get_end()
        if snake_ladder:
            move_via = "Snake"
        else:
            move_via = "Ladder"
        raise SnakeLadderException("Unable to determine new position from {} via {}".format(pos, move_via))

    def start_game(self):
        while not self.is_game_over():
            print("############################################################################################")
            print("Player {}: is at position: {}.".format(self.player.get_name(), self.player.get_position()))
            print("Player {}: rolling dice...".format(self.player.get_name()))

            move_val = self.dice.roll()
            new_pos = self.player.get_position() + move_val
            print("Player {}: got roll: {}".format(self.player.get_name(), move_val))

            if self.is_snake(new_pos):
                print("Player {}: got eaten by Snake at {}.".format(self.player.get_name(), new_pos))
                new_pos = self.get_new_pos(new_pos, True)
                print("Player {}: is at position: {}.".format(self.player.get_name(), new_pos))
            # use if not else if corner case
            if self.is_ladder(new_pos):
                print("Player {}: got ladder at {}.".format(self.player.get_name(), new_pos))
                new_pos = self.get_new_pos(new_pos, False)
                print("Player {}: is at position: {}.".format(self.player.get_name(), new_pos))

            self.player.move(new_pos)
            print("player {}: is at new position: {}.".format(self.player.get_name(), self.player.get_position()))
