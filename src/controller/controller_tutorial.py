from src.gui.gui_game import *
from src.utilclasses.cjsonhandler import *
from src.utilclasses.caudiohandler import *


class TutorialController(object):
    def __init__(self):
        # Tutorialphase wird initialisiert
        self.phase = 0
        self.jsonphaser = JSONHandler()
        self.jsonphaser.openNewFile('tutorial')
        self.audiohandler = AudioHandler(self.jsonphaser.getData()['normal']['audiofile'])
        self.audiohandler.play()
        self.text = self.jsonphaser.getData()['normal']['text']
        # Neues GUI-Objekt
        self.gui = GUIGame(self.buttonLookNorth, self.buttonLookEast, self.buttonLookSouth, self.buttonLookWest,
                           self.buttonMove, self.buttonLook, self.buttonNext, self.buttonAnswerA,
                           self.buttonAnswerB, self.buttonAnswerC, self.buttonInventory)
        # Registrierung des WindowClose Event-Handlers
        self.gui.fenster.protocol("WM_DELETE_WINDOW", self.windowCloseEvent)

        # Buttons deaktivieren
        self.gui.buttonNorth.config(state='disabled')
        self.gui.buttonEast.config(state='disabled')
        self.gui.buttonSouth.config(state='disabled')
        self.gui.buttonWest.config(state='disabled')
        self.gui.buttonMove.config(state='disabled')
        self.gui.buttonLook.config(state='disabled')
        self.gui.buttonAnswerA.config(state='disabled')
        self.gui.buttonAnswerB.config(state='disabled')
        self.gui.buttonAnswerC.config(state='disabled')
        self.gui.textInput.config(state='disabled')
        self.gui.vPrestigeOutput.set(0)
        self.gui.vPlaceOutput.set('Tutorial')
        self.tutorial()
        # Aktivierung des Fensters
        self.gui.fenster.mainloop()

    def windowCloseEvent(self):
        """
        Schließt das Tutorialfenster, falls bei einer okcancel Abfrage auf ok geklickt wird.
        """
        if messagebox.askokcancel("Beenden?", "Möchtest du das Tutorial wirklich beenden?!"):
            self.audiohandler.stop()
            self.gui.fenster.quit()
            self.gui.fenster.destroy()

    def endTutorial(self):
        """
        Beendet das Tutorial, nachdem eine Infobox angezeigt wurde.
        """
        messagebox.showinfo('Tutorial', 'Ob dies die richtige Entscheidung war...')
        self.audiohandler.stop()
        self.gui.fenster.quit()
        self.gui.fenster.destroy()

# Callback Funktionen, welche beim Tutorial nicht benötigt werden
    def buttonLookNorth(self):
        """
        Leere Callbackfunktion
        """
        pass

    def buttonLookEast(self):
        """
        Leere Callbackfunktion
        """
        pass

    def buttonLookSouth(self):
        """
        Leere Callbackfunktion
        """
        pass

    def buttonLookWest(self):
        """
        Leere Callbackfunktion
        """
        pass

    def buttonLook(self):
        """
        Leere Callbackfunktion
        """
        pass

    def buttonNext(self):
        """
        Ruft die nächste Phase des Tutorials auf.
        """
        self.tutorial()

    def buttonMove(self):
        """
        Leere Callbackfunktion
        """
        pass

    def buttonInventory(self):
        """
        Leere Callbackfunktion
        """
        pass

    def buttonAnswerA(self):
        """
        Beendet das Tutorial
        """
        self.endTutorial()

    def buttonAnswerB(self):
        """
        Beendet das Tutorial
        """
        self.endTutorial()

    def buttonAnswerC(self):
        """
        Beendet das Tutorial
        """
        self.endTutorial()

    def setText(self, text):
        """
        Setzt den Text des Textfensters auf den gegebenen Text
        :param text: Anzuzeigender Text
        """
        self.gui.vTextOutput.set(text)

    def setAnswers(self, answers):
        """
        Setzt die Antwortbuttons auf gegebenen Text
        :param answers:
        """
        if len(answers) == 0:
            self.gui.buttonAnswerA.config(state='disabled', text='Antwort A')
            self.gui.buttonAnswerB.config(state='disabled', text='Antwort B')
            self.gui.buttonAnswerC.config(state='disabled', text='Antwort C')
        else:
            if len(answers) >= 1:
                self.gui.buttonAnswerA.config(text=answers[0], state='active')
                self.gui.buttonAnswerB.config(state='disabled')
                self.gui.buttonAnswerC.config(state='disabled')
            if len(answers) >= 2:
                self.gui.buttonAnswerB.config(text=answers[1], state='active')
            if len(answers) == 3:
                self.gui.buttonAnswerC.config(text=answers[2], state='active')

    def tutorial(self):
        """
        Springt zur nächsten Phase des Tutorials
        """
        if self.phase < (len(self.text)-1):
            self.setText(self.text[self.phase])
            self.phase += 1
        else:
            self.gui.buttonNext.config(state='disabled')
            self.setText("Bereit zum Spielen?")
            self.setAnswers(['JA!', 'JAA!', 'JAAA!'])

if __name__ == '__main__':
    t = TutorialController()