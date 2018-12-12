from kivy.app import App    # Allows for creation of an Kivy app
from kivy.config import Config
from kivy.lang import Builder
from kivy.properties import StringProperty    # used to change text
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition, SlideTransition    # ScreenManager: keeps track of screens,
# Screen allow for the creation of screens

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


class GameScreen(Screen):

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

    def change_btn(self, position):
        if position == 0:
            GameScreen.ids.btn0.text = " "
            self.change0 = False
        if position == 1:
            self.GameScreen.ids.btn1.text = " "
            self.GameScreen.change1 = False
        if position == 2:
            self.GameScreen.ids.btn2.text = " "
            self.GameScreen.change2 = False
        if position == 3:
            self.GameScreen.ids.btn3.text = " "
            self.GameScreen.change3 = False
        if position == 4:
            self.GameScreen.ids.btn4.text = " "
            self.GameScreen.change4 = False
        if position == 5:
            self.GameScreen.ids.btn5.text = " "
            self.GameScreen.change5 = False
        if position == 6:
            self.GameScreen.ids.btn6.text = " "
            self.GameScreen.change6 = False
        if position == 7:
            self.GameScreen.ids.btn7.text = " "
            self.GameScreen.change7 = False
        if position == 8:
            self.GameScreen.ids.btn8.text = " "
            self.GameScreen.change8 = False

    def check_win(self):
        if self.player_one_win:
            self.manager.current = "X"
        if self.player_two_win:
            self.manager.current = "O"
        if self.player_tie:
            self.manager.current = "Cat"

    def set_piece(self):
        if self.player_number == 1:
            return PlayGameConsole.GameConsole.player_two
        if self.player_number == 2:
            return PlayGameConsole.GameConsole.player_one

    def label(self):
        if self.player_number == 1:
            self.ids.label_turn.text = "Xs turn"
        if self.player_number == 2:
            self.ids.label_turn.text = "Os turn"

    def computer_pick(self):
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
    def end_game(self):
        exit()


class OScreen(Screen):
    def end_game(self):
        exit()


class CatScreen(Screen):
    def end_game(self):
        exit()


class GraphicsApp(App):
    def build(self):

        sm = ScreenManager(transition=FadeTransition())
        sm.add_widget(TitleScreen(name="Title"))
        sm.add_widget(GameScreen(name="Game"))
        sm.add_widget(XScreen(name="X"))
        sm.add_widget(OScreen(name="O"))
        sm.add_widget(CatScreen(name="Cat"))

        return sm
