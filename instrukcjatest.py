from tkinter import *
def instrtest():
    root5 = Tk()
    root5.title("Wynik")
    root5.geometry("360x130")
    app5 = Frame(root5)
    app5.grid()
    
    napis = "KOŃCOWY WYNIK WYŚWIETLA SIĘ PO ZAMKNIĘCIU WYKRESU\nZalecane jest założenie słuchawek.\nPo wciśnięciu przycisku \"Test\", nadany zostanie\nsygnał o różnych parametrach częstotliwości oraz decybeli.\nTwoim zadaniem jest naciśnięcie przycisku Tak jeżeli usłyszysz\ndźwięk lub Nie, jeśli go nie usłyszysz. Test zostanie przeprowadzony\noddzielnie dla obu uszu. Na podstawie twoich odpowiedzi program\nwyznaczy dwa audiogramy określające twój ubytek słuchu."
    
    lbl = Label(app5, text = napis)
    lbl.grid(row = 0, column = 0, sticky = W)
    root5.mainloop()
