from gui_game import *
from cgame import *


class GameController(object):
    def __init__(self):
        self.gui = GUIGame()
        self.game = Game()

        self.gui.fenster.mainloop()



