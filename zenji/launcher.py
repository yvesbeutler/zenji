from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.dropdown import DropDown

class MainWindow(GridLayout):
    def __init__(self, **kwargs):
        super(MainWindow, self).__init__(**kwargs)
        self.cols=2
        self.add_widget(Label(text='Board size'))
        self.board_size = TextInput(multiline=False)
        self.add_widget(self.board_size)
        self.add_widget(Label(text='Animation speed'))
        self.speed = TextInput(multiline=False)
        self.add_widget(self.speed)
        self.add_widget(Label(text='Algorithm'))
        self.add_widget(DropDown())

class Zenji(App):
    def build(self):
        return MainWindow()

if __name__ == '__main__':
    Zenji().run()