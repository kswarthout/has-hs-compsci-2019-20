from tkinter import *
from tic_tac_toe import TicTacToe

def main():
    '''
    The program's entry point
    '''

    ## Window setup
    root = Tk()
    root.geometry('500x400')
    root.title('Tic Tac Toe')

    ## Configure Root's Grid
    Grid.columnconfigure(root, 0, weight=2)
    Grid.columnconfigure(root, 1, weight=1)
    Grid.rowconfigure(root, 1, weight=1)
    
    game = TicTacToe(root)
    root.mainloop()

if __name__ == '__main__': main()



