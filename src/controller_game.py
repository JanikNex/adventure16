from src.gui_game import *
from src.cgame import *


class GameController(object):
    def __init__(self):
        # Neues GUI-Objekt
        self.gui = GUIGame()
        # Neues Game-Objekt
        self.game = Game()
        # Registrierung des WindowClose Event-Handlers
        self.gui.fenster.protocol("WM_DELETE_WINDOW", self.windowCloseEvent)
        # Aktivierung des Fensters
        self.gui.fenster.mainloop()

    def windowCloseEvent(self):
        if messagebox.askokcancel("Beenden", "Möchtest du das Spiel wirklich beenden? Dein Spielstand wird dabei unwiederruflich gelöscht!"):
            self.gui.fenster.quit()
            self.gui.fenster.destroy()

