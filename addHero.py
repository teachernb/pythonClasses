from Superhero import Szuperhos
from tkinter import *

def addHero(root):
    #s változó ->példányosítok, létrehozok egy szuperhőst Thor névvel és 70 erőponntal
    somahosealegjobb = Szuperhos("UwU", 9999999999999999)
    createhHeroLbl = Label(root, text=somahosealegjobb.nev + " " + str(somahosealegjobb.szuperero))
    createhHeroLbl.pack()
