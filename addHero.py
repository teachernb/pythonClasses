from Superhero import Szuperhos
from tkinter import *

def addHero(root):
    #s változó ->példányosítok, létrehozok egy szuperhőst Thor névvel és 70 erőponntal
    s = Szuperhos("Thor", 70)
    benedeke = Szuperhos("KKK", 40)
    zalanhose = Szuperhos("Goku", 9001)
    dominikHose = Szuperhos("RHN", 1235)
    david_hose = Szuperhos("😎", -1)
    s1 = Szuperhos("NB", "Infinity")
    veghdavidbelapatrik = Szuperhos("Kazuma", 9001)
    eszterhose = Szuperhos("Hősneve", 45)
    k = Szuperhos("Supermodell", 1000)
    adamhose = Szuperhos("Jamal", 1)
    g = Szuperhos("PepsiMan", 5999999999)
    bazsi_hos = Szuperhos("Lö Csó", 99999999999999999)
    
    createhHeroLbl = Label(root, text=s.nev + " " + str(s.szuperero))
    createhHeroLbl.pack()
