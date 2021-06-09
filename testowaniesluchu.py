from tkinter import *
from pygame import *
import matplotlib.pyplot as plt
import obliczenia

class Test(Frame):
    def __init__(self, master):
        """ Inicjalizacja ramki """
        super(Test, self).__init__(master)
        self.grid()
        self.create_widgets()
    def create_widgets(self):
        self.czest = (125, 250, 500, 1000, 1500, 2000, 3000, 4000, 6000, 8000, 10000)
        self.c = 0
        self.wzmo = (0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100)
        self.w = 0
        self.uszy = ("prawe","lewe")
        self.u = 0
        self.glosnosc = 1.0
        mixer.init(frequency=44000, size=-16,channels=2, buffer=4096)
        self.sygnal = (mixer.Sound('dzwieki/125Hz.wav'),
                       mixer.Sound('dzwieki/250Hz.wav'),
                       mixer.Sound('dzwieki/500Hz.wav'),
                       mixer.Sound('dzwieki/1000Hz.wav'),
                       mixer.Sound('dzwieki/1500Hz.wav'),
                       mixer.Sound('dzwieki/2000Hz.wav'),
                       mixer.Sound('dzwieki/3000Hz.wav'),
                       mixer.Sound('dzwieki/4000Hz.wav'),
                       mixer.Sound('dzwieki/6000Hz.wav'),
                       mixer.Sound('dzwieki/8000Hz.wav'),
                       mixer.Sound('dzwieki/10000Hz.wav'))
        
        tytul = Label(self, text="Uruchom i zaznacz, czy słyszysz dźwięk?")
        tytul.grid(row = 0, column = 0, columnspan = 2, sticky = W)
        tytul1 = Label(self, text=str(self.czest[self.c])+" Hz, ubytek dźwięku "+str(self.wzmo[self.w])+"%, ucho "+self.uszy[self.u])
        tytul1.grid(row = 1, column = 0, columnspan = 2, sticky = W)

        tak = Button(self)
        tak["text"] = "Tak"
        tak["width"] = "6"
        tak["command"] = self.optak
        tak.grid(row=2, column=0, sticky=W)

        nie = Button(self)
        nie["text"] = "Nie"
        nie["width"] = "6"
        nie["command"] = self.opnie
        nie.grid(row=2, column=1, sticky=E)

        begin = Button(self)
        begin["text"] = "Uruchom\ndźwięk"
        begin["command"] = self.start
        begin.grid(row=0, column=3, rowspan=2, sticky=W)

        self.praweucho=[0,0,0,0,0,0,0,0,0,0,0]
        self.leweucho=[0,0,0,0,0,0,0,0,0,0,0]


        
    def optak(self):
        if (self.w<10):
            self.glosnosc -= 0.1
            self.w+=1            
        elif (self.w>=10):
            if (self.czest[self.c]==10000):
                if (self.u==0):
                    self.praweucho[self.c]=self.w
                    self.u=1
                    self.w=0
                    self.glosnosc = 1.0
                    self.c=0
                elif (self.u==1):
                    self.leweucho[self.c]=self.w
                    self.wykres()
            else:
                if (self.u==0):
                    self.praweucho[self.c]=self.w
                else:
                    self.leweucho[self.c]=self.w
                self.glosnosc = 1.0
                self.c+=1
                self.w=0
                
        tytul1 = Label(self, text=str(self.czest[self.c])+" Hz, ubytek dźwięku "+str(self.wzmo[self.w])+"%, ucho "+self.uszy[self.u])
        tytul1.grid(row = 1, column = 0, columnspan = 2, sticky = W)
        #print(self.praweucho)
        #print(self.leweucho)
        
    def opnie(self):
        if (self.czest[self.c]==10000 and self.c==10):
            if (self.u==0):
                self.praweucho[self.c]=self.w
                self.u=1
                self.w=0
                self.glosnosc = 1.0
                self.c=0
            elif (self.u==1):
                self.leweucho[self.c]=self.w
                self.wykres()
        else:
            if (self.u==0):
                self.praweucho[self.c]=self.w
            else:
                self.leweucho[self.c]=self.w
            self.glosnosc = 1.0
            self.c+=1
            self.w=0

        tytul1 = Label(self, text=str(self.czest[self.c])+" Hz, ubytek dźwięku "+str(self.wzmo[self.w])+"%, ucho "+self.uszy[self.u])
        tytul1.grid(row = 1, column = 0, columnspan = 2, sticky = W)
        #print(self.praweucho)
        #print(self.leweucho)
        
    def start(self):        
        channel0 = mixer.Channel(0)
        channel0.play(self.sygnal[self.c])
        if (self.u==0):
            channel0.set_volume(0.0, self.glosnosc)
        elif (self.u==1):
            channel0.set_volume(self.glosnosc, 0.0)

    def wykres(self):
        #self.praweucho
        #self.leweucho
        for i in range(11):
            self.praweucho[i] = int((1 - self.praweucho[i]/10)*100)
            self.leweucho[i] = int((1 - self.leweucho[i]/10)*100)
        plt.plot(self.czest, self.praweucho, 'r--', self.czest, self.leweucho, 'b--')
        plt.xlabel('Częstotliwość Hz')
        plt.ylabel('Ubytek słuchu dB')
        plt.title('Audiogram')
        plt.xlim([125, 10000])
        plt.ylim([130, 0])
        # plt.xticks([500,1000,2000,3000,4000,6000,8000,10000])
        # plt.yticks([ 0, 10, 30, 50, 60, 80, 90, 110, 130])
        plt.show()
        obliczenia.wynik(self.praweucho,self.leweucho,self.czest)
def start():
    root2 = Tk()
    root2.title("Test")
    root2.geometry("300x70")
    app2 = Test(root2)
    root2.mainloop()


    

