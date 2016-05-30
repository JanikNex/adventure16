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
        if messagebox.askokcancel("Beenden", "Möchtest du das Tutorial wirklich beenden?!"):
            self.audiohandler.stop()
            self.gui.fenster.quit()
            self.gui.fenster.destroy()

# Callback Funktionen, welche beim Tutorial nicht benötigt werden
    def buttonLookNorth(self):
        pass

    def buttonLookEast(self):
        pass

    def buttonLookSouth(self):
        pass

    def buttonLookWest(self):
        pass

    def buttonLook(self):
        pass

    def buttonNext(self):
        self.tutorial()

    def buttonMove(self):
        pass

    def buttonInventory(self):
        pass

    def buttonAnswerA(self):
        messagebox.showinfo('Tutorial', 'Ob diese Entscheidung weise war.....wer weiß!')
        self.gui.fenster.quit()
        self.gui.fenster.destroy()

    def buttonAnswerB(self):
        messagebox.showinfo('Tutorial', 'Ob diese Entscheidung weise war.....wer weiß!')
        self.gui.fenster.quit()
        self.gui.fenster.destroy()

    def buttonAnswerC(self):
        messagebox.showinfo('Tutorial', 'Ob diese Entscheidung weise war.....wer weiß!')
        self.gui.fenster.quit()
        self.gui.fenster.destroy()

    def setText(self, text):
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