from kivy.app import App    # Allows for creation of an Kivy app
from kivy.config import Config
from kivy.lang import Builder
from kivy.properties import StringProperty    # used to change text
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition    # ScreenManager: keeps track of screens,
# Screen allow for the creation of screens and FadeTransition allows for a fade to occur between screens

import PlayGameConsole

# Configure input
Config.set('input', 'mouse', 'mouse,multitouch_on_demand')

# Load .kv file and use
Builder.load_file("graphics.kv")


class TitleScreen(Screen):
    """"
    Introduction screen showing options to play

    :param Screen: Screen in GUI. Tasked by screen manager.
    """

    game = " "

    def game_choice(self):
        """"
        Sets game choice in PlayGameConsole utility class.
        """
        PlayGameConsole.GameConsole.game_choice(game)
        print("game: " + game)

    def p_v_p(self):
        """"
        Sets game to "Person vs Person" depending if button is pressed with title.
        """
        global game
        game = "player_vs_player"
        self.game_choice()

    def p_v_c(self):
        """"
        Sets game to Person vs Computer depending if button is pressed with title.
        """
        global game
        game = "player_vs_computer"
        self.game_choice()


class GameScreen(Screen):
    """"
    Main screen showing game board

    :param Screen: Screen in GUI. Tasked by screen manager.
    """
    com_exist = False
    position = None
    player_number = 1
    player_one_win = False
    player_two_win = False
    player_tie = False

    change0 = True
    change1 = True
    change2 = True
    change3 = True
    change4 = True
    change5 = True
    change6 = True
    change7 = True
    change8 = True

    def check_win(self):
        """"
        Check to see if player1 or player2 has one and if so, change screen
        """
        if self.player_one_win:
            self.manager.current = "X"
        if self.player_two_win:
            self.manager.current = "O"
        if self.player_tie:
            self.manager.current = "Cat"

    def set_piece(self):
        """"
        Place player1 or player2's letter on board depending on who's turn it is

        :return: player2s letter
        :return: player1s letter
        """
        if self.player_number == 1:
            return PlayGameConsole.GameConsole.player_two
        if self.player_number == 2:
            return PlayGameConsole.GameConsole.player_one

    def label(self):
        """"
        Change text of id: label_turn
        """
        if self.player_number == 1:
            self.ids.label_turn.text = "Xs turn"
        if self.player_number == 2:
            self.ids.label_turn.text = "Os turn"

    def computer_pick(self):
        """"
        When com_exist variable is true, Computer picks placement of its letter
        """
        self.position = PlayGameConsole.ComThink.find_best_move(PlayGameConsole.GameConsole.game)
        PlayGameConsole.GameConsole.update_board(self.player_number, self.position)
        if self.position == 0:
            self.ids.btn0.text = self.set_piece()
        if self.position == 1:
            self.ids.btn1.text = self.set_piece()
        if self.position == 2:
            self.ids.btn2.text = self.set_piece()
        if self.position == 3:
            self.ids.btn3.text = self.set_piece()
        if self.position == 4:
            self.ids.btn4.text = self.set_piece()
        if self.position == 5:
            self.ids.btn5.text = self.set_piece()
        if self.position == 6:
            self.ids.btn6.text = self.set_piece()
        if self.position == 7:
            self.ids.btn7.text = self.set_piece()
        if self.position == 8:
            self.ids.btn8.text = self.set_piece()
        self.label()
        self.check_win()

    def btn0(self):
        """"
        When btn0 is clicked, the player's piece (letter) is placed in slot 0 on the game board.
        This sets change0 variable to false, not allowing for button or slot's text to be changed.
        Also, when the computer is true (com_exist), the computer will play off of this turn.
        """
        if self.change0:
            self.change0 = False
            position = 0
            PlayGameConsole.GameConsole.update_board(self.player_number, position)
            self.ids.btn0.text = self.set_piece()
            self.label()
            self.check_win()
            if self.com_exist:
                self.computer_pick()

    def btn1(self):
        """"
        When btn1 is clicked, the player's piece (letter) is placed in slot 1 on the game board.
        This sets change1 variable to false, not allowing for button or slot's text to be changed.
        Also, when the computer is true (com_exist), the computer will play off of this turn.
        """
        if self.change1:
            self.change1 = False
            position = 1
            PlayGameConsole.GameConsole.update_board(self.player_number, position)
            self.ids.btn1.text = self.set_piece()
            self.label()
            self.check_win()
            if self.com_exist:
                self.computer_pick()

    def btn2(self):
        """"
        When btn2 is clicked, the player's piece (letter) is placed in slot 2 on the game board.
        This sets change2 variable to false, not allowing for the button or slot's text to be changed.
        Also, when the computer is true (com_exist), the computer will play off of this turn.
        """
        if self.change2:
            self.change2 = False
            position = 2
            PlayGameConsole.GameConsole.update_board(self.player_number, position)
            self.ids.btn2.text = self.set_piece()
            self.label()
            self.check_win()
            if self.com_exist:
                self.computer_pick()

    def btn3(self):
        """"
        When btn3 is clicked, the player's piece (letter) is placed in slot 3 on the game board.
        This sets change3 variable to false, not allowing for the button or slot's text to be changed.
        Also, when the computer is true (com_exist), the computer will play off of this turn.
        """
        if self.change3:
            self.change3 = False
            position = 3
            PlayGameConsole.GameConsole.update_board(self.player_number, position)
            self.ids.btn3.text = self.set_piece()
            self.label()
            self.check_win()
            if self.com_exist:
                self.computer_pick()

    def btn4(self):
        """"
        When btn4 is clicked, the player's piece (letter) is placed in slot 4 on the game board.
        This sets change4 variable to false, not allowing for the button or slot's text to be changed.
        Also, when the computer is true (com_exist), the computer will play off of this turn.
        """
        if self.change4:
            self.change4 = False
            position = 4
            PlayGameConsole.GameConsole.update_board(self.player_number, position)
            self.ids.btn4.text = self.set_piece()
            self.label()
            self.check_win()
            if self.com_exist:
                self.computer_pick()

    def btn5(self):
        """"
        When btn5 is clicked, the player's piece (letter) is placed in slot 5 on the game board.
        This sets change5 variable to false, not allowing for the button or slot's text to be changed.
        Also, when the computer is true (com_exist), the computer will play off of this turn.
        """
        if self.change5:
            self.change5 = False
            position = 5
            PlayGameConsole.GameConsole.update_board(self.player_number, position)
            self.ids.btn5.text = self.set_piece()
            self.label()
            self.check_win()
            if self.com_exist:
                self.computer_pick()

    def btn6(self):
        """"
        When btn6 is clicked, the player's piece (letter) is placed in slot 6 on the game board.
        This sets change6 variable to false, not allowing for the button or slot's text to be changed.
        Also, when the computer is true (com_exist), the computer will play off of this turn.
        """
        if self.change6:
            self.change6 = False
            position = 6
            PlayGameConsole.GameConsole.update_board(self.player_number, position)
            self.ids.btn6.text = self.set_piece()
            self.label()
            self.check_win()
            if self.com_exist:
                self.computer_pick()

    def btn7(self):
        """"
        When btn7 is clicked, the player's piece (letter) is placed in slot 7 on the game board.
        This sets change7 variable to false, not allowing for the button or slot's text to be changed.
        Also, when the computer is true (com_exist), the computer will play off of this turn.
        """
        if self.change7:
            self.change7 = False
            position = 7
            PlayGameConsole.GameConsole.update_board(self.player_number, position)
            self.ids.btn7.text = self.set_piece()
            self.label()
            self.check_win()
            if self.com_exist:
                self.computer_pick()

    def btn8(self):
        """"
        When btn8 is clicked, the player's piece (letter) is placed in slot 8 on the game board.
        This sets change8 variable to false, not allowing for the button or slot's text to be changed.
        Also, when the computer is true (com_exist), the computer will play off of this turn.
        """
        if self.change8:
            self.change8 = False
            position = 8
            PlayGameConsole.GameConsole.update_board(self.player_number, position)
            self.ids.btn8.text = self.set_piece()
            self.label()
            self.check_win()
            if self.com_exist:
                self.computer_pick()


class XScreen(Screen):
    """"
    X's Win screen showing after X wins the game

    :param Screen: Screen in GUI. Tasked by screen manager.
    """
    def end_game(self):
        """"
        When end_btn is pressed program closes
        """
        exit()


class OScreen(Screen):
    """"
    O's Win screen showing after O wins the game

    :param Screen: Screen in GUI. Tasked by screen manager.
    """
    def end_game(self):
        """"
        When end_btn is pressed program closes
        """
        exit()


class CatScreen(Screen):
    """"
    Cats Screen shows after no one wins the game

    :param Screen: Screen in GUI. Tasked by screen manager.
    """
    def end_game(self):
        """"
        When end_btn is pressed program closes
        """
        exit()


class GraphicsApp(App):
    """"
    GraphicsApp starts up the GUI, with organized screens

    :param App: This helps open the application with GUI
    """
    def build(self):
        """"
        These are the main building blocks for the program, including the screen manager

        :return: Returns the screen manager object
        """
        sm = ScreenManager(transition=FadeTransition())
        sm.add_widget(TitleScreen(name="Title"))
        sm.add_widget(GameScreen(name="Game"))
        sm.add_widget(XScreen(name="X"))
        sm.add_widget(OScreen(name="O"))
        sm.add_widget(CatScreen(name="Cat"))

        return sm
