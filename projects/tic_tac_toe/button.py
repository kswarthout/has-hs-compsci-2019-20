from tkinter import *

class TTTButton(Button):

    '''
    Represents a tic-tac-toe-button:
    - uses x_img and o_img arguments for btn image
    '''
    
    def __init__(self, parent, *args, **kwargs):
        ## Make call to super's constructor before any other configuration
        Button.__init__(self, parent, *args, **kwargs)

    def click(self, player):
        '''
        Updates the button's image, disables button once clicked by player.
        Image is based on player type:
        - 1: show "X" image
        - 2: show "O" image
        - 0 or -1: None
        '''
        if player == 1:
            self.configure(image=TTTButton.x_img)
            self.configure(state=DISABLED)
        elif player == 2:
            self.configure(image=TTTButton.o_img)
            self.configure(state=DISABLED)

        
            
        
