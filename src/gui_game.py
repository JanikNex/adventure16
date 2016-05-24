from tkinter import *
from tkinter import messagebox
from sys import exit


class GUIGame():
    def __init__(self, cNorth, cEast, cSouth, cWest, cMove, cLook, cNext, cAnswerA, cAnswerB, cAnswerC, cInventory):
        self.cNorth = cNorth
        self.cEast = cEast
        self.cSouth = cSouth
        self.cWest = cWest
        self.cMove = cMove
        self.cLook = cLook
        self.cNext = cNext
        self.cAnswerA = cAnswerA
        self.cAnswerB = cAnswerB
        self.cAnswerC = cAnswerC
        self.cInventory = cInventory
        try:
            # Erstellt das Spielfenster
            self.fenster = Toplevel()
            self.fenster.title("Lost Brother")
            self.fenster.geometry("1024x600")
            self.fenster.resizable(0, 0)
            #self.fenster.attributes("-topmost", 1)
            # Erstellt alle Elemente der GUI
            # MasterFrame
            self.masterFrame = Frame(master=self.fenster)
            self.masterFrame.place(x=0, y=0, width=1024, height=600)
            # LeftFrame
            self.leftFrame = Frame(master=self.masterFrame, width=512, height=600)
            # RightFrame with PArtFrames
            self.rightFrame = Frame(master=self.masterFrame, width=512, height=600)
            self.rightUpperFrame = Frame(master=self.rightFrame, width=512, height=150)
            self.rightControlFrame = LabelFrame(master=self.rightFrame, width=512, height=225, fg='black',
                                                text='Steuerung')
            self.rightChoiceFrame = LabelFrame(master=self.rightFrame, width=512, height=225, text='Antwortwahl',
                                               fg='black')
            self.rightUpperInfoFrame = LabelFrame(master=self.rightUpperFrame, width=512, height=75, fg='black',
                                                  text='Spielerinformationen')
            self.rightUpperInventoryFrame = LabelFrame(master=self.rightUpperFrame, width=512, height=75, fg='black',
                                                       text='Inventar')
            self.rightControlLookAroundFrame = LabelFrame(master=self.rightControlFrame, text='Bewegung', fg='black')
            # Positioning onscreen
            self.leftFrame.pack(side="left")
            self.leftFrame.pack_propagate(False)
            self.rightFrame.pack(side="right")
            self.rightUpperFrame.place(x=0, y=0, width=512, height=150)
            self.rightControlFrame.place(x=0, y=151, width=512, height=225)
            self.rightChoiceFrame.place(x=0, y=376, width=512, height=225)
            self.rightUpperInfoFrame.place(x=0, y=0, width=512, height=75)
            self.rightUpperInventoryFrame.place(x=0, y=76, width=512, height=75)
            self.rightControlLookAroundFrame.pack()
            # VarStrings
            self.vTextOutput = StringVar(master=self.leftFrame)
            self.vTextInput = StringVar(master=self.leftFrame)
            self.vPlaceOutput = StringVar(master=self.rightUpperInfoFrame)
            self.vPrestigeOutput = StringVar(master=self.rightUpperInfoFrame)
            # Logo laden
            self.image = PhotoImage(file='placeholder.gif')
            # Logo einfügen
            self.pictureLabel = Label(master=self.leftFrame, height=150, width=512, image=self.image)
            self.pictureLabel.pack(side='top', fill='x')
            # TextAnzeige
            self.textOutput = Label(master=self.leftFrame, height=25, width=512, bg='#A3B1B5',
                                    textvariable=self.vTextOutput, wraplength=500, justify=LEFT)
            self.textOutput.pack(side='top', fill='x')
            # Texteingabe
            self.textInput = Entry(master=self.leftFrame, bg='grey', fg='white', textvariable=self.vTextInput)
            self.textInput.pack(side='top', fill='x')
            # Weiter-Buttton
            self.buttonNext = Button(master=self.leftFrame, height=3, text='Weiter', command=self.cNext)
            self.buttonNext.pack(side='top', fill='x')
            # Infolabels
            self.placeLabel = Label(master=self.rightUpperInfoFrame, font=('fixedsys', 13), width=5, justify=RIGHT,
                                    text='Ort:', fg='black')
            self.placeLabel.grid(row=0, column=0)
            self.placeOutput = Label(master=self.rightUpperInfoFrame, font=('fixedsys', 10), width=20, justify=LEFT,
                                     textvariable=self.vPlaceOutput, fg='black')
            self.placeOutput.grid(row=0, column=1)
            self.prestigeLabel = Label(master=self.rightUpperInfoFrame, font=('fixedsys', 13), width=5, justify=LEFT,
                                       text='Ruhm:', fg='black')
            self.prestigeLabel.grid(row=1, column=0)
            self.prestigeOutput = Label(master=self.rightUpperInfoFrame, font=('fixedsys', 10), width=20, justify=RIGHT,
                                        textvariable=self.vPrestigeOutput, fg='black')
            self.prestigeOutput.grid(row=1, column=1)
            # Inventory Buttons
            self.imageNoIcon = PhotoImage(file='noItem.gif')  # 40x40
            self.buttonInventory1 = Button(master=self.rightUpperInventoryFrame, state='disabled', image=self.imageNoIcon, command= lambda: cInventory(0))
            self.buttonInventory1.pack(side='left')
            self.buttonInventory2 = Button(master=self.rightUpperInventoryFrame, state='disabled', image=self.imageNoIcon, command= lambda: cInventory(1))
            self.buttonInventory2.pack(side='left')
            self.buttonInventory3 = Button(master=self.rightUpperInventoryFrame, state='disabled', image=self.imageNoIcon, command= lambda: cInventory(2))
            self.buttonInventory3.pack(side='left')
            self.buttonInventory4 = Button(master=self.rightUpperInventoryFrame, state='disabled', image=self.imageNoIcon, command= lambda: cInventory(3))
            self.buttonInventory4.pack(side='left')
            self.buttonInventory5 = Button(master=self.rightUpperInventoryFrame, state='disabled', image=self.imageNoIcon, command= lambda: cInventory(4))
            self.buttonInventory5.pack(side='left')
            self.buttonInventory6 = Button(master=self.rightUpperInventoryFrame, state='disabled', image=self.imageNoIcon, command= lambda: cInventory(5))
            self.buttonInventory6.pack(side='left')
            self.buttonInventory7 = Button(master=self.rightUpperInventoryFrame, state='disabled', image=self.imageNoIcon, command= lambda: cInventory(6))
            self.buttonInventory7.pack(side='left')
            self.buttonInventory8 = Button(master=self.rightUpperInventoryFrame, state='disabled', image=self.imageNoIcon, command= lambda: cInventory(7))
            self.buttonInventory8.pack(side='left')
            self.buttonInventory9 = Button(master=self.rightUpperInventoryFrame, state='disabled', image=self.imageNoIcon, command= lambda: cInventory(8))
            self.buttonInventory9.pack(side='left')
            self.buttonInventory10 = Button(master=self.rightUpperInventoryFrame, state='disabled', image=self.imageNoIcon, command= lambda: cInventory(9))
            self.buttonInventory10.pack(side='left')
            self.buttonInventory11 = Button(master=self.rightUpperInventoryFrame, state='disabled', image=self.imageNoIcon, command= lambda: cInventory(10))
            self.buttonInventory11.pack(side='left')
            # Movement Buttons
            self.buttonNorth = Button(master=self.rightControlLookAroundFrame, width=15, height=2, text='↑',
                                      command=self.cNorth)
            self.buttonNorth.grid(row=0, column=1)
            self.buttonEast = Button(master=self.rightControlLookAroundFrame, width=15, height=2, text='→',
                                     command=self.cEast)
            self.buttonEast.grid(row=1, column=2)
            self.buttonSouth = Button(master=self.rightControlLookAroundFrame, width=15, height=2, text='↓',
                                      command=self.cSouth)
            self.buttonSouth.grid(row=2, column=1)
            self.buttonWest = Button(master=self.rightControlLookAroundFrame, width=15, height=2, text='←',
                                     command=self.cWest)
            self.buttonWest.grid(row=1, column=0)
            # Look Button
            self.buttonLook = Button(master=self.rightControlFrame, width=45, height=2, text='Umschauen',
                                     command=self.cLook)
            self.buttonLook.pack()
            # Move Button
            self.buttonMove = Button(master=self.rightControlLookAroundFrame, width=15, height=2, text='Bewegen',
                                     command=self.cMove)
            self.buttonMove.grid(row=1, column=1)
            # Reaction Buttons
            self.buttonAnswerA = Button(master=self.rightChoiceFrame, width=15, height=1, text='Antwort A',
                                        state='disabled', command=self.cAnswerA)
            self.buttonAnswerB = Button(master=self.rightChoiceFrame, width=15, height=1, text='Antwort B',
                                        state='disabled', command=self.cAnswerB)
            self.buttonAnswerC = Button(master=self.rightChoiceFrame, width=15, height=1, text='Antwort C',
                                        state='disabled', command=self.cAnswerC)
            self.buttonAnswerA.pack(pady=20)
            self.buttonAnswerB.pack(pady=20)
            self.buttonAnswerC.pack(pady=20)
        except:
            # Kommt es beim erstellen des Fensters zu einem Fehler wird das Programm mit einem Fehler geschlossen
            messagebox.showerror('Fehler', 'Ein Fehler ist aufgetreten und das Programm muss beendet werden!')
            self.fenster.quit()
            self.fenster.destroy()
            sys.exit(0)
