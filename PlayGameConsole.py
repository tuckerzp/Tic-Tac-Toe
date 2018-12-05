from GameBoard import GameBoard


class GameConsole:

    def com_think(self):
        print("clowns")

    @staticmethod
    def player_vs_player():

        print("Enter Player one: ")
        player_one = input()                                                    # Kivy Input Here
        while player_one != "X" and player_one != "O":
            print("Player one must be X or O")
            player_one = input()

        print("Enter Player two: ")
        player_two = input()                                                    # Kivy Input Here
        while player_two != "X" and player_two != "O":
            print("Player two must be X or O")
            player_two = input()                                                # Kivy Input Here

        game = GameBoard(player_one, player_two)
        game.print_board()

        player_number = 1
        while not game.check_win(1) and not game.check_win(2):
            print("Player #%d's turn\n" % player_number)
            print("Enter Position")
            position = int(input())                                             # Kivy Input Here
            if position is None or position > 8 or position < 0:
                print("Error")
            else:
                game.edit_board(player_number, position)
                if player_number == 1:
                    player_number = 2
                else:
                    player_number = 1
                game.print_board()

        game.print_board()




