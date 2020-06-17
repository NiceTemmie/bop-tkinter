#!/usr/bin/python3.7
# -*-coding:Utf-8 -*
from tkinter import *
from bop import BopValues as BV
from bop import BopGames as BG
from tkinter.font import Font
from widgets import *

class NavigationMenu(Frame):

    def __init__(self,master=None):
        super().__init__(master,background=BV["COLOR_MENU"],width=BV["WIDTH"]/4,height=BV["HEIGHT"])
        self.grid_propagate(0)
        self.columnconfigure(0,weight=1) #fill all the widgets width
        self.font_bop = Font(family="Open sans extra bold",size=63)
        Label(self,text="Bop!",font=self.font_bop,foreground=BV["COLOR_BACKGROUND"],background=BV["COLOR_MENU"]).grid()
        self.gameScreen=GameScreen(master)
        self.gameScreen.grid(column=1,row=0,sticky=N+S)



class GameScreen(Frame):
    def __init__(self, master=None):
        super().__init__(master,background=BV["COLOR_BACKGROUND2"],height=BV["HEIGHT"],width=BV["WIDTH"]*3/4)
        self.low=0
        self.hight=8
        self.pages_number=len(BV["GAME_LIST"])//8 #Get the numbers of pages (8games/page) it work like that cause the pages starts to 0 not 1 so no need of +1
        self.page=0

        self.grid_propagate(0)
        self.show_game()

    def show_game(self):
        for widget in self.winfo_children():
            widget.destroy()

        page_text = ("Page {}/{}".format(self.page+1,self.pages_number+1))
        Label(self,text=page_text,background=BV["COLOR_BACKGROUND"]).grid(row=0,column=1)

        if self.page != 0:
            Button(self,text="Previous page",command=self.triggered_previouspage_button,background=BV["COLOR_BACKGROUND"],relief=FLAT).grid(column=0,row=0)
        if self.page != self.pages_number:
            Button(self,text="Next page",command=self.triggered_nextpage_button,background=BV["COLOR_BACKGROUND"],relief=FLAT).grid(column=2,row=0)

        row=1
        for game in BV["GAME_LIST"][self.page*8:self.page*8+8]:
            if game in str(BG.keys()):
                currentGame = Game(self,game_name=game)
            else:
                currentGame = Game(self,game_name=game,configured=False)
            currentGame.grid(column=0,row=row,pady=(0,5),columnspan=3)
            currentGame.view_main()
            row+=1



    def triggered_nextpage_button(self):
        self.page+=1
        self.show_game()

    def triggered_previouspage_button(self):
        self.page-=1
        self.show_game()
