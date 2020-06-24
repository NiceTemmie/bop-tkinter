#!/usr/bin/python3.7
# -*-coding:Utf-8 -*
from tkinter import *
import pickle
from os import listdir
from os.path import isfile, join
import os
import ScreenManagement as SM

#----------------------------------------------------------------------------------------------------------

def saveData(*x): #Ecrire avec Pickle
    with open(os.path.join(BopValues["PATH"], 'gamesdata'),'wb') as file: #on écrit
        pikl=pickle.Pickler(file)
        pikl.dump(x)

def getData(): #lire avec pickle
    with open(os.path.join(BopValues["PATH"], 'gamesdata'),"rb") as file:
        pikl=pickle.Unpickler(file)
        data=pikl.load()
        return data #on retourne le résultat"""

#-----------------------------------------------------------------------------------------------------------
givemevalue=Tk()
BopValues={"WIDTH":givemevalue.winfo_screenwidth(),
            "HEIGHT":givemevalue.winfo_screenheight(),
            "PATH":os.path.dirname(os.path.realpath(__file__)),
            "SCREENTITLE":"Bop!",
            "COLOR_BACKGROUND":'#FFFFFF',
            "COLOR_BACKGROUND2":'#D9D9D9',
            "COLOR_MENU":'#FF914D'}

BopValues["GAMES_PATH"]=BopValues["PATH"][:-19]+"/games"
BopValues["BOPSIZE"]=str(BopValues["WIDTH"])+"x"+str(BopValues["HEIGHT"])
BopValues["GAME_LIST"]=os.listdir(BopValues["GAMES_PATH"])

givemevalue.destroy()
del givemevalue

BopGames=getData()[0]
gd=dict()
for k,v in BopGames.items():
    gd[str(k)]=v
BopGames=gd

if __name__ == "__main__":
    from widgets import loading_time

    #Try to update from Github. Just a bonus
    load=loading_time(text="Waiting for Github...")
    try:
        os.system("bash '%s/github.sh'"%BopValues["PATH"])
    except :
        print("Unable to connect to github")
    load.end()

    master_window=Tk()
    master_window.overrideredirect(True)
    master_window.geometry(BopValues["BOPSIZE"])
    master_window.title(BopValues["SCREENTITLE"])
    master_window.configure(background= BopValues["COLOR_BACKGROUND"])
    master_window.resizable(False,False)

    tem = SM.NavigationMenu(master_window)
    tem.grid(column=0,row=0,sticky='ne')

    master_window.mainloop()
