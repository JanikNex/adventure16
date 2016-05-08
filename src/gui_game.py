from tkinter import *
from tkinter import messagebox
from sys import exit


class GUIGame():
    def __init__(self):
        try:
            # Erstellt das Spielfenster
            self.fenster = Toplevel()
            self.fenster.title("Lost Brother")
            self.fenster.geometry("1024x600")
            # Erstellt alle Elemente der GUI
            self.masterFrame = Frame(master=self.fenster, bg='black')
            self.masterFrame.place(x=0, y=0, width=1024, height=600)
            self.leftFrame = Frame(master=self.masterFrame, width=512, height=600)
            self.rightFrame = Frame(master=self.masterFrame, width=512, height=600)
            self.rightUpperFrame = Frame(master=self.rightFrame, width=512, height=150, bg='red')
            self.rightControlFrame = LabelFrame(master=self.rightFrame, width=512, height=225, bg='black', fg='white', text='Steuerung')
            self.rightChoiceFrame = LabelFrame(master=self.rightFrame, width=512, height=225, bg='black', text='Antwortwahl', fg='white')
            self.rightUpperInfoFrame = LabelFrame(master=self.rightUpperFrame, width=512, height=75, bg='black', fg='white', text='Spielerinformationen')
            self.rightUpperInventoryFrame = LabelFrame(master=self.rightUpperFrame, width=512, height=75, bg='black', fg='white', text='Inventar')
            self.rightControlLookAroundFrame = LabelFrame(master=self.rightControlFrame, text='Bewegung', bg='black', fg='white')
            self.leftFrame.pack(side="left")
            self.rightFrame.pack(side="right")
            self.rightUpperFrame.place(x=0, y=0, width=512, height=150)
            self.rightControlFrame.place(x=0, y=151, width=512, height=225)
            self.rightChoiceFrame.place(x=0, y=376, width=512, height=225)
            self.rightUpperInfoFrame.place(x=0, y=0, width=512, height=75)
            self.rightUpperInventoryFrame.place(x=0, y=76, width=512, height=75)
            self.rightControlLookAroundFrame.pack()
            self.image = PhotoImage(file='placeholder.gif')
            self.pictureLabel = Label(master=self.leftFrame, height=150, width=512, image=self.image)
            self.pictureLabel.pack(side='top', fill='x')
            self.textOutput = Canvas(master=self.leftFrame, height=400, width=512, state="disabled", bg='#A3B1B5')
            self.textOutput.pack(side='top', fill='x')
            self.textInput = Entry(master=self.leftFrame, bg='grey', fg='white')
            self.textInput.pack(side='top', fill='x')
            self.buttonNext = Button(master=self.leftFrame, height=3, text='Weiter')
            self.buttonNext.pack(side='top', fill='x')
            self.placeLabel = Label(master=self.rightUpperInfoFrame,     font=('Arial', 16), text='Ort', bg='white')
            self.placeLabel.grid(row=0, column=0)
            self.placeOutput = Label(master=self.rightUpperInfoFrame,    font=('Arial', 16), text='irgendwo', bg='white')
            self.placeOutput.grid(row=0, column=1)
            self.prestigeLabel = Label(master=self.rightUpperInfoFrame,  font=('Arial', 16), text='Ruhm', bg='white')
            self.prestigeLabel.grid(row=1, column=0)
            self.prestigeOutput = Label(master=self.rightUpperInfoFrame, font=('Arial', 16), text='0', bg='white')
            self.prestigeOutput.grid(row=1, column=1)
            self.buttonNorth = Button(master=self.rightControlLookAroundFrame, width=15, height=2, text='↑')
            self.buttonNorth.grid(row=0, column=1)
            self.buttonEast = Button(master=self.rightControlLookAroundFrame, width=15, height=2, text='→')
            self.buttonEast.grid(row=1, column=2)
            self.buttonSouth = Button(master=self.rightControlLookAroundFrame, width=15, height=2, text='↓')
            self.buttonSouth.grid(row=2, column=1)
            self.buttonWest = Button(master=self.rightControlLookAroundFrame, width=15, height=2, text='←')
            self.buttonWest.grid(row=1, column=0)
            self.buttonLook = Button(master=self.rightControlFrame, width=45, height=2, text='Umschauen')
            self.buttonLook.pack()
            self.buttonMove = Button(master=self.rightControlLookAroundFrame, width=15, height=2, text='Bewegen')
            self.buttonMove.grid(row=1, column=1)
        except:  # Kommt es beim erstellen des Startbildschrims zu einem Fehler wird das Programm mit einem Fehler geschlossen
            messagebox.showerror('Fehler', 'Ein Fehler ist aufgetreten und das Programm muss beendet werden!')
            self.fenster.quit()
            self.fenster.destroy()
            sys.exit(0)

if __name__ == '__main__':
    g = GUIGame()
    g.fenster.mainloop()