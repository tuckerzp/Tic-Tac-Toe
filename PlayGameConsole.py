from GameBoard import GameBoard
import Graphics

class ComThink:
    __com_win = 10
    __player_win = -10
    __tie = 0

    @staticmethod
    def find_best_move(self, board, player):
        new_board = board.get_board()

        # X | X | X <-- Check for win on this row
        # ---------
        # 3 | 4 | 5
        # ---------
        # 6 | 7 | 9
        if new_board[0] == new_board[1] and new_board[2] == "2":
            return 2
        elif new_board[0] == new_board[2] and new_board[1] == "1":
            return 1
        elif new_board[1] == new_board[2] and new_board[0] == "0":
            return 0

        # 0 | 1 | 2
        # ---------
        # X | X | X <-- Check for win on this row
        # ---------
        # 6 | 7 | 9
        elif new_board[3] == new_board[4] and new_board[5] == "5":
            return 5
        elif new_board[3] == new_board[5] and new_board[4] == "4":
            return 4
        elif new_board[4] == new_board[5] and new_board[3] == "3":
            return 3

        # 0 | 1 | 2
        # ---------
        # 3 | 4 | 5
        # ---------
        # X | X | X <-- Check for win on this row
        elif new_board[6] == new_board[7] and new_board[8] == "8":
            return 8
        elif new_board[6] == new_board[8] and new_board[7] == "7":
            return 7
        elif new_board[7] == new_board[8] and new_board[6] == "6":
            return 6

        # X | 1 | 2 Check for win on column one
        # ---------
        # X | 4 | 5
        # ---------
        # X | 7 | 9
        elif new_board[0] == new_board[3] and new_board[6] == "6":
            return 6
        elif new_board[0] == new_board[6] and new_board[3] == "3":
            return 3
        elif new_board[6] == new_board[3] and new_board[0] == "0":
            return 0

        # 0 | X | 2 Checks for win on column two
        # ---------
        # 3 | X | 5
        # ---------
        # 6 | X | 9
        elif new_board[1] == new_board[4] and new_board[7] == "7":
            return 7
        elif new_board[1] == new_board[7] and new_board[4] == "4":
            return 4
        elif new_board[7] == new_board[4] and new_board[0] == "0":
            return 0

        # 0 | 1 | X
        # ---------
        # 3 | 4 | X
        # ---------
        # 6 | 7 | X
        elif new_board[2] == new_board[5] and new_board[8] == "8":
            return 8
        elif new_board[2] == new_board[8] and new_board[5] == "5":
            return 5
        elif new_board[8] == new_board[5] and new_board[2] == "2":
            return 2

        # X | 1 | 2
        # ---------
        # 3 | X | 5
        # ---------
        # 6 | 7 | X
        elif new_board[0] == new_board[4] and new_board[8] == "8":
            return 8
        elif new_board[0] == new_board[8] and new_board[4] == "4":
            return 4
        elif new_board[8] == new_board[4] and new_board[0] == "0":
            return 0

        # 0 | 1 | X
        # ---------
        # 3 | X | 5
        # ---------
        # X | 7 | 9
        elif new_board[2] == new_board[4] and new_board[6] == "6":
            return 6
        elif new_board[2] == new_board[6] and new_board[4] == "4":
            return 4
        elif new_board[6] == new_board[4] and new_board[2] == "2":
            return 2

        # If middle is empty, play there
        elif new_board[4] == "4":
            return 4

        # If corners are empty, play there
        elif new_board[0] == "0" or new_board[2] == "2" or new_board[6] == "6" or new_board[8] == "8":
            try_spot = 0
            while True:
                if new_board[try_spot] != "X" and new_board[try_spot] != "O":
                    return try_spot
                else:
                    try_spot = try_spot + 2

        # Finally if edges are empty try there
        elif new_board[1] == "1" or new_board[3] == "3" or new_board[5] == "5" or new_board[7] == "7":
            try_spot = 1
            while True:
                if new_board[try_spot] != "X" and new_board[try_spot] != "O":
                    return try_spot
                else:
                    try_spot = try_spot + 2


class GameConsole:

    player_one = "X"
    player_two = "O"
    set_game = " "

    @staticmethod
    def game_choice(game):
        global set_game
        set_game = game
        return set_game

    game = GameBoard(player_one, player_two)
    game.print_board()

    @staticmethod
    def update_board(player_number, position):
        if GameConsole.game.check_win(1) != 1 and GameConsole.game.check_win(2) != 2\
                and GameConsole.game.check_win(1) != 3:
            print("Player #%d's turn\n" % player_number)
            if position is None or position > 8 or position < 0:
                print("Error")
            else:
                GameConsole.game.edit_board(player_number, position)
                if Graphics.GameScreen.player_number == 1:
                    Graphics.GameScreen.player_number = 2
                else:
                    Graphics.GameScreen.player_number = 1
        if GameConsole.game.check_win(1) == 1:
            Graphics.GameScreen.player_one_win = True
        if GameConsole.game.check_win(2) == 2:
            Graphics.GameScreen.player_two_win = True
        if GameConsole.game.check_win(1) == 3:
            Graphics.GameScreen.tie = True

