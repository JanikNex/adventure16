from src.gui.gui_game import *
from src.gameclasses.cgame import *


class GameController(object):
    def __init__(self):
        # Neues Game-Objekt
        self.game = Game()
        # Neues GUI-Objekt
        self.gui = GUIGame(self.buttonLookNorth, self.buttonLookEast, self.buttonLookSouth, self.buttonLookWest,
                           self.buttonMove, self.buttonLook, self.buttonNext, self.buttonAnswerA,
                           self.buttonAnswerB, self.buttonAnswerC, self.buttonInventory)
        # Registrierung des WindowClose Event-Handlers
        self.gui.fenster.protocol("WM_DELETE_WINDOW", self.windowCloseEvent)
        # Registrierung der Keyboard-Binds
        self.gui.fenster.bind("<Return>", lambda e: self.buttonNext())
        # Bilder initialisieren
        self.ImageNoItem = PhotoImage(file='src/gif/noItem.gif')
        self.ImageInventorySlot = [None, None, None, None, None, None, None, None, None, None, None]
        # Button Array initialisieren
        self.ButtonText = []
        self.AnswerButtonsActive = False
        # GUI an Spielstart anpassen
        self.updateGUI()
        # Einmal umschauen um den Spieleinstieg zu erleichtern
        self.buttonLook()
        # Aktivierung des Fensters
        self.gui.fenster.mainloop()

    def windowCloseEvent(self):
        """
        Wird aufgerufen, sobald versucht wird das Fenster zu schließen. Es erscheint eine Messagebox und mit klick auf
        ok wird das Fenster geschlossen
        """
        if messagebox.askokcancel("Beenden",
                                  "Möchtest du das Spiel wirklich beenden? \nDein Spielstand wird dabei unwiederruflich gelöscht!"):
            self.gui.fenster.quit()
            self.gui.fenster.destroy()

    def buttonLookNorth(self):
        """
        Setzt die Blickrichtung des Spielers richtung Norden und gibt die Beschreibung des Ortes aus
        """
        if not self.game.getPlayer().isInteracting():
            self.game.getPlayer().setFacing('n')
            self.textOutputDesciption(self.game.getPlayer().getPlace().getPlaceInDirection(0).getFarsightDescription())
            self.updateGUI()

    def buttonLookEast(self):
        """
        Setzt die Blickrichtung des Spielers richtung Osten und gibt die Beschreibung des Ortes aus
        """
        if not self.game.getPlayer().isInteracting():
            self.game.getPlayer().setFacing('e')
            self.textOutputDesciption(self.game.getPlayer().getPlace().getPlaceInDirection(1).getFarsightDescription())
            self.updateGUI()

    def buttonLookSouth(self):
        """
        Setzt die Blickrichtung des Spielers richtung Süden und gibt die Beschreibung des Ortes aus
        """
        if not self.game.getPlayer().isInteracting():
            self.game.getPlayer().setFacing('s')
            self.textOutputDesciption(self.game.getPlayer().getPlace().getPlaceInDirection(2).getFarsightDescription())
            self.updateGUI()

    def buttonLookWest(self):
        """
        Setzt die Blickrichtung des Spielers richtung Westen und gibt die Beschreibung des Ortes aus
        """
        if not self.game.getPlayer().isInteracting():
            self.game.getPlayer().setFacing('w')
            self.textOutputDesciption(self.game.getPlayer().getPlace().getPlaceInDirection(3).getFarsightDescription())
            self.updateGUI()

    def buttonLook(self):
        """
        Gibt die Beschreibung des aktullenen Standorts des Spielers aus
        """
        if not self.game.getPlayer().isInteracting():
            self.textOutputDesciption(self.game.getPlayer().getPlace().getDescription())
            self.textOutputInteraction(self.game.getPlayer().getPlace().getInteractableThingsAsString())
            print(self.getTextInput())
            self.updateGUI()

    def buttonNext(self):
        # try:
        if not self.AnswerButtonsActive:
            if self.game.getDialogueHandler().isInDialogue():
                if self.getTextInput() == '':
                    self.game.getDialogueHandler().nextStep()
                else:
                    self.resetTextInput()
                    self.buttonNext()
            else:
                if self.getTextInput() == '':
                    if self.game.getPlayer().isInteracting():
                        self.textOutputWarning('Du musst eine Option auswwählen um fortfahren zu können!')
                    else:
                        self.textOutputWarning('Du musst mit etwas interagieren um diesen Button nutzen zu können!')
                        self.buttonLook()
                else:
                    if self.game.getPlayer().isInteracting():
                        if int(self.getTextInput()) <= self.game.getPlayer().getInteraction().getActionCount():
                            self.textOutputReset()
                            self.selectInteraction(int(self.getTextInput()))
                            if self.game.getPlayer().isInteracting() and not self.game.getDialogueHandler().isInDialogue():
                                self.textOutputInteraction(self.game.getPlayer().getInteraction().getActionsAsString())
                                self.gui.textInput.focus()
                            else:
                                self.buttonLook()
                            self.resetTextInput()
                    else:
                        if int(
                                self.getTextInput()) <= self.game.getPlayer().getPlace().getInteractionPossNum():  # Ist Eingabe möglich?
                            self.textOutputReset()
                            self.game.getPlayer().startInteractWith(
                                self.game.getPlayer().getPlace().getInteractionObject(int(self.getTextInput())))
                            self.textOutputInteraction(self.game.getPlayer().getInteraction().getActionsAsString())
                            self.resetTextInput()
                            self.gui.textInput.focus()
                        else:
                            self.resetTextInput()
                            self.textOutputReset()
                            self.textOutputWarning('Diese Interaktion ist nicht möglich!')
            self.updateGUI()
            # except:
            #    self.textOutputWarning('Ungültige Eingabe!')
            #    self.updateGUI()

    def selectInteraction(self, num):
        if self.game.getDialogueHandler().isInDialogue():
            self.updateDialogueOutput()
        else:
            self.textOutputDialogue(self.game.getPlayer().getInteraction().interact(
                self.game.getPlayer().getInteraction().getActions()[num]))

    def buttonMove(self):
        """
        Bewegt den Spieler, wenn möglich, in die aktuelle Blickrichtung und lässt den Spieler sich einmal umschauen
        """
        if not self.game.getPlayer().isInteracting():
            if not self.game.getPlayer().goDirection():
                self.textOutputWarning('Du kannst dich nicht in diese Richtung bewegen!')
            else:
                self.buttonLook()
            self.updateGUI()

    def buttonAnswerA(self):
        """
        Führt den Dialog mit ausgewählter Antwort fort
        """
        self.game.getPlayer().nextInteraction(button=0)
        # self.selectInteraction(None)
        self.ButtonText = []
        self.updateGUI()

    def buttonAnswerB(self):
        """
        Führt den Dialog mit ausgewählter Antwort fort
        """
        self.game.getPlayer().nextInteraction(button=1)
        # self.selectInteraction(None)
        self.ButtonText = []
        self.updateGUI()

    def buttonAnswerC(self):
        """
        Führt den Dialog mit ausgewählter Antwort fort
        """
        self.game.getPlayer().nextInteraction(button=2)
        # self.selectInteraction(None)
        self.ButtonText = []
        self.updateGUI()

    def buttonInventory(self, index):
        """
        Startet die Interaktion mit ausgewähltem Item
        :param index: Index des ausgewählten Items
        :type index: int
        """
        if not self.game.player.isInteracting():
            self.game.player.startInteractWith(self.game.player.getInventory().getItem(index))
            self.textOutputInteraction(self.game.getPlayer().getInteraction().getActionsAsString())

    def updateDialogueOutput(self):
        """
        Updatet die Antwortbuttons und gibt den aktuellen Textoutput des Dialogs aus
        """
        if self.game.getDialogueHandler().isInDialogue():
            self.ButtonText = self.game.getDialogueHandler().getButtonArray('text')
            textoutput = self.game.getDialogueHandler().getTextOutput()
            if textoutput[1] == "C":
                self.textOutputDialogue(textoutput[0])
            elif textoutput[1] == "P":
                self.textOutputMain(textoutput[0])

    def textOutputReset(self):
        """
        Resettet den Textoutput
        """
        self.textOutputSet('')

    def textOutputInteraction(self, text):
        """
        Fügt die Interaktionsmöglichekeiten an den aktuellen Textoutput an
        :param text: Interaktionsmöglichkeiten als String
        :type text: str
        """
        # Formatierung fehlt
        self.textOutputAdd(text)

    def textOutputMain(self, text):
        """
        Gibt Textoutput des Protagonisten aus
        :param text: Text als String
        :type text: str
        """
        print(text)
        self.textOutputSet(text)

    def textOutputDialogue(self, text):
        """
        Gibt Textoutput des Dialogpartners aus
        :param text: Text als String
        :type text: str
        """
        print(text)
        self.textOutputAdd(text)

    def textOutputDesciption(self, text):
        """
        Gibt Textoutput der aktuellen Ortsbeschreibung aus
        :param text: Text als String
        :type text: str
        """
        # Formatierung fehlt
        self.textOutputSet(text)

    def textOutputWarning(self, text):
        """
        Gibt Warnung aus
        :param text: Text als String
        :type text: str
        """
        # Formatierung fehlt
        self.textOutputAdd(text)

    def textOutputAdd(self, text):
        """
        Fügt den Text mit einer Zeile Abstand an den aktuellen Textoutput an
        :param text: Text als String
        :type text: str
        """
        print(text)
        self.gui.vTextOutput.set(self.gui.vTextOutput.get() + '\n\n' + text)

    def textOutputSet(self, text):
        """
        Setzt den Textoutput auf Text
        :param text: Text als String
        :type text: str
        """
        self.gui.vTextOutput.set(text)

    def setPlace(self):
        """
        Setzt die Ortsanzeige auf den aktuellen Standort des Spielers
        """
        self.gui.vPlaceOutput.set(self.game.getPlayer().getPlace().getName())

    def setPrestige(self):
        """
        Setzt die Prestigeanzeige auf den aktuellen Wert des Spielers
        """
        self.gui.vPrestigeOutput.set(self.game.getPlayer().getPrestige())

    def setAnswers(self):
        """
        Setzt die Buttons auf den aktuellen Inhalt der ButtonText-Liste
        """
        answers = self.ButtonText
        if len(answers) == 0:
            self.gui.buttonAnswerA.config(state='disabled', text='Antwort A')
            self.gui.buttonAnswerB.config(state='disabled', text='Antwort B')
            self.gui.buttonAnswerC.config(state='disabled', text='Antwort C')
            self.AnswerButtonsActive = False
            self.ButtonText = []
        else:
            self.AnswerButtonsActive = True
            if len(answers) >= 1:
                self.gui.buttonAnswerA.config(text=answers[0], state='active')
                self.gui.buttonAnswerB.config(state='disabled')
                self.gui.buttonAnswerC.config(state='disabled')
            if len(answers) >= 2:
                self.gui.buttonAnswerB.config(text=answers[1], state='active')
            if len(answers) == 3:
                self.gui.buttonAnswerC.config(text=answers[2], state='active')

    def setInventory(self):
        """
        Setzt die Inventar-Buttons auf den aktuellen Inhalt des Spielerinventars
        """
        for i in range(10):
            if self.game.getPlayer().getInventory().isItemInSlot(i):
                self.ImageInventorySlot[i] = PhotoImage(file=self.game.player.inventory.getItem(i).getTexture())
                self.getInventoryButtonWithIndex(i).config(image=self.ImageInventorySlot[i], state='active')
            else:
                self.getInventoryButtonWithIndex(i).config(image=self.ImageNoItem, state='disabled')

    def setMovementDirections(self):
        """
        Setzt den Bewegungsbuttons auf die aktuell gegebenen Möglichkeiten des Spielers
        """
        if self.game.getPlayer().canMove() or not self.game.getPlayer().isInteracting():
            self.gui.buttonMove.config(state='active')
            if self.game.getPlayer().getPossibleDirections()[0] is None:
                self.gui.buttonNorth.config(state='disabled')
            else:
                self.gui.buttonNorth.config(state='active')
            if self.game.getPlayer().getPossibleDirections()[1] is None:
                self.gui.buttonEast.config(state='disabled')
            else:
                self.gui.buttonEast.config(state='active')
            if self.game.getPlayer().getPossibleDirections()[2] is None:
                self.gui.buttonSouth.config(state='disabled')
            else:
                self.gui.buttonSouth.config(state='active')
            if self.game.getPlayer().getPossibleDirections()[3] is None:
                self.gui.buttonWest.config(state='disabled')
            else:
                self.gui.buttonWest.config(state='active')
        else:
            self.gui.buttonNorth.config(state='disabled')
            self.gui.buttonEast.config(state='disabled')
            self.gui.buttonSouth.config(state='disabled')
            self.gui.buttonWest.config(state='disabled')
            self.gui.buttonMove.config(state='disabled')

    def getInventoryButtonWithIndex(self, index):
        """
        Selektiert den Inventar-Button an gegebenem Index
        :param index: Index des Buttons, mit dem man interargieren möchte
        :return: Button
        """
        if index == 0:
            return self.gui.buttonInventory1
        elif index == 1:
            return self.gui.buttonInventory2
        elif index == 2:
            return self.gui.buttonInventory3
        elif index == 3:
            return self.gui.buttonInventory4
        elif index == 4:
            return self.gui.buttonInventory5
        elif index == 5:
            return self.gui.buttonInventory6
        elif index == 6:
            return self.gui.buttonInventory7
        elif index == 7:
            return self.gui.buttonInventory8
        elif index == 8:
            return self.gui.buttonInventory9
        elif index == 9:
            return self.gui.buttonInventory10
        elif index == 10:
            return self.gui.buttonInventory11

    def getTextInput(self):
        """
        Gibt den aktuellen Textinput zurück
        :return: Textinput
        :rtype: str
        """
        return self.gui.vTextInput.get()

    def resetTextInput(self):
        """
        Setzt die Textinput-Zeile zurück
        """
        self.gui.vTextInput.set('')

    def updateGUI(self):
        """
        Updatet alle GUI-Elemente
        """
        self.toggleMovementButtons()
        self.setPlace()
        self.setPrestige()
        self.setAnswers()
        self.setInventory()
        self.setMovementDirections()
        self.updateDialogueOutput()

    def toggleMovementButtons(self):
        """
        Deaktiviert Move- und Look-Button, während der Spieler interargiert
        """
        if self.game.getPlayer().isInteracting():
            self.gui.buttonLook.config(state='disabled')
            self.gui.buttonMove.config(state='disabled')
        else:
            self.gui.buttonLook.config(state='active')
            self.gui.buttonMove.config(state='active')
