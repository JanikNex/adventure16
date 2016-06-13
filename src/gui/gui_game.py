from tkinter import *
from tkinter import messagebox
import tkinter.scrolledtext as scrtxt
from sys import exit


class GUIGame(object):
    def __init__(self, cNorth, cEast, cSouth, cWest, cMove, cLook, cNext, cAnswerA, cAnswerB, cAnswerC, cInventory):
        """
        Erstellt eine neue GameGui und setzt Callbackfunktionen
        :param cNorth: Callbackfunktion
        :param cEast:  Callbackfunktion
        :param cSouth: Callbackfunktion
        :param cWest: Callbackfunktion
        :param cMove: Callbackfunktion
        :param cLook: Callbackfunktion
        :param cNext: Callbackfunktion
        :param cAnswerA: Callbackfunktion
        :param cAnswerB: Callbackfunktion
        :param cAnswerC: Callbackfunktion
        :param cInventory: Callbackfunktion
        """
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
            self.fenster.title("Lost Brother - The choice is yours")
            self.fenster.geometry("1024x600")
            self.fenster.wm_iconbitmap("src/icon.ico")
            self.fenster.resizable(0, 0)
            self.fenster.attributes("-topmost", 1)
            # Erstellt alle Elemente der GUI
            # MasterFrame
            self.masterFrame = Frame(master=self.fenster)
            self.masterFrame.place(x=0, y=0, width=1024, height=600)
            # LeftFrame
            self.leftFrame = Frame(master=self.masterFrame, width=512, height=600)
            self.leftFrameTextOutput = Frame(master=self.leftFrame, width=512, height=25, borderwidth=0)
            # RightFrame with PartFrames
            self.rightFrame = Frame(master=self.masterFrame, width=512, height=600)
            self.rightUpperFrame = Frame(master=self.rightFrame, width=512, height=150)
            self.rightControlFrame = Frame(master=self.rightFrame, width=512, height=225)
            self.rightChoiceFrame = Frame(master=self.rightFrame, width=512, height=225)
            self.rightUpperInfoFrame = Frame(master=self.rightUpperFrame, width=512, height=75)
            self.rightUpperInventoryFrame = Frame(master=self.rightUpperFrame, width=512, height=75)
            self.rightControlLookAroundFrame = Frame(master=self.rightControlFrame)
            # Positioning onscreen | LeftFrame
            self.leftFrame.pack(side="left")
            self.leftFrame.pack_propagate(False)
            # Logo laden
            self.image = PhotoImage(file='src/gif/header2.gif')
            # Logo einfügen
            self.pictureLabel = Label(master=self.leftFrame, height=150, width=512, image=self.image)
            self.pictureLabel.pack(side='top', fill='x')
            # Textoutput einfügen
            self.leftFrameTextOutput.pack(expand=YES, fill=BOTH)
            self.leftFrameTextOutput.pack_propagate(False)
            # Hintergrund laden
            self.background = PhotoImage(file='src/gif/sky_225.gif')
            self.fullBackground = PhotoImage(file='src/gif/sky.gif')
            # Hintergrundlabels platzieren
            self.masterBackground = Label(master=self.masterFrame, image=self.fullBackground)
            self.masterBackground.place(x=0, y=0, width=1024, height=600)
            self.leftFrame.lift(self.masterBackground)
            self.rightFrame.lift(self.masterBackground)
            self.backgrundLabel1 = Label(master=self.rightChoiceFrame, image=self.background)
            self.backgrundLabel1.place(x=0, y=0, width=512, height=225)
            self.backgrundLabel2 = Label(master=self.rightControlLookAroundFrame, image=self.background)
            self.backgrundLabel2.place(x=0, y=0, width=512, height=225)
            self.backgrundLabel3 = Label(master=self.rightUpperInfoFrame, image=self.background)
            self.backgrundLabel3.place(x=0, y=0, width=512, height=75)
            self.backgrundLabel4 = Label(master=self.rightControlFrame, image=self.background)
            self.backgrundLabel4.place(x=0, y=0, width=512, height=225)
            self.rightControlLookAroundFrame.lift(self.backgrundLabel4)
            self.backgrundLabel5 = Label(master=self.rightUpperInventoryFrame, image=self.background)
            self.backgrundLabel5.place(x=0, y=0, width=512, height=75)
            # Positioning onscreen | RightFrame
            self.rightFrame.pack(side="right")
            self.rightUpperFrame.place(x=0, y=0, width=512, height=150)
            self.rightControlFrame.place(x=0, y=150, width=512, height=225)
            self.rightChoiceFrame.place(x=0, y=375, width=512, height=225)
            self.rightUpperInfoFrame.place(x=0, y=2, width=512, height=75)
            self.rightUpperInventoryFrame.place(x=0, y=75, width=512, height=75)
            self.rightControlLookAroundFrame.pack()
            # VarStrings
            self.vTextInput = StringVar(master=self.leftFrame)
            self.vPlaceOutput = StringVar(master=self.rightUpperInfoFrame)
            self.vPrestigeOutput = StringVar(master=self.rightUpperInfoFrame)
            # TextAnzeige
            self.textOutput = scrtxt.ScrolledText(master=self.leftFrameTextOutput, wrap=WORD, bg='#000038',
                                                  state='disabled', cursor='arrow')
            self.textOutput.pack(fill=BOTH, expand=True)
            # Formatierungstags für die Textausgabe
            self.textOutput.tag_configure('warning', foreground='red', justify=CENTER, spacing1=2,
                                          font=("fixedsys", 12))
            self.textOutput.tag_configure('description', foreground='#00a6ff', justify=CENTER, font=("fixedsys", 12))
            self.textOutput.tag_configure('main', foreground='#00a6ff', justify=LEFT, font=("fixedsys", 12))
            self.textOutput.tag_configure('dialogue', foreground='#00a6ff', justify=RIGHT, font=("fixedsys", 12))
            self.textOutput.tag_configure('interaction', foreground='white', justify=LEFT, spacing1=2,
                                          font=("fixedsys", 12))
            self.textOutput.tag_configure('tutorial', foreground='#00a6ff', justify=CENTER, spacing1=6,
                                          font=("fixedsys", 12))
            # Texteingabe
            self.textInput = Entry(master=self.leftFrame, textvariable=self.vTextInput,
                                   cursor='pencil', fg='#00a6ff', bg='#000038', disabledbackground='#000038',
                                   disabledforeground='#00a6ff', exportselection=False, selectbackground='#000038',
                                   selectforeground='#00a6ff')
            self.textInput.pack(side='top', fill='x')
            # Weiter-Buttton
            self.buttonNext = Button(master=self.leftFrame, height=3, text='Weiter', command=self.cNext, cursor='hand2',
                                     fg='#00a6ff', bg='#000038', activebackground='#000038', activeforeground='#00a6ff')
            self.buttonNext.pack(side='top', fill='x')
            # Infolabels
            self.placeLabel = Label(master=self.rightUpperInfoFrame, font=('fixedsys', 13), width=5, justify=RIGHT,
                                    text='Ort:', fg='#00a6ff', bg='#000038')
            self.placeLabel.grid(row=0, column=0)
            self.placeOutput = Label(master=self.rightUpperInfoFrame, font=('fixedsys', 10), width=25, justify=LEFT,
                                     textvariable=self.vPlaceOutput, fg='#00a6ff', bg='#000038')
            self.placeOutput.grid(row=0, column=1)
            self.prestigeLabel = Label(master=self.rightUpperInfoFrame, font=('fixedsys', 13), width=5, justify=LEFT,
                                       text='Ruhm:', fg='#00a6ff', bg='#000038')
            self.prestigeLabel.grid(row=1, column=0)
            self.prestigeOutput = Label(master=self.rightUpperInfoFrame, font=('fixedsys', 10), width=5, justify=RIGHT,
                                        textvariable=self.vPrestigeOutput, fg='#00a6ff', bg='#000038')
            self.prestigeOutput.grid(row=1, column=1)
            # Inventory Buttons
            self.imageNoIcon = PhotoImage(file='src/gif/noItem.gif')  # 40x40
            self.buttonInventory1 = Button(master=self.rightUpperInventoryFrame, state='disabled',
                                           image=self.imageNoIcon, command=lambda: cInventory(0))
            self.buttonInventory1.pack(side='left')
            self.buttonInventory2 = Button(master=self.rightUpperInventoryFrame, state='disabled',
                                           image=self.imageNoIcon, command=lambda: cInventory(1))
            self.buttonInventory2.pack(side='left')
            self.buttonInventory3 = Button(master=self.rightUpperInventoryFrame, state='disabled',
                                           image=self.imageNoIcon, command=lambda: cInventory(2))
            self.buttonInventory3.pack(side='left')
            self.buttonInventory4 = Button(master=self.rightUpperInventoryFrame, state='disabled',
                                           image=self.imageNoIcon, command=lambda: cInventory(3))
            self.buttonInventory4.pack(side='left')
            self.buttonInventory5 = Button(master=self.rightUpperInventoryFrame, state='disabled',
                                           image=self.imageNoIcon, command=lambda: cInventory(4))
            self.buttonInventory5.pack(side='left')
            self.buttonInventory6 = Button(master=self.rightUpperInventoryFrame, state='disabled',
                                           image=self.imageNoIcon, command=lambda: cInventory(5))
            self.buttonInventory6.pack(side='left')
            self.buttonInventory7 = Button(master=self.rightUpperInventoryFrame, state='disabled',
                                           image=self.imageNoIcon, command=lambda: cInventory(6))
            self.buttonInventory7.pack(side='left')
            self.buttonInventory8 = Button(master=self.rightUpperInventoryFrame, state='disabled',
                                           image=self.imageNoIcon, command=lambda: cInventory(7))
            self.buttonInventory8.pack(side='left')
            self.buttonInventory9 = Button(master=self.rightUpperInventoryFrame, state='disabled',
                                           image=self.imageNoIcon, command=lambda: cInventory(8))
            self.buttonInventory9.pack(side='left')
            self.buttonInventory10 = Button(master=self.rightUpperInventoryFrame, state='disabled',
                                            image=self.imageNoIcon, command=lambda: cInventory(9))
            self.buttonInventory10.pack(side='left')
            self.buttonInventory11 = Button(master=self.rightUpperInventoryFrame, state='disabled',
                                            image=self.imageNoIcon, command=lambda: cInventory(10))
            self.buttonInventory11.pack(side='left')
            # Movement Buttons
            self.buttonNorth = Button(master=self.rightControlLookAroundFrame, width=15, height=2, text='↑',
                                      command=self.cNorth, fg='#00a6ff', bg='#000038', activebackground='#000038',
                                      activeforeground='#00a6ff')
            self.buttonNorth.grid(row=0, column=1)
            self.buttonEast = Button(master=self.rightControlLookAroundFrame, width=15, height=2, text='→',
                                     command=self.cEast, fg='#00a6ff', bg='#000038', activebackground='#000038',
                                     activeforeground='#00a6ff')
            self.buttonEast.grid(row=1, column=2)
            self.buttonSouth = Button(master=self.rightControlLookAroundFrame, width=15, height=2, text='↓',
                                      command=self.cSouth, fg='#00a6ff', bg='#000038', activebackground='#000038',
                                      activeforeground='#00a6ff')
            self.buttonSouth.grid(row=2, column=1)
            self.buttonWest = Button(master=self.rightControlLookAroundFrame, width=15, height=2, text='←',
                                     command=self.cWest, fg='#00a6ff', bg='#000038', activebackground='#000038',
                                     activeforeground='#00a6ff')
            self.buttonWest.grid(row=1, column=0)
            # Look Button
            self.buttonLook = Button(master=self.rightControlFrame, width=45, height=2, text='Umschauen',
                                     command=self.cLook, fg='#00a6ff', bg='#000038', activebackground='#000038',
                                     activeforeground='#00a6ff')
            self.buttonLook.pack()
            # Move Button
            self.buttonMove = Button(master=self.rightControlLookAroundFrame, width=15, height=2, text='Bewegen',
                                     command=self.cMove, fg='#00a6ff', bg='#000038', activebackground='#000038',
                                     activeforeground='#00a6ff')
            self.buttonMove.grid(row=1, column=1)
            # Reaction Buttons
            self.buttonAnswerA = Button(master=self.rightChoiceFrame, width=15, height=1, text='Antwort A',
                                        state='disabled', command=self.cAnswerA, fg='#00a6ff', bg='#000038',
                                        activebackground='#000038', activeforeground='#00a6ff')
            self.buttonAnswerB = Button(master=self.rightChoiceFrame, width=15, height=1, text='Antwort B',
                                        state='disabled', command=self.cAnswerB, fg='#00a6ff', bg='#000038',
                                        activebackground='#000038', activeforeground='#00a6ff')
            self.buttonAnswerC = Button(master=self.rightChoiceFrame, width=15, height=1, text='Antwort C',
                                        state='disabled', command=self.cAnswerC, fg='#00a6ff', bg='#000038',
                                        activebackground='#000038', activeforeground='#00a6ff')
            self.buttonAnswerA.pack(pady=20)
            self.buttonAnswerB.pack(pady=20)
            self.buttonAnswerC.pack(pady=20)
        except:
            # Kommt es beim erstellen des Fensters zu einem Fehler wird das Programm mit einem Fehler geschlossen
            messagebox.showerror('Fehler', 'Ein Fehler ist aufgetreten und das Programm muss beendet werden!')
            self.fenster.quit()
            self.fenster.destroy()
            sys.exit(0)
