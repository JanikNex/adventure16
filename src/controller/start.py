from src.gui.gui_start import *
from src.controller.controller_game import *
from src.controller.controller_tutorial import *
from src.controller.controller_credits import *


class Starter(object):
    def __init__(self):
        """
        Erstellt ein neues StarterObjekt, auf dem alle anderen GameFenster besieren werden.
        """
        self.start = GUIStart(self.startGame, self.tutorialStart, self.creditStart)
        # Registrierung des WindowClose Event-Handlers
        self.start.fenster.protocol("WM_DELETE_WINDOW", self.windowCloseEvent)
        self.start.fenster.mainloop()

    def windowCloseEvent(self):
        """
        Beendet das Mainfenster, wodurch nach einer okcancel Abfrage alle Fenster des Spiels geschlossen werden.
        """
        if messagebox.askokcancel("Beenden?",
                                  "Durch Beenden dieses Fensters werden alle Fenster dieses Spiels geschlossen!"):
            self.start.fenster.quit()
            self.start.fenster.destroy()
            sys.exit(0)

    def startGame(self):
        """
        Deaktiviert die Buttons des Starters, minimiert diesen, erstellt ein GameController Objekt und macht alles nach
        beendigung des GameControllers rückgängig.
        """
        # Startet neues Spiel
        # Deaktivieren des Buttons, damit nur ein Spiel zur gleichen Zeit laufen kann
        self.start.buttonStartGame.config(text='Ingame...', state='disabled', cursor='no')
        self.start.buttonTutorial.config(state='disabled', cursor='no')
        self.start.buttonCredits.config(state='disabled', cursor='no')
        self.start.fenster.iconify()
        # Spielobjekt erstellen
        game = GameController()
        # Nach beenden des Spieles wird der Button wieder aktiviert
        self.start.fenster.deiconify()
        self.start.buttonStartGame.config(text='Spiel starten', state='active', cursor='hand2')
        self.start.buttonTutorial.config(state='active', cursor='hand2')
        self.start.buttonCredits.config(state='active', cursor='hand2')
        # Zum Abschluss werden die Credits automatisch abgespielt
        self.creditStart()

    def tutorialStart(self):
        """
        Deaktiviert die Buttons des Starters, minimiert diesen, erstellt ein TutorialController Objekt und macht alles nach
        beendigung des TutorialControllers rückgängig.
        """
        # Startet neues Tutorial
        # Deaktivieren des Buttons, damit nur ein Tutorial zur gleichen Zeit laufen kann
        self.start.buttonStartGame.config(state='disabled', cursor='no')
        self.start.buttonTutorial.config(text='Ingame...', state='disabled', cursor='no')
        self.start.buttonCredits.config(state='disabled', cursor='no')
        self.start.fenster.iconify()
        # Spielobjekt erstellen
        tutorial = TutorialController()
        # Nach beenden des Tutorials wird der Button wieder aktiviert
        self.start.fenster.deiconify()
        self.start.buttonStartGame.config(state='active', cursor='hand2')
        self.start.buttonTutorial.config(text='Tutorial', state='active', cursor='hand2')
        self.start.buttonCredits.config(state='active', cursor='hand2')

    def creditStart(self):
        """
        Deaktiviert die Buttons des Starters, minimiert diesen, erstellt ein CreditController Objekt und macht alles nach
        beendigung des CreditControllers rückgängig.
        """
        # Startet Credits
        # Deaktivieren des Buttons, damit nur ein Credit-Fenster zur gleichen Zeit laufen kann
        self.start.buttonStartGame.config(state='disabled', cursor='no')
        self.start.buttonCredits.config(text='Ingame...', state='disabled', cursor='no')
        self.start.buttonTutorial.config(state='disabled', cursor='no')
        self.start.fenster.iconify()
        # Spielobjekt erstellen
        credits = CreditController()
        # Nach beenden der Credits wird der Button wieder aktiviert
        self.start.fenster.deiconify()
        self.start.buttonStartGame.config(state='active', cursor='hand2')
        self.start.buttonCredits.config(text='Credits', state='active', cursor='hand2')
        self.start.buttonTutorial.config(state='active', cursor='hand2')


if __name__ == '__main__':
    load = Starter()  # Erstellt ein neues Spielstart-Fenster
