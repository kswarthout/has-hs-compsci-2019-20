from tkinter import *
from tkinter import messagebox
import random

class ChooseUser(Toplevel):

    def __init__(self, parent, title, question, options):
        Toplevel.__init__(self, parent)
        self.title(title)
        self.question = question
        self.transient(parent)
        self.protocol("WM_DELETE_WINDOW",self.cancel)
        self.options = options
        self.result = None

        self.createWidgets()
        self.grab_set()

        self.geometry("+%d+%d" % (parent.winfo_rootx()+50,
                                  parent.winfo_rooty()+50))

        self.wait_window(self)

    def createWidgets(self):
        frmQuestion = Frame(self)
        frmQuestion.grid(row=1, padx=5, pady=5)
        
        Label(frmQuestion,text=self.question).grid()
        
        frmButtons = Frame(self)
        frmButtons.grid(row=2)
        column = 0
        for option in self.options:
            btn = Button(frmButtons,text=option,command=lambda x=option:self.setOption(x))
            btn.grid(column=column,row=0)
            column += 1
            
    def setOption(self,optionSelected):
        if optionSelected == 'Player 1':
            self.result = 1
        elif optionSelected == 'Player 2':
            self.result = 2
        else:
            self.result = random.choice([1, 2])
        self.destroy()
        
    def cancel(self):
        self.result = None
        self.destroy()
        
    
