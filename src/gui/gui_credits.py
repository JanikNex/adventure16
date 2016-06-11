from tkinter import *
from tkinter import messagebox
from sys import exit


class GUICredits(object):
    def __init__(self):
        """
        Erstellt eine neue CreditGui
        """
        try:
            self.fenster = Toplevel()
            self.fenster.title("Lost Brother - The choice is yours")
            self.fenster.geometry("600x652")
            self.fenster.wm_iconbitmap("src/icon.ico")
            self.fenster.resizable(0, 0)
            self.fenster.attributes("-topmost", 1)
            self.background = PhotoImage(file='src/gif/logo_noText.gif')
            self.masterFrame = Frame(master=self.fenster)
            self.masterFrame.place(x=0, y=0, width=600, height=652)
            self.title = StringVar()
            self.title.set("Lost Brother")
            self.description = StringVar()
            self.description.set("The choice is yours")
            self.picture = Label(master=self.masterFrame, image=self.background, width=600, height=652)
            self.picture.place(x=0, y=0)
            self.titleLabel = Label(master=self.masterFrame, textvariable=self.title, fg='#00a6ff', bg='#707070', font="fixedsys 36 bold")
            self.descriptionLabel = Label(master=self.masterFrame, textvariable=self.description, fg='#00a6ff', bg='#707070',
                                          font="fixedsys 26 bold")
            self.exitTextLabel = Label(master=self.masterFrame, text='Drücke "Enter" zum überspringen!', fg='#00a6ff', bg='#707070',
                                       font="fixedsys 10 bold italic")
            self.titleLabel.place(y=150, x=300, anchor=CENTER)
            self.descriptionLabel.place(y=360, x=300, anchor=CENTER)
            self.exitTextLabel.place(y=620, x=300, anchor=CENTER)
        except:
            # Kommt es beim erstellen des Fensters zu einem Fehler wird das Programm mit einem Fehler geschlossen
            messagebox.showerror('Fehler', 'Ein Fehler ist aufgetreten und das Programm muss beendet werden!')
            self.fenster.quit()
            self.fenster.destroy()
            sys.exit(0)
