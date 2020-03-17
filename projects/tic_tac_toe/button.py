from tkinter import *


class TTTButton(Button):

    '''
    Represents a tic-tac-toe-button:
    - uses x_img and o_img arguments for btn image
    - marked_by stores the value of which player selected the button (0 for none)
    '''
    x_img = None
    o_img = None

    def __init__(self, parent, *args, **kwargs):
        # Make call to super's constructor before any other configuration
        Button.__init__(self, parent, *args, **kwargs)
        self.marked_by = 0

    def click(self, player):
        '''
        Updates the button's image, disables button once clicked by player.
        Image is based on player type:
        - 1: show "X" image
        - 2: show "O" image
        - 0 or -1: None
        '''
        if player == 1 or player == 2:
            if player == 1:
                self.configure(image=TTTButton.x_img)
            elif player == 2:
                self.configure(image=TTTButton.o_img)
            self.marked_by = player
            self.configure(state=DISABLED)
