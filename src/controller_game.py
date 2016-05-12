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
        # Aktivierung des Fensters
        self.gui.fenster.mainloop()

    def windowCloseEvent(self):
        if messagebox.askokcancel("Beenden", "Möchtest du das Spiel wirklich beenden? \nDein Spielstand wird dabei unwiederruflich gelöscht!"):
            self.gui.fenster.quit()
            self.gui.fenster.destroy()

    def buttonLookNorth(self):
        print('OK')
        pass

    def buttonLookEast(self):
        print('OK')
        pass

    def buttonLookSouth(self):
        print('OK')
        pass

    def buttonLookWest(self):
        print('OK')
        pass

    def buttonLook(self):
        print('OK')
        pass

    def buttonNext(self):
        print('OK')
        pass

    def buttonMove(self):
        print('OK')
        pass

    def buttonAnswerA(self):
        print('OK')
        pass

    def buttonAnswerB(self):
        print('OK')
        pass

    def buttonAnswerC(self):
        print('OK')
        pass
