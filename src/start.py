from gui_start import *
from controller_game import *


class Starter(object):
    def __init__(self):
        self.start = GUIStart(self.startGame)

        self.start.fenster.mainloop()

    def startGame(self):  # Schließt das Fenster und startet das Spiel
        print("GO!")
        self.start.buttonStartGame.config(text='Ingame...', state='disabled')
        game = GameController()


load = Starter()  # Erstellt ein neues Spielstart-Fenster
