from src.gui_game import *
from src.cgame import *


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
        # Bilder initialisieren
        self.ImageNoItem = PhotoImage(file='noItem.gif')
        self.ImageInventorySlot = [None, None, None, None, None, None, None, None, None, None, None]
        # GUI an Spielstart anpassen
        self.updateGUI()
        # Einmal umschauen um den Spieleinstieg zu erleichtern
        self.buttonLook()
        # Aktivierung des Fensters
        self.gui.fenster.mainloop()

    def windowCloseEvent(self):
        if messagebox.askokcancel("Beenden",
                                  "Möchtest du das Spiel wirklich beenden? \nDein Spielstand wird dabei unwiederruflich gelöscht!"):
            self.gui.fenster.quit()
            self.gui.fenster.destroy()

    def buttonLookNorth(self):
        self.game.getPlayer().setFacing('n')
        self.textOutputDesciption(self.game.getPlayer().getPlace().getPlaceInDirection(0).getFarsightDescription())
        self.updateGUI()

    def buttonLookEast(self):
        self.game.getPlayer().setFacing('e')
        self.textOutputDesciption(self.game.getPlayer().getPlace().getPlaceInDirection(1).getFarsightDescription())
        self.updateGUI()

    def buttonLookSouth(self):
        self.game.getPlayer().setFacing('s')
        self.textOutputDesciption(self.game.getPlayer().getPlace().getPlaceInDirection(2).getFarsightDescription())
        self.updateGUI()

    def buttonLookWest(self):
        self.game.getPlayer().setFacing('w')
        self.textOutputDesciption(self.game.getPlayer().getPlace().getPlaceInDirection(3).getFarsightDescription())
        self.updateGUI()

    def buttonLook(self):
        self.textOutputDesciption(self.game.getPlayer().getPlace().getDescription())
        self.textOutputInteraction(self.game.getPlayer().getPlace().getInteractableThingsAsString())
        print(self.getTextInput())
        self.updateGUI()

    def buttonNext(self):
        if not self.getTextInput() == '':
            #try:
                if not self.game.getPlayer().isInteracting():
                    if int(self.getTextInput()) <= self.game.getPlayer().getPlace().getInteractionPossNum():
                        self.textOutputReset()
                        self.game.getPlayer().startInteractWith(self.game.getPlayer().getPlace().getInteractionObject(int(self.getTextInput())))
                        self.textOutputInteraction(self.game.getPlayer().getInteraction().getActionsAsString())
                        self.resetTextInput()
                    else:
                        self.resetTextInput()
                        self.textOutputReset()
                        self.textOutputWarning('Diese Interaktion ist nicht möglich!')
                else:
                    if not self.game.getDialogueHandler().isInDialogue():
                        if int(self.getTextInput()) <= self.game.getPlayer().getInteraction().getActionCount():
                            self.textOutputReset()
                            self.selectInteraction(int(self.getTextInput()))
                            if self.game.getPlayer().isInteracting():
                                self.textOutputInteraction(self.game.getPlayer().getInteraction().getActionsAsString())
                            else:
                                self.buttonLook()
                            self.resetTextInput()
                        else:
                            self.resetTextInput()
                            self.textOutputReset()
                            self.textOutputWarning('Diese Interaktion ist nicht möglich!')
                    else:
                        self.resetTextInput()
                        self.game.getPlayer().nextInteraction()
            #except:
            #    self.resetTextInput()
            #    self.textOutputWarning('Ungültige Eingabe!')
        else:
            if not self.game.getPlayer().isInteracting():
                self.resetTextInput()
                self.textOutputReset()
                self.textOutputWarning('Du musst mit etwas Interargieren oder eine Auswahl eingeben um diesen Button nutzen zu können!')
        self.updateGUI()

    def selectInteraction(self, num):
        self.textOutputInteraction(self.game.getPlayer().getInteraction().interact(self.game.getPlayer().getInteraction().getActions()[num]))

    def buttonMove(self):
        if not self.game.getPlayer().goDirection():
            self.textOutputWarning('Du kannst dich nicht in diese Richtung bewegen!')
        else:
            self.buttonLook()
        self.updateGUI()

    def buttonAnswerA(self):
        print('OK')
        pass

    def buttonAnswerB(self):
        print('OK')
        pass

    def buttonAnswerC(self):
        print('OK')
        pass

    def buttonInventory(self, index):
        if not self.game.player.isInteracting():
            self.game.player.startInteractWith(self.game.player.getInventory().getItem(index))
            self.textOutputInteraction(self.game.getPlayer().getInteraction().getActionsAsString())

    def textOutputReset(self):
        self.textOutputSet('')

    def textOutputInteraction(self, text):
        # Formatierung fehlt
        self.textOutputAdd(text)

    def textOutputMain(self):
        pass

    def textOutputDialogue(self):
        pass

    def textOutputDesciption(self, text):
        # Formatierung fehlt
        self.textOutputSet(text)

    def textOutputWarning(self, text):
        # Formatierung fehlt
        self.textOutputAdd(text)

    def textOutputAdd(self, text):
        self.gui.vTextOutput.set(self.gui.vTextOutput.get()+'\n\n'+text)

    def textOutputSet(self, text):
        self.gui.vTextOutput.set(text)

    def setPlace(self):
        self.gui.vPlaceOutput.set(self.game.getPlayer().getPlace().getName())

    def setPrestige(self):
        self.gui.vPrestigeOutput.set(self.game.getPlayer().getPrestige())

    def setAnswers(self):
        answers = []  # getAnswers einfügen
        if len(answers) == 0:
            self.gui.buttonAnswerA.config(state='disabled', text='Antwort A')
            self.gui.buttonAnswerB.config(state='disabled', text='Antwort B')
            self.gui.buttonAnswerC.config(state='disabled', text='Antwort C')
        else:
            if len(answers) >= 1:
                self.gui.buttonAnswerA.config(text=answers[0], state='active')
                self.gui.buttonAnswerB.config(state='disabled')
                self.gui.buttonAnswerC.config(state='disabled')
            if len(answers) >= 2:
                self.gui.buttonAnswerB.config(text=answers[1], state='active')
            if len(answers) == 3:
                self.gui.buttonAnswerC.config(text=answers[2], state='active')

    def setInventory(self):
        for i in range(10):
            if self.game.getPlayer().getInventory().isItemInSlot(i):
                self.ImageInventorySlot[i] = PhotoImage(file=self.game.player.inventory.getItem(i).getTexture())
                self.getInventoryButtonWithIndex(i).config(image=self.ImageInventorySlot[i], state='active')
            else:
                self.getInventoryButtonWithIndex(i).config(image=self.ImageNoItem, state='disabled')

    def setMovementDirections(self):
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
        return self.gui.vTextInput.get()

    def resetTextInput(self):
        self.gui.vTextInput.set('')

    def updateGUI(self):
        self.toggleMovementButtons()
        self.setPlace()
        self.setPrestige()
        self.setAnswers()
        self.setInventory()
        self.setMovementDirections()

    def toggleMovementButtons(self):
        if self.game.getPlayer().isInteracting():
            self.gui.buttonLook.config(state='disabled')
            self.gui.buttonMove.config(state='disabled')
        else:
            self.gui.buttonLook.config(state='active')
            self.gui.buttonMove.config(state='active')
