from GameBoard import GameBoard
import Graphics


class GameConsole:

    player_one = "X"
    player_two = "O"
    set_game = " "

    @staticmethod
    def game_choice(game):
        global set_game
        set_game = game
        return set_game
        self.board()

    game = GameBoard(player_one, player_two)
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
