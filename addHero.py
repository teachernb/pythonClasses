from Superhero import Szuperhos
from tkinter import *

def addHero(root):
    #s változó ->példányosítok, létrehozok egy szuperhőst Thor névvel és 70 erőponntal
    s = Szuperhos("Thor", 70)
    benedeke = Szuperhos("KKK", 40000)
    createhHeroLbl = Label(root, text=s.nev + " " + str(s.szuperero))
    createhHeroLbl.pack()
