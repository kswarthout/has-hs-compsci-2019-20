from tkinter import *


class Status(Label):

    def __init__(self, parent, *args, **kwargs):
        Label.__init__(self, parent, *args, **kwargs)
        self.configure(font=('Verdana', 15))
        self.set_to_welcome()

    def set_to_player_turn(self, player):
        self.configure(text='Player {:d}\'s Turn'.format(player))

    def set_to_welcome(self):
        self.configure(text='Welcome! Click "New Game" to begin.')

    def set_to_winner(self, player):
        self.configure(text='Player {:d} Wins!'.format(player))
