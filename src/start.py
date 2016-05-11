from src.gui_start import *
from src.controller_game import *


class Starter(object):
    def __init__(self):
        self.start = GUIStart(self.startGame)

        self.start.fenster.mainloop()

    def startGame(self):  # Schließt das Fenster und startet das Spiel
        # Deaktivieren des Buttons, damit nur ein Spiel zur gleichen Zeit laufen kann
        self.start.buttonStartGame.config(text='Ingame...', state='disabled')
        # Spielobjekt erstellen
        game = GameController()
        # Nach beenden des Spieles wird der Button wieder aktiviert
        self.start.buttonStartGame.config(text='Spiel starten', state='active')


load = Starter()  # Erstellt ein neues Spielstart-Fenster
