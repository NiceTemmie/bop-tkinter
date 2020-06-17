#!/usr/bin/python3.7
# -*-coding:Utf-8 -*
from tkinter import *
import pickle
from os import listdir
from os.path import isfile, join
import os
import ScreenManagement as SM


#VO.4  15/06/2020
#News: Page system to have more than 8game on your colection , Upgrade hud with font and logo (change some grid for game wodget)

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

BopValues={"WIDTH":1000,
            "HEIGHT":900,
            "PATH":os.path.dirname(os.path.realpath(__file__)),
            "SCREENTITLE":"Bop!",
            "COLOR_BACKGROUND":'#FFFFFF',
            "COLOR_BACKGROUND2":'#D9D9D9',
            "COLOR_MENU":'#FF914D'}

BopValues["GAMES_PATH"]=BopValues["PATH"][:-19]+"/games"
BopValues["BOPSIZE"]=str(BopValues["WIDTH"])+"x"+str(BopValues["HEIGHT"])
BopValues["GAME_LIST"]=os.listdir(BopValues["GAMES_PATH"])

BopGames=getData()[0]
gd=dict()
for k,v in BopGames.items():
    gd[str(k)]=v
BopGames=gd




if __name__ == "__main__":
    master_window=Tk()
    master_window.geometry(BopValues["BOPSIZE"])
    master_window.title(BopValues["SCREENTITLE"])
    master_window.configure(background= BopValues["COLOR_BACKGROUND"])
    master_window.resizable(False,False)

    tem = SM.NavigationMenu(master_window)
    tem.grid(column=0,row=0,sticky='ne')

    master_window.mainloop()
