from tkinter import *
from tkinter import messagebox as mb
from status import Status
from button import TTTButton
from PIL import Image, ImageTk
from choose_user import ChooseUser
import os

class TicTacToe():

    '''Represents a game of tic-tac-toe'''
        
    def __init__(self, master):
        '''Intialize the game tic-tac-toe'''

        ## Save a reference to app root
        self.master = master
        
        ## Load Game Images (Just Once)
        self.load_images()

        ## Init game state
        self.player=0
        self.buttons=[]

        ## Init Widgets
        self.build_game_board()
        
        self.status = Status(master)
        self.status.grid(row=0, columnspan=2, pady=10)

        cmd_btn_frame = Frame(master, highlightbackground='cyan', highlightthickness='1', width=200)
        cmd_btn_frame.grid(row=1, column=1, sticky=NSEW)
        self.new_game_btn = Button(cmd_btn_frame,text='New Game',command=self.new_game)
        self.new_game_btn.pack(side=TOP, pady=10)
        self.end_game_btn = Button(cmd_btn_frame,text='End Game',command=self.end_game,state=DISABLED)
        self.end_game_btn.pack(side=TOP, pady=10)
        
        
    def has_winner(self):
        '''
        If the game has a winner, their player number is returned (1 or 2).
        If the game has no winner and is a cat's game, return -1,
        else return 0.'''
        pass

    def choose_player(self):
        '''
        Allows a user to select who plays first.

        You must:
        - Open a dialog with the following selectable options:
            - Player 1
            - Player 2
            - Random (Will randomly select player 1 or 2)
        - Return the selected user
        '''
        dialog = ChooseUser(self.master,
                            'Choose First Player ',
                            'Choose which player goes first:',
                            ['Player 1', 'Player 2', 'Random'])
        return dialog.result
    
    def clear_game(self, state):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].configure(state=state)
                self.buttons[i][j].configure(image=self.null_image)

    def new_game(self):
        '''
        Initializes and return a new TicTacToe instance.

        You must:
        - Prompt the user to choose who plays first (player 1 or 2)
          (Hint: call choose_player() to show the choose user dialog)
        - Pass the chosen player as 'first_player' to your new instance
        - Enable the 'End Game' button
        - Return the TicTacToe instance.
        '''

        ## Set Player / Update Game Status
        self.player = self.choose_player()
        self.status.set_to_player_turn(self.player)
        
        ## Clear Game / Enable Buttons
        self.clear_game(NORMAL)

        ## Enable End Game Button
        self.end_game_btn['state']=NORMAL

    def end_game(self):
        '''
        Allows a user to end the current tic-tac-toe game.
        You must reset the UI as follows:
        - Clear the game board (i.e. no selected cells)
        - Reset the game status to the welcome message
        - Disable the 'End Game' button and tic-tac-toe buttons
        '''
        self.player = 0
        self.clear_game(DISABLED)
        self.end_game_btn['state']=DISABLED
        self.status.set_to_welcome()
            
    def mark_cell(self, row, col):
        ''' Updates the game grid when a cell is selected by a player '''
        ## Only allow cells to be clicked if game is in play
        ## and buttons state is not disabled
        if self.player > 0 and self.buttons[row][col]['state'] == 'normal':

            ## call btn's click to update image
            self.buttons[row][col].click(self.player)

            ## change player
            if self.player == 1:
                self.player = 2
            else:
                self.player = 1

            ## update window's status
            self.status.set_to_player_turn(self.player)

    def build_game_board(self):
        '''Creates a 3x3 grid containing tic-tac-toe buttons'''

        ## Create button grid container
        container = Frame(self.master, highlightbackground='red', highlightthickness='1')

        ## Configure the grid layout manager to handle window resize
        container.grid(row=1, column=0, sticky=NSEW)
        Grid.columnconfigure(container, 0, weight=1)
        Grid.columnconfigure(container, 1, weight=1)
        Grid.columnconfigure(container, 2, weight=1)
        Grid.rowconfigure(container, 0, weight=1)
        Grid.rowconfigure(container, 1, weight=1)
        Grid.rowconfigure(container, 2, weight=1)

        ## Create the Buttons
        ## - Initial game state will be clear (no Xs or Os shown)
        ## - Button clicks will update the display to an "X" or an "O"
        ## - Button will be disabled until new game is requested
        for i in range(3):
            self.buttons.append([])
            for j in range(3):
                self.buttons[i].append(TTTButton(container,
                                              state=DISABLED,
                                              image=self.null_image,
                                              command=lambda row=i, col=j:self.mark_cell(row, col)))
                self.buttons[i][j].grid(row=i, column=j, sticky=NSEW)

    def load_images(self, x_path='x.png', o_path='o.png', v_path='v.png'):
        ''' Loads game images '''

        ## Create Image Placeholder
        self.null_image = PhotoImage(width=90, height=90)
        
        ## Get base image path
        base_folder = os.path.dirname(__file__)
        image_path = os.path.join(base_folder, "images")

        ## Load "X" image
        x_photo = Image.open(os.path.join(image_path, x_path))
        TTTButton.x_img = ImageTk.PhotoImage(x_photo.resize((90, 90), Image.ANTIALIAS))

        ## Load "O" image
        o_photo = Image.open(os.path.join(image_path, o_path))
        TTTButton.o_img = ImageTk.PhotoImage(o_photo.resize((90, 90), Image.ANTIALIAS))

        ## Load victory image
        self.v_img = PhotoImage(file=os.path.join(image_path, v_path))
        self.v_img.subsample(300, 300)


            
        
