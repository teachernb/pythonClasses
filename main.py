from tkinter import *
import addHero

root = Tk()

myButton = Button(root, text="Szuperhős létrehozása", padx=50, pady=50,
                  command=lambda: addHero.addHero(root), fg="red", bg="blue")

myButton.pack()

root.mainloop()
