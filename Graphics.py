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
    pass

    game = " "

    """"
    Sets game choice in PlayGameConsole utility class.
    """
    def game_choice(self):
        global game
        PlayGameConsole.GameConsole.game_choice(game)
        print("game: " + game)

    """"
    Sets game to "Person vs Person" depending if button is pressed with title.
    """
    def p_v_p(self):
        global game
        game = "player_vs_player"
        self.game_choice()

    """"
    Sets game to Person vs Computer depending if button is pressed with title.
    """
    def p_v_c(self):
        global game
        game = "player_vs_computer"
        self.game_choice()

    """"
    Sets game to Computer vs Computer depending if button is pressed with title.
    """
    def c_v_c(self):
        global game
        game = "computer_vs_computer"
        self.game_choice()


class ChooseScreen(Screen):
    pass

    player_one = " "
    player_two = " "
    computer_player = " "
    player_two_exist = True
    player_one_pick = True
    label = StringProperty("Player 1 Choose")

    def set_player_two(self):
        print("your game: " + PlayGameConsole.GameConsole.game_choice(game))
        return PlayGameConsole.GameConsole.game_choice(game) == "player_vs_player"

    def check_pick(self, player_one, player_two):
        if self.set_player_two():
            if self.player_one_pick:
                self.player_one_pick = False
                PlayGameConsole.GameConsole.set_player_one(self, player_one)
                self.label = str("Player 2 Choose")
                self.ids.label_choose.text = self.label
            else:
                if self.manager.current == "Choose":
                    PlayGameConsole.GameConsole.set_player_two(self, player_two)
                    self.manager.transition = FadeTransition()
                    self.manager.current = "Game"
                else:
                    self.manager.current == "Choose"
        else:
            if player_one == "X":
                computer_player = "O"
                print("CPU: " + computer_player)
                self.manager.current = "Game"
            else:
                computer_player = "X"
                print("CPU: " + computer_player)
                self.manager.current = "Game"
                return player_one
                return computer_player

    def x_button_press(self):
        if self.player_one_pick:
            player_one = "X"
            print("player one: " + player_one)
            self.ids.X_Button.color = 1, 1, 1, 0.1
            self.check_pick(player_one, self.player_two)
        elif not self.player_one == "X":
            player_two = "X"
            print("player two: " + player_two)
            self.check_pick(self.player_one, player_two)
        else:
            print("'X' already selected")

    def o_button_press(self):
        if self.player_one_pick:
            player_one = "O"
            print("player one: " + player_one)
            self.ids.O_Button.color = 1, 1, 1, 0.1
            self.check_pick(player_one, self.player_two)
        elif not self.player_one == "O":
            player_two = "O"
            print("player two: " + player_two)
            self.check_pick(self.player_one, player_two)
        else:
            print("'O' already selected")


class GameScreen(Screen):
    pass

    position = None
    player_number = 1
    player_one_win = False
    player_two_win = False
    player_one = " "
    player_two = " "

    def check_win(self):
        if self.player_one_win:
            self.manager.current = "Win"
        if self.player_two_win:
            self.manager.current = "Win"

    def btn0(self):
        position = 0
        PlayGameConsole.GameConsole.update_board(self.player_number, position)
        self.check_win()

    def btn1(self):
        position = 1
        PlayGameConsole.GameConsole.update_board(self.player_number, position)
        self.check_win()

    def btn2(self):
        position = 2
        PlayGameConsole.GameConsole.update_board(self.player_number, position)
        self.check_win()

    def btn3(self):
        position = 3
        PlayGameConsole.GameConsole.update_board(self.player_number, position)
        self.check_win()

    def btn4(self):
        position = 4
        PlayGameConsole.GameConsole.update_board(self.player_number, position)
        self.check_win()

    def btn5(self):
        position = 5
        PlayGameConsole.GameConsole.update_board(self.player_number, position)
        self.check_win()

    def btn6(self):
        position = 6
        PlayGameConsole.GameConsole.update_board(self.player_number, position)
        self.check_win()

    def btn7(self):
        position = 7
        PlayGameConsole.GameConsole.update_board(self.player_number, position)
        self.check_win()

    def btn8(self):
        position = 8
        PlayGameConsole.GameConsole.update_board(self.player_number, position)
        self.check_win()


class WinScreen(Screen):
    pass

    label = StringProperty("Cats game!")

    def player_win(self):
        if GameScreen.player_one_win:
            self.label = str("Player 1 Wins!")
        if GameScreen.player_two_win:
            self.label = str("Player 2 Wins!")


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
        sm.add_widget(ChooseScreen(name="Choose"))
        sm.add_widget(GameScreen(name="Game"))
        sm.add_widget(WinScreen(name="Win"))

        return sm
