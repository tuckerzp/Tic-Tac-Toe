from GameBoard import GameBoard
import Graphics


class GameConsole:

    set_game = " "
    set_player_one = " "
    set_player_two = " "

    @staticmethod
    def game_choice(game):
        global set_game
        set_game = game
        return game

    def set_player_one(self, player_one):
        if set_game == "player_vs_player":
            self.set_player_one = player_one
            print(player_one)
        return player_one

    def set_player_two(self, player_two):
        if set_game == "player_vs_player":
            self.set_player_two = player_two
            print(player_two)
        return player_two

    game = GameBoard(set_player_one, set_player_two)
    game.print_board()

    @staticmethod
    def update_board(player_number, position):
        if not GameConsole.game.check_win(1) and not GameConsole.game.check_win(2):
            print("Player #%d's turn\n" % player_number)
            if position is None or position > 8 or position < 0:
                print("Error")
            else:
                GameConsole.game.edit_board(player_number, position)
                if Graphics.GameScreen.player_number == 1:
                    Graphics.GameScreen.player_number = 2
                else:
                    Graphics.GameScreen.player_number = 1
            if GameConsole.game.check_win(1):
                Graphics.GameScreen.player_one_win = True
            if GameConsole.game.check_win(2):
                Graphics.GameScreen.player_two_win = True

        GameConsole.game.print_board()
