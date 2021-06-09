import pygame
import time
from tkinter import *
def kalibr():
    pygame.mixer.pre_init(frequency=44100, size=-16, channels=1, buffer=512)
    pygame.mixer.init()
    sound1=pygame.mixer.Sound("1kHz_44100Hz_16bit_05sec.wav")
    for i in range(5):
        sound1.set_volume(1.0)
        print (sound1.get_volume())
        sound1.play()
        time.sleep(1)
        sound1.stop()
        sound1.set_volume(0.316)
        print (sound1.get_volume())
        sound1.play()
        time.sleep(1)
        sound1.stop()
def instrkalibr():
    root1 = Tk()
    root1.title("Instrukcja kalibracji")
    root1.geometry("425x60")
    app1 = Frame(root1)
    app1.grid()
    lbl = Label(app1, text = "INSTRUKCJA KALIBRACJI\nPo wciśnięciu przycisku \"Kalibracja\" usłyszysz dwa dźwięki o różnej głośności.\nNależy ustawić poziom głośności urządzenia, aby nie słyszeć cichszego dźwięku") 
    lbl.grid(row = 0, column = 0, sticky = W, columnspan = 3)
    root1.mainloop()



