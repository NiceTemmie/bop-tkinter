#!/usr/bin/python3.7
# -*-coding:Utf-8 -*
from tkinter import *
from tkinter import filedialog
from bop import BopValues as BV
from bop import BopGames as BG
from bop import saveData
from tkinter.font import Font
import os
from threading import Thread

class Game (Frame):

    def __init__(self,master=None,game_name='', configured=True):
        super().__init__(master,width=BV["WIDTH"]*3/4,height=BV["HEIGHT"]/9, background=BV["COLOR_BACKGROUND"])
        self.font_game_title = Font(family="ArchivoBlack",size=20)
        self.font_configured = Font(family="Open sans light",size=16)
        self.game_name=game_name
        self.configured=configured
        self.grid_propagate(0)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

    def view_destroy(self):
        for widget in self.winfo_children():
            widget.destroy()
        self.debug("All widgets deleted")

    def view_main(self):
        self.columnconfigure(4, weight=0)

        self.debug("main view ?")
        Button(self,text="Manage",command=self.triggered_manage_button,background=BV["COLOR_BACKGROUND"],relief=FLAT).grid(column=2,row=1) #Manage button
        Button(self,text="Play",command=self.triggered_play_button,background=BV["COLOR_BACKGROUND"],relief=FLAT).grid(column=0,row=1,sticky="W") #Play button
        if self.configured: #IF the game has already been configured
            Label(self,text=BG[self.game_name][0],background=BV["COLOR_BACKGROUND"],font=self.font_game_title).grid(column=0,row=0,sticky="WN")#Name of the game give by the user
            Label(self,text='OK',foreground='green',background=BV["COLOR_BACKGROUND"],font=self.font_configured).grid(column=0,row=0,sticky=N) #Juste a green OK lol
            self.debug("configuré")
        else: #IF it's the first time
            Label(self,text=self.game_name,background=BV["COLOR_BACKGROUND"],font=self.font_game_title).grid(column=0,row=0,sticky="WN") #The original name of the file
            Label(self,text='Configuration requiered',foreground='red',background=BV["COLOR_BACKGROUND"],font=self.font_configured).grid(column=0,row=0,sticky=N)
            self.debug("non configuré")
        self.debug("main view !")

    def view_config(self):
        self.columnconfigure(4, weight=1)

        Label(self,text="Main files directory" ,background=BV["COLOR_BACKGROUND"]).grid(row=0,column=4,sticky=W+E,columnspan=3)
        Label(self,text="Title of the game",background=BV["COLOR_BACKGROUND"]).grid(row=0,column=0,sticky=W+E,columnspan=3)
        Button(self,text='Save', command=self.triggered_save_button,background=BV["COLOR_BACKGROUND"]).grid(row=2,column=1)
        Button(self,text='Back', command=self.triggered_back_button,background=BV["COLOR_BACKGROUND"]).grid(row=2,column=0)
        Button(self,text='Delete', command=self.triggered_deletedata_button,background=BV["COLOR_BACKGROUND"]).grid(row=2,column=4)
        Button(self,text='Browse',command=self.triggered_fileBrowser,background=BV["COLOR_BACKGROUND"]).grid(row=1,column=6)
        self.entry_command=Entry(self,background=BV["COLOR_BACKGROUND"])
        self.entry_game_title=Entry(self,background=BV["COLOR_BACKGROUND"])

        self.wine=IntVar()
        self.checkbox_wine = Checkbutton(self, text="Wine",variable=self.wine,background=BV["COLOR_BACKGROUND"],relief='flat')
        self.checkbox_wine.deselect() #Would be reselect only if it already was (just mor quick that make many if else)
        if self.configured:
            self.entry_game_title.insert(0,BG[self.game_name][0])
            self.entry_command.insert(0,BG[self.game_name][1])
            if BG[self.game_name][2]:
                self.checkbox_wine.select()
        else:
            self.entry_game_title.insert(0,self.game_name)

        #Grid must be done after .insert() cause when grid it becone a none type
        self.entry_game_title.grid(row=1,column=0,sticky=W+E,columnspan=3)
        self.entry_command.grid(row=1,column=4,columnspan=2 ,sticky=W+E)
        self.checkbox_wine.grid(row=2,column=5)

    def triggered_manage_button(self):
        self.view_destroy()
        self.view_config()

    def triggered_play_button(self):
        try:
            if BG[self.game_name][2]:
                cmd = "wine " + str(BG[self.game_name][1])
            else:
                cmd = BG[self.game_name][1]
            self.debug("bash command execute >>> '%s'"%cmd)
            os.system(cmd)
        except KeyError:
            self.debug("cannot execute without configuration")

    def triggered_back_button(self):
        self.view_destroy()
        self.view_main()

    def triggered_save_button(self):
        if self.entry_command.get()!="":
            self.configured=True
            if self.wine.get() == 1:
                w=True
            else:
                w=False

            BG[self.game_name]=(self.entry_game_title.get(),self.entry_command.get(),w)
            saveData(BG)

            self.view_destroy()
            self.view_main()


    def triggered_deletedata_button(self):
        try:
            del BG[self.game_name]
            self.configured=False
            saveData(BG)
            print("Data deleted")
            self.view_destroy()
            self.view_main()
        except KeyError:
            pass

        self.view_destroy()
        self.view_main()

    def triggered_fileBrowser(self):
        self.filename = filedialog.askopenfilename(initialdir="{}/{}".format(BV["GAMES_PATH"],self.game_name), title = "Select Main File")
        self.entry_command.insert(0,"'%s'"%self.filename)

    def debug(self,txt=''):
        print("["+str(self.game_name)+"]: "+str(txt))

class loading_time(Tk):

    def __init__(self,text='loading...'):
        self.root= Tk()
        self.root.geometry('300x200')
        self.root.overrideredirect(1)
        self.root.configure(background=BV["COLOR_MENU"])
        self.root.columnconfigure(0,weight=1)
        self.root.rowconfigure(0,weight=1)

        self.font = Font(family="Open sans extra bold",size=19)
        Label(self.root,text=text,foreground=BV["COLOR_BACKGROUND"],background=BV["COLOR_MENU"],font=self.font).grid(row=0,column=0)

        positionRight = int(self.root.winfo_screenwidth()/2 - self.root.winfo_reqwidth()/2)
        positionDown = int(self.root.winfo_screenheight()/2 - self.root.winfo_reqheight()/2)
        self.root.geometry("+{}+{}".format(positionRight, positionDown))

        self.root.update()

    def end(self):
        self.root.destroy()

class NavigationMenu_label(Label):

    position=1

    def __init__(self,master=None,command=None,name='text'):
        self.font = Font(family="ArchivoBlack",size=18)
        super().__init__(master,text=name,background=BV["COLOR_MENU"],foreground=BV["COLOR_BACKGROUND"],font=self.font)
        self.grid(row=NavigationMenu_label.position,column=0)
        self.bind("<Button-1>",command)
        NavigationMenu_label.position+=1
