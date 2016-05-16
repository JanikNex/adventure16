from src.gui_start import *
from src.controller_game import *
from src.controller_tutorial import *
from src.controller_credits import *


class Starter(object):
    def __init__(self):
        self.start = GUIStart(self.startGame, self.tutorialStart, self.creditStart)
        self.start.fenster.mainloop()

    def startGame(self):
        # Startet neues Spiel
        # Deaktivieren des Buttons, damit nur ein Spiel zur gleichen Zeit laufen kann
        self.start.buttonStartGame.config(text='Ingame...', state='disabled')
        self.start.buttonTutorial.config(state='disabled')
        self.start.buttonCredits.config(state='disabled')
        # Spielobjekt erstellen
        game = GameController()
        # Nach beenden des Spieles wird der Button wieder aktiviert
        self.start.buttonStartGame.config(text='Spiel starten', state='active')
        self.start.buttonTutorial.config(state='active')
        self.start.buttonCredits.config(state='active')
        # Zum Abschluss werden die Credits automatisch abgespielt
        # self.creditStart()

    def tutorialStart(self):
        # Startet neues Tutorial
        # Deaktivieren des Buttons, damit nur ein Tutorial zur gleichen Zeit laufen kann
        self.start.buttonStartGame.config(state='disabled')
        self.start.buttonTutorial.config(text='Ingame...', state='disabled')
        self.start.buttonCredits.config(state='disabled')
        # Spielobjekt erstellen
        tutorial = TutorialController()
        # Nach beenden des Tutorials wird der Button wieder aktiviert
        self.start.buttonStartGame.config(state='active')
        self.start.buttonTutorial.config(text='Tutorial', state='active')
        self.start.buttonCredits.config(state='active')

    def creditStart(self):
        # Startet Credits
        # Deaktivieren des Buttons, damit nur ein Credit-Fenster zur gleichen Zeit laufen kann
        self.start.buttonStartGame.config(state='disabled')
        self.start.buttonCredits.config(text='Ingame...', state='disabled')
        self.start.buttonTutorial.config(state='disabled')
        # Spielobjekt erstellen
        credits = CreditController()
        # Nach beenden der Credits wird der Button wieder aktiviert
        self.start.buttonStartGame.config(state='active')
        self.start.buttonCredits.config(text='Credits', state='active')
        self.start.buttonTutorial.config(state='active')


load = Starter()  # Erstellt ein neues Spielstart-Fenster
