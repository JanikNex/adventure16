from src.gui_game import *
from src.cgame import *


class GameController(object):
    def __init__(self):
        self.gui = GUIGame()
        self.game = Game()

        self.gui.fenster.mainloop()



