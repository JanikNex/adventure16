from src.gui_game import *
from src.cgame import *


class GameController(object):
    def __init__(self):
        # Neues Game-Objekt
        self.game = Game()
        # Neues GUI-Objekt
        self.gui = GUIGame(self.buttonLookNorth, self.buttonLookEast, self.buttonLookSouth, self.buttonLookWest,
                           self.buttonMove, self.buttonLook, self.buttonNext, self.buttonAnswerA,
                           self.buttonAnswerB, self.buttonAnswerC)
        # Registrierung des WindowClose Event-Handlers
        self.gui.fenster.protocol("WM_DELETE_WINDOW", self.windowCloseEvent)
        # GUI an Spielstart anpassen
        self.updateGUI()
        # Aktivierung des Fensters
        self.gui.fenster.mainloop()

    def windowCloseEvent(self):
        if messagebox.askokcancel("Beenden",
                                  "Möchtest du das Spiel wirklich beenden? \nDein Spielstand wird dabei unwiederruflich gelöscht!"):
            self.gui.fenster.quit()
            self.gui.fenster.destroy()

    def buttonLookNorth(self):
        self.game.getPlayer().setFacing('n')
        self.game.getPlayer().getPlace().getPlaceInDirection(0).getDescription()
        self.updateGUI()

    def buttonLookEast(self):
        self.game.getPlayer().setFacing('e')
        self.game.getPlayer().getPlace().getPlaceInDirection(1).getDescription()
        self.updateGUI()

    def buttonLookSouth(self):
        self.game.getPlayer().setFacing('s')
        self.game.getPlayer().getPlace().getPlaceInDirection(2).getDescription()
        self.updateGUI()

    def buttonLookWest(self):
        self.game.getPlayer().setFacing('w')
        self.game.getPlayer().getPlace().getPlaceInDirection(3).getDescription()
        self.updateGUI()

    def buttonLook(self):
        self.textOutputDesciption((self.game.getPlayer().getPlace().getDescription(), '\n', self.game.getPlayer().canMove()))
        self.updateGUI()

    def buttonNext(self):
        print('OK')
        pass

    def buttonMove(self):
        self.game.getPlayer().goDirection()
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

    def textOutputReset(self):
        pass

    def textOutputInteraction(self):
        pass

    def textOutputMain(self):
        pass

    def textOutputDialogue(self):
        pass

    def textOutputDesciption(self, text):
        # Formatierung fehlt
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
        pass

    def setMovementDirections(self):
        if self.game.getPlayer().canMove():
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

    def getTextInput(self):
        return self.gui.vTextInput.get()

    def resetTextInput(self):
        self.gui.vTextInput.set('')

    def updateGUI(self):
        self.setPlace()
        self.setPrestige()
        self.setAnswers()
        self.setInventory()
        self.setMovementDirections()
