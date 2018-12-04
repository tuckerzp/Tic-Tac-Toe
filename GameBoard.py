class GameBoard:
    __board = [" ", " ", " ", " ", " ", " ", " ", " "]
    #         ["0", "1", "3", "4", "5", "6", "7", "8"]
    #               0 | 1 | 2
    #               ---------
    #               3 | 4 | 5
    #               ---------
    #               6 | 7 | 9

    __player_one = " "
    __player_two = " "

    # Constructs a game board object
    def __init__(self, player_one, player_two):
        self.__player_one = player_one
        self.__player_two = player_two

    # Returns true if current player has win conditions met
    def check_win(self, player):
        if player == 1:
            letter = self.__player_one
            print("Player one checking...\n")
        elif player == 2:
            letter = self.__player_two
        else:
            print("Error incorrect player")
            return

        if (self.__board[0] == letter and self.__board[1] == letter and self.__board[2] == letter
                or self.__board[3] == letter and self.__board[4] == letter and self.__board[5] == letter
                or self.__board[6] == letter and self.__board[7] == letter and self.__board[8] == letter
                or self.__board[0] == letter and self.__board[3] == letter and self.__board[6] == letter
                or self.__board[1] == letter and self.__board[4] == letter and self.__board[7] == letter
                or self.__board[2] == letter and self.__board[5] == letter and self.__board[8] == letter
                or self.__board[0] == letter and self.__board[4] == letter and self.__board[8] == letter
                or self.__board[2] == letter and self.__board[4] == letter and self.__board[8] == letter):
            return True
        else:
            return False

    # edits board[]'s position using player's character
    # returns true if spot if empty else returns false
    def edit_board(self, player, position):
        if player == 1:
            letter = self.__player_one
            print("Edit Board player one\n")
        elif player == 2:
            letter = self.__player_two
            print("Edit Board player two\n")
        else:
            print("Error incorrect player")
            return

        if self.__board[position] == " ":
            self.__board[position] = letter
            return True
        else:
            print("Position already filled")
            return False

    # returns the board
    def get_board(self):
        return self.__board
