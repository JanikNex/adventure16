from src.gui_credits import *
from src.caudiohandler import *


class CreditController(object):
    def __init__(self):
        # Creditphase wird initialisiert
        self.phase = 0
        self.text = [
            ['1', 'XXX'],
            ['2', 'XXX'],
            ['3', 'XXX'],
            ['4', 'XXX'],
            ['Vielen Dank!', 'XXX']
        ]
        # Neues GUI-Objekt
        self.gui = GUICredits()
        # Neuer AudioHandler
        self.audioHandler = AudioHandler('credits.wav')
        self.audioHandler.play()
        # Registrierung der Event-Handler
        self.gui.fenster.protocol("WM_DELETE_WINDOW", self.windowCloseEvent)
        self.gui.fenster.bind("<Return>", self.windowCloseEvent)
        # Beginnen der Präsentation
        self.gui.fenster.after(2500, self.nextPhase)
        # Aktivierung des Fensters
        self.gui.fenster.mainloop()

    def windowCloseEvent(self, event=None):
        self.audioHandler.stop()
        self.gui.fenster.quit()
        self.gui.fenster.destroy()

    def setText(self, text):
        self.gui.title.set(text[0])
        self.gui.description.set(text[1])

    def nextPhase(self):
        if self.phase <= (len(self.text)-1):
            self.setText(self.text[self.phase])
            self.phase += 1
            self.gui.fenster.after(2500, self.nextPhase)


if __name__ == '__main__':
    t = CreditController()