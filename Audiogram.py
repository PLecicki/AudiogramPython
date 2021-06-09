#moduł wbudowany
from tkinter import *
#własne moduły
import kalibracja
import testowaniesluchu
import instrukcjatest

class Application(Frame):
    """ Interfejs graficzny """
    def __init__(self, master):
        """ Inicjalizacja ramki """
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()
    def create_widgets(self):
        """ Utworzenie widgetow """
        self.tytul = Label(self, text="AUDIOGRAM")
        self.tytul.grid(row = 0, column = 0, sticky = W)

        self.tytul1 = Label(self, text="Autorzy:")
        self.tytul1.grid(row = 1, column = 0, columnspan = 2, sticky = W)

        self.tytul2 = Label(self, text="Piotr Łęcicki (back-end)")
        self.tytul2.grid(row = 2, column = 0, columnspan = 2, sticky = W)

        self.tytul2 = Label(self, text="Emil Rybaczewski-Jlassi (front-end)")
        self.tytul2.grid(row = 3, column = 0, columnspan = 2, sticky = W)

        self.tytul2 = Label(self, text="WEL18EC1S1")
        self.tytul2.grid(row = 4, column = 0, columnspan = 2, sticky = W)
        
        self.bttn = Button(self)
        self.bttn["text"]= "Kalibracja"
        self.bttn["command"] = self.startkalibracja
        self.bttn.grid(row = 1, column = 3, sticky = E)

        self.bttn1 = Button(self)
        self.bttn1["text"]= "Instrukcja kalibracji"
        self.bttn1["command"] = self.instrukcjakalibracja
        self.bttn1.grid(row = 0, column = 3, sticky = E)

        self.bttn2 = Button(self)
        self.bttn2["text"]= "Instrukcja do testu słuchu"
        self.bttn2["command"] = self.instrukcjatest
        self.bttn2.grid(row = 6, column = 0, sticky = W)

        self.bttn3 = Button(self)
        self.bttn3["text"]= "Test"
        self.bttn3["command"] = self.test
        self.bttn3["width"] = "19"
        self.bttn3["bg"] = "green"
        self.bttn3["fg"] = "white"
        self.bttn3.grid(row = 7, column = 0, sticky = W)
    def startkalibracja(self):
        kalibracja.kalibr()
    def instrukcjakalibracja(self):
        kalibracja.instrkalibr()
    def instrukcjatest(self):
        instrukcjatest.instrtest()
    def test(self):
        testowaniesluchu.start()
        
        

root = Tk()
root.title("Audiogram")
root.geometry("305x200")

app = Application(root)

root.mainloop()
        

