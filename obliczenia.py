from math import *
from tkinter import *
def wynik(prawe, lewe, czestotliwosci):
    print("Ziobro",prawe,lewe)

    if (fabs(prawe[2]-prawe[5]) > 40 and prawe[7] < prawe[5]):
        utrataP = (prawe[2]+prawe[3]+prawe[5]+prawe[7])/4
    elif (fabs(prawe[2]-prawe[5]) > 40):
        utrataP = (prawe[2]+prawe[3]+prawe[7])/3
    else:
        utrataP = (prawe[2]+prawe[3]+prawe[5])/3

    if (fabs(lewe[2]-lewe[5]) > 40 and lewe[7] < lewe[5]):
        utrataL = (lewe[2]+lewe[3]+lewe[5]+lewe[7])/4
    elif (fabs(lewe[2]-lewe[5]) > 40):
        utrataL = (lewe[2]+lewe[3]+lewe[7])/3
    else:
        utrataL = (lewe[2]+lewe[3]+lewe[5])/3

    if (fabs(utrataP - utrataL) > 25):
        if (utrataL > utrataP):
            utrata = utrataP + 5
        else:
            utrata = utrataL + 5
    else:
        if (utrataL > utrataP):
            utrata = utrataP
        else:
            utrata = utrataL
    #print(utrata)
    if (utrata < 20):
        opinia = "norma"
    elif (20<=utrata<40):
        opinia = "lekkie uszkodzenie słuchu"
    elif (40<=utrata<70):
        opinia = "umiarkowane uszkodzenie słuchu"
    elif (70<=utrata<90):
        opinia = "znaczne uszkodzenie słuchu"
    elif (90<=utrata<120):
        opinia = "głębokie uszkodzenie słuchu"
    else:
        opinia = "całkowita głuchota"

    root3 = Tk()
    root3.title("Wynik")
    root3.geometry("250x60")
    app3 = Frame(root3)
    app3.grid()
    
    napis = "WYNIK: \n"+str(int(utrata))+" dB\n"+opinia
    
    lbl = Label(app3, text = napis)
    lbl.grid(row = 0, column = 0, sticky = W)
    root3.mainloop()    
    
