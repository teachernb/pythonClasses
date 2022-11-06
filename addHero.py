from Superhero import Szuperhos
from tkinter import *


def addHero(root):
    s = Szuperhos("Thor", 70)
    createhHeroLbl = Label(root, text=s.nev + " " + str(s.szuperero))
    createhHeroLbl.pack()
