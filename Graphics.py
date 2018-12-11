from kivy.app import App    # Allows for creation of an Kivy app
from kivy.config import Config
from kivy.lang import Builder
from kivy.properties import StringProperty    # used to change text
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition, SlideTransition    # ScreenManager: keeps track of screens,
# Screen allow for the creation of screens
from kivy.clock import Clock

import PlayGameConsole

# Configure input
Config.set('input', 'mouse', 'mouse,multitouch_on_demand')

# Load .kv file and use
Builder.load_file("graphics.kv")


class TitleScreen(Screen):
    """"
    Introduction Screen

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

    def c_v_c(self):
        """"
        Sets game to Computer vs Computer depending if button is pressed with title.
        """
        global game
        game = "computer_vs_computer"
        self.game_choice()


class GameScreen(Screen):

    position = None
    player_number = 1
    player_one_win = False
    player_two_win = False

    def clear_btns(self):
        self.ids.btn0.text = " "
        self.ids.btn1.text = " "
        self.ids.btn2.text = " "
        self.ids.btn3.text = " "
        self.ids.btn4.text = " "
        self.ids.btn5.text = " "
        self.ids.btn6.text = " "
        self.ids.btn7.text = " "
        self.ids.btn8.text = " "

    def check_win(self):
        if self.player_one_win or self.player_two_win:
            WinScreen.label_change(self.player_one_win, self.player_two_win)
            self.manager.current = "Win"

    def set_piece(self):
        if self.player_number == 1:
            return PlayGameConsole.GameConsole.player_two
        if self.player_number == 2:
            return PlayGameConsole.GameConsole.player_one

    def btn0(self):
        position = 0
        PlayGameConsole.GameConsole.update_board(self.player_number, position)
        self.ids.btn0.text = self.set_piece()
        self.check_win()

    def btn1(self):
        position = 1
        PlayGameConsole.GameConsole.update_board(self.player_number, position)
        self.ids.btn1.text = self.set_piece()
        self.check_win()

    def btn2(self):
        position = 2
        PlayGameConsole.GameConsole.update_board(self.player_number, position)
        self.ids.btn2.text = self.set_piece()
        self.check_win()

    def btn3(self):
        position = 3
        PlayGameConsole.GameConsole.update_board(self.player_number, position)
        self.ids.btn3.text = self.set_piece()
        self.check_win()

    def btn4(self):
        position = 4
        PlayGameConsole.GameConsole.update_board(self.player_number, position)
        self.ids.btn4.text = self.set_piece()
        self.check_win()

    def btn5(self):
        position = 5
        PlayGameConsole.GameConsole.update_board(self.player_number, position)
        self.ids.btn5.text = self.set_piece()
        self.check_win()

    def btn6(self):
        position = 6
        PlayGameConsole.GameConsole.update_board(self.player_number, position)
        self.ids.btn6.text = self.set_piece()
        self.check_win()

    def btn7(self):
        position = 7
        PlayGameConsole.GameConsole.update_board(self.player_number, position)
        self.ids.btn7.text = self.set_piece()
        self.check_win()

    def btn8(self):
        position = 8
        PlayGameConsole.GameConsole.update_board(self.player_number, position)
        self.ids.btn8.text = self.set_piece()
        self.check_win()


class WinScreen(Screen):

    label = str(" ")

    @staticmethod
    def label_change(player_one_win, player_two_win):
        global label
        if player_one_win:
            label = str("O's win!")
        elif player_two_win:
            label = str("X's win!")
        else:
            label = str("Cats game!")
        return label


class GraphicsApp(App):
    def build(self):
        count = 0

        def transition(count):
            if count == 0:
                return SlideTransition()
                count += 1
            if count == 1:
                return FadeTranstion()

        sm = ScreenManager(transition=transition(count))
        sm.add_widget(TitleScreen(name="Title"))
        sm.add_widget(GameScreen(name="Game"))
        sm.add_widget(WinScreen(name="Win"))

        return sm
