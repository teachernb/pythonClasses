from Superhero import Szuperhos
from tkinter import *

def addHero(root):
    #s változó ->példányosítok, létrehozok egy szuperhőst Thor névvel és 70 erőponntal
    s = Szuperhos("Thor", 70)
    david_hose = Szuperhos("😎", -1)
    somahosealegjobb = Szuperhos("UwU", 9999999999999999)
    veghdavidbelapatrik = Szuperhos("Kazuma", 9001)
    k = Szuperhos("Supermodell", 1000)
    createhHeroLbl = Label(root, text=s.nev + " " + str(s.szuperero))
    createhHeroLbl.pack()
