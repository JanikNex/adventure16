from tkinter import *
from tkinter import messagebox
from sys import exit


class GUIStart():
    def __init__(self, cGameStart):
        self.cGameStart = cGameStart
        try:
            self.fenster = Tk()
            self.fenster.title("Lost Brother")
            self.fenster.geometry("600x600")
            self.logo = PhotoImage(file='lostBrother.gif')
            self.masterFrame = Frame(master=self.fenster)
            self.masterFrame.place(x=0, y=0, width=600, height=600)
            self.picture = Label(master=self.masterFrame, image=self.logo)
            self.picture.place(x=0, y=0)
            self.buttonStartGame = Button(master=self.masterFrame, text='Spiel starten', command=self.cGameStart)
            self.buttonStartGame.place(x=250, y=550)
        except:  # Kommt es beim erstellen des Startbildschrims zu einem Fehler wird das Programm mit einem Fehler geschlossen
            messagebox.showerror('Fehler', 'Ein Fehler ist aufgetreten und das Programm muss beendet werden!')
            self.fenster.quit()
            self.fenster.destroy()
            sys.exit(0)


