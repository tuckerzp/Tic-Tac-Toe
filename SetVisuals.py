from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout


class GraphicsApp(App):
    # initialization stage of variables
    player1 = True
    player2 = False

    button_id = " "
    button_int = None
    change0 = True
    change1 = True
    change2 = True
    change3 = True
    change4 = True
    change5 = True
    change6 = True
    change7 = True
    change8 = True

    player1Str = "X"
    player2Str = "O"

    # beginning step of GraphicsApp
    def build(self):
        layout = FloatLayout()

        # initialization of all buttons (9 total)
        button0 = Button(id="btn0", text=' ', size_hint=(0.2, 0.2), pos_hint={'x': .1, 'y': 0.7})
        button1 = Button(id="btn1", text=' ', size_hint=(0.2, 0.2), pos_hint={'x': .4, 'y': 0.7})
        button2 = Button(id="btn2", text=' ', size_hint=(0.2, 0.2), pos_hint={'x': .7, 'y': 0.7})
        button3 = Button(id="btn3", text=' ', size_hint=(0.2, 0.2), pos_hint={'x': .1, 'y': 0.4})
        button4 = Button(id="btn4", text=' ', size_hint=(0.2, 0.2), pos_hint={'x': .4, 'y': 0.4})
        button5 = Button(id="btn5", text=' ', size_hint=(0.2, 0.2), pos_hint={'x': .7, 'y': 0.4})
        button6 = Button(id="btn6", text=' ', size_hint=(0.2, 0.2), pos_hint={'x': .1, 'y': 0.1})
        button7 = Button(id="btn7", text=' ', size_hint=(0.2, 0.2), pos_hint={'x': .4, 'y': 0.1})
        button8 = Button(id="btn8", text=' ', size_hint=(0.2, 0.2), pos_hint={'x': .7, 'y': 0.1})

        # Get button position
        def button_num(Button, button_id):
            if button_id == "btn0":
                button_int = 0
            if button_id == "btn1":
                button_int = 1
            if button_id == "btn2":
                button_int = 2
            if button_id == "btn3":
                button_int = 3
            if button_id == "btn4":
                button_int = 4
            if button_id == "btn5":
                button_int = 5
            if button_id == "btn6":
                button_int = 6
            if button_id == "btn7":
                button_int = 7
            if button_id == "btn8":
                button_int = 8
            self.button_int = button_int
            return self.button_int

        # placement of letter in button
        def place_letter(Button):
            if self.player1:
                Button.text = self.player1Str
                print("Player1:" + self.player1Str)
                self.player1 = False
                self.player2 = True
            else:
                Button.text = self.player2Str
                print("Player2:" + self.player2Str)
                self.player2 = False
                self.player1 = True

        # Update GameBoard object
        def update(button_int):
            if self.player1:
                # ** add connection GameBoard.py **
                print("Update Player placement on board")
            elif self.player2:
                # ** add connection GameBoard.py **
                print("Update Player placement on board")
            self.button_int = None
            self.button_id = " "

        # Change text displayed in button
        def change_text(Button):
            self.button_id = Button.id
            button_num(Button, self.button_id)
            print(self.button_int)
            if self.button_int == 0 and self.change0:
                self.change0 = False
                place_letter(Button)
            if self.button_int == 1 and self.change1:
                self.change1 = False
                place_letter(Button)
            if self.button_int == 2 and self.change2:
                self.change2 = False
                place_letter(Button)
            if self.button_int == 3 and self.change3:
                self.change3 = False
                place_letter(Button)
            if self.button_int == 4 and self.change4:
                self.change4 = False
                place_letter(Button)
            if self.button_int == 5 and self.change5:
                self.change5 = False
                place_letter(Button)
            if self.button_int == 6 and self.change6:
                self.change6 = False
                place_letter(Button)
            if self.button_int == 7 and self.change7:
                self.change7 = False
                place_letter(Button)
            if self.button_int == 8 and self.change8:
                self.change8 = False
                place_letter(Button)
            update(self.button_int)

        # Button binding process
        button0.bind(on_press=change_text)
        button1.bind(on_press=change_text)
        button2.bind(on_press=change_text)
        button3.bind(on_press=change_text)
        button4.bind(on_press=change_text)
        button5.bind(on_press=change_text)
        button6.bind(on_press=change_text)
        button7.bind(on_press=change_text)
        button8.bind(on_press=change_text)

        # Adding buttons to layout on GUI
        layout.add_widget(button0)
        layout.add_widget(button1)
        layout.add_widget(button2)
        layout.add_widget(button3)
        layout.add_widget(button4)
        layout.add_widget(button5)
        layout.add_widget(button6)
        layout.add_widget(button7)
        layout.add_widget(button8)

        return layout


if __name__ == "__main__":
    GraphicsApp().run()
