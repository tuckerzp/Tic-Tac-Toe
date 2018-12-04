from GameBoard import GameBoard


def main():
    print("-------- Testing GameBoard Class -------- \n\n")
    game = GameBoard("X", "O")
    print("Current Board: %r \n" % (game.get_board()))

    game.edit_board(1, 0)
    game.edit_board(1, 1)
    game.edit_board(1, 2)
    print("Current Board: %r \n" % (game.get_board()))

    if game.check_win(1):
        print("Player one wins!")
    else:
        print("Error")


if __name__ == "__main__":
    main()
