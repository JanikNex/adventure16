from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from sys import exit


class GUIStart(object):
    def __init__(self, cGameStart, cTutorialStart, cCreditStart):
        """
        Erstellt eine neue StartMenueGui
        :param cGameStart: Callbackfunktion
        :param cTutorialStart: Callbackfunktion
        :param cCreditStart: Callbackfunktion
        """
        self.cGameStart = cGameStart
        self.cTutorialStart = cTutorialStart
        self.cCreditStart = cCreditStart
        try:
            self.fenster = Tk()
            self.fenster.title("Lost Brother - The choice is yours")
            self.fenster.geometry("600x669")
            self.fenster.wm_iconbitmap("src/icon.ico")
            # self.fenster.attributes("-topmost", 1)
            self.fenster.resizable(0, 0)
            self.logo = PhotoImage(file='src/gif/logo_withText.gif')
            self.masterFrame = Frame(master=self.fenster)
            self.masterFrame.place(x=0, y=0, width=600, height=669)
            self.picture = Label(master=self.masterFrame, image=self.logo)
            self.picture.place(x=0, y=0)
            # Button Style generieren
            self.buttonStyle = ttk.Style()
            self.buttonStyle.configure("C.TButton", foreground='#00a6ff', background='#000038',
                                       activebackground='#000038',
                                       activeforeground='#00a6ff')
            self.buttonStyle.map("C.TButton", foreground=[('pressed', '#00a6ff'), ('active', '#00a6ff'),
                                                          ('!pressed', '!active', 'black')],
                                 background=[('pressed', '!disabled', '#000038'), ('!pressed', '#000038'),
                                             ('active', '#000038'), ('disabled', '#000038')])
            # Buttons erzeugen und platzieren
            self.buttonStartGame = ttk.Button(master=self.masterFrame, text='Spiel starten', command=self.cGameStart,
                                              style='C.TButton', cursor='hand2')
            self.buttonStartGame.place(x=85, y=200)
            self.buttonTutorial = ttk.Button(master=self.masterFrame, text='Tutorial', command=self.cTutorialStart,
                                             style='C.TButton', cursor='hand2')
            self.buttonTutorial.place(x=85, y=250)
            self.buttonCredits = ttk.Button(master=self.masterFrame, text='Credits', command=self.cCreditStart,
                                            style='C.TButton', cursor='hand2')
            self.buttonCredits.place(x=85, y=450)
        except:
            # Kommt es beim erstellen des Fensters zu einem Fehler wird das Programm mit einem Fehler geschlossen
            messagebox.showerror('Fehler', 'Ein Fehler ist aufgetreten und das Programm muss beendet werden!')
            self.fenster.quit()
            self.fenster.destroy()
            sys.exit(0)
