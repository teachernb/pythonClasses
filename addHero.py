from Superhero import Szuperhos
from tkinter import *

def addHero(root):
    #s változó ->példányosítok, létrehozok egy szuperhőst Thor névvel és 70 erőponntal
    s = Szuperhos("Thor", 70)
    benedeké = Szuperhos("KKK", 30)
    somahosealegjobb = Szuperhos("UwU", 9999999999999999)
    createhHeroLbl = Label(root, text=s.nev + " " + str(s.szuperero))
    createhHeroLbl.pack()
