from src.gui.gui_credits import *
from src.utilclasses.caudiohandler import *
from src.utilclasses.cjsonhandler import *


class CreditController(object):
    def __init__(self, mode='fromStart'):
        # Creditphase wird initialisiert
        """
        Erstellt ein neues CreditController-Objekt
        :param mode: Modus der Credits (unbenutzt)
        """
        self.phase = 0
        self.jsonparser = JSONHandler()
        self.jsonparser.openNewFile('credits')
        self.text = self.jsonparser.getData()[str(mode)]['text']
        # Neues GUI-Objekt
        self.gui = GUICredits()
        # Neuer AudioHandler
        self.audioHandler = AudioHandler(self.jsonparser.getData()[str(mode)]['audiofile'])
        self.audioHandler.play()
        # Registrierung der Event-Handler
        self.gui.fenster.protocol("WM_DELETE_WINDOW", self.windowCloseEvent)
        self.gui.fenster.bind("<Return>", self.windowCloseEvent)
        # Beginnen der Präsentation
        self.gui.fenster.after(6000, self.nextPhase)
        # Aktivierung des Fensters
        self.gui.fenster.mainloop()

    def windowCloseEvent(self, event=None):
        """
        Stoppt die Audiowiedergabe und schließt das Fenster
        :param event: Event falls Funktion als Eventhandler aufgerufen wird
        """
        self.audioHandler.stop()
        self.gui.fenster.quit()
        self.gui.fenster.destroy()

    def setText(self, text):
        """
        Setzt die Textvariablen auf den Inhalt der übergebenen Liste
        :param text: Liste [Titel, Beschreibung]
        :type text: list
        """
        self.gui.title.set(text[0])
        self.gui.description.set(text[1])

    def nextPhase(self):
        """
        Startet die nächste Phase der Credits
        """
        if self.phase <= (len(self.text) - 1):
            self.setText(self.text[self.phase])
            self.phase += 1
            self.gui.fenster.after(4000, self.nextPhase)


if __name__ == '__main__':
    t = CreditController()
