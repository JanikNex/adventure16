from tkinter import *
from tkinter import messagebox
from sys import exit


class GUIGame():
    def __init__(self):
        try:
            self.fenster = Toplevel()
            self.fenster.title("Lost Brother")
            self.fenster.geometry("1024x600")
            self.masterFrame = Frame(master=self.fenster, bg='black')
            self.masterFrame.place(x=0, y=0, width=1024, height=600)
            self.leftFrame = Frame(master=self.masterFrame, width=512, height=600)
            self.rightFrame = Frame(master=self.masterFrame, width=512, height=600)
            self.rightUpperFrame = Frame(master=self.rightFrame, width=512, height=150, bg='red')
            self.rightControlFrame = Frame(master=self.rightFrame, width=512, height=225, bg='yellow')
            self.rightChoiceFrame = Frame(master=self.rightFrame, width=512, height=225, bg='red')
            self.rightUpperInfoFrame = Frame(master=self.rightUpperFrame, width=512, height=75, bg='green')
            self.rightUpperInventoryFrame = Frame(master=self.rightUpperFrame, width=512, height=75, bg='pink')
            self.leftFrame.pack(side="left")
            self.rightFrame.pack(side="right")
            self.rightUpperFrame.place(x=0, y=0, width=512, height=150)
            self.rightControlFrame.place(x=0, y=151, width=512, height=225)
            self.rightChoiceFrame.place(x=0, y=376, width=512, height=225)
            self.rightUpperInfoFrame.place(x=0, y=0, width=512, height=75)
            self.rightUpperInventoryFrame.place(x=0, y=76, width=512, height=75)
            self.image = PhotoImage(file='placeholder.gif')
            self.pictureLabel = Label(master=self.leftFrame, height=150, width=512, image=self.image)
            self.pictureLabel.pack(side='top', fill='x')
            self.textOutput = Canvas(master=self.leftFrame, height=400, width=512, state="disabled", bg='#A3B1B5')
            self.textOutput.pack(side='top', fill='x')
            self.textInput = Entry(master=self.leftFrame, bg='grey', fg='white')
            self.textInput.pack(side='top', fill='x')
            self.buttonNext = Button(master=self.leftFrame, text='Weiter')
            self.buttonNext.pack(side='top', fill='x')
            self.placeLabel = Label(master=self.rightUpperInfoFrame,     font=('Arial', 16), text='Ort', bg='white')
            self.placeLabel.grid(row=0, column=0)
            self.placeOutput = Label(master=self.rightUpperInfoFrame,    font=('Arial', 16), text='irgendwo', bg='white')
            self.placeOutput.grid(row=0, column=1)
            self.prestigeLabel = Label(master=self.rightUpperInfoFrame,  font=('Arial', 16), text='Ruhm', bg='white')
            self.prestigeLabel.grid(row=1, column=0)
            self.prestigeOutput = Label(master=self.rightUpperInfoFrame, font=('Arial', 16), text='0', bg='white')
            self.prestigeOutput.grid(row=1, column=1)
            self.buttonNorth = Button(master=self.rightControlFrame, text='↑')
            self.buttonNorth.pack()
            self.buttonEast = Button(master=self.rightControlFrame, text='→')
            self.buttonEast.pack()
            self.buttonSouth = Button(master=self.rightControlFrame, text='↓')
            self.buttonSouth.pack()
            self.buttonWest = Button(master=self.rightControlFrame, text='←')
            self.buttonWest.pack()
        except:  # Kommt es beim erstellen des Startbildschrims zu einem Fehler wird das Programm mit einem Fehler geschlossen
            messagebox.showerror('Fehler', 'Ein Fehler ist aufgetreten und das Programm muss beendet werden!')
            self.fenster.quit()
            self.fenster.destroy()
            sys.exit(0)

if __name__ == '__main__':
    g = GUIGame()
    g.fenster.mainloop()