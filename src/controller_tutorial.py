from src.gui_game import *


class TutorialController(object):
    def __init__(self):
        # Tutorialphase wird initialisiert
        self.phase = 0
        self.text = ['Willkommen im Tutorial für Lost Brother - The Choice is yours!',
                     'Dies ist die Benutzeroberfläche',
                     'Die Textausgaben, aus denen der größte Teil des Spieles besteht werden in diesem Fenster angezeigt!',
                     'Dein aktueller Aufenthaltsort wird hier angezeigt',
                     'Hier wird dein Ruhm angezeigt. Dieser kann positiv, jedoch auch negativ sein! Dies hängt von DEINEN Entscheidungen ab!',
                     'Dein Inventar kann Gegenstände beinhalten, welche du aufgesammelt hast. Klicke auf einen von diesen um dir Informationen über ihn anzeigen zu lassen',
                     'Mit den Knöpfen in diesem Feld kannst du dich umschauen und bewegen. Klicke eine der Pfeiltasten an um in die gedrückte Richtung zu schauen!',
                     'Durch betätigen der "Bewegen" Taste kannst du dann dann in die Richtung, in die duu zuletzt geschaut hast bewegen.',
                     'Möchtest du dich nur an deinem Aktuellen Standpunkt umschauen nutze die "Umschauen" Taste',
                     'Wenn du mit einem Gegenstand oder einer Person interagieren möchtest, gib einfach die angezeigte Nummer in dieses Textfeld ein und betätige den "Weiter" Button',
                     'Betätige den "Weiter" Button während eines Dialoges um dein Gegenüber weiterreden zu lassen',
                     'Während mancher Dialoge hast du die Möglichkeit eine Entscheidung zu Treffen, nutze dafür einfach einen dieser Buttons',
                     'Wähle Weise! Die Entscheidungen wirken sich auf deinen Ruhm und auf den Verlauf der Geschichte aus!',
                     'Für das optimale Spielerlebniss sollten Sounds aktiviert sein!',
                     'Viel Spaß']
        # Neues GUI-Objekt
        self.gui = GUIGame(self.buttonLookNorth, self.buttonLookEast, self.buttonLookSouth, self.buttonLookWest,
                           self.buttonMove, self.buttonLook, self.buttonNext, self.buttonAnswerA,
                           self.buttonAnswerB, self.buttonAnswerC)
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
            self.gui.fenster.quit()
            self.gui.fenster.destroy()

    def updateOutput(self):
        print('OK')
        pass

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
        if self.phase < (len(self.text)-1):
            self.setText(self.text[self.phase])
            self.phase += 1
        else:
            self.gui.buttonNext.config(state='disabled')
            self.setText("Bereit zum Spielen?")
            self.setAnswers(['JA!', 'JAA!', 'JAAA!'])

if __name__ == '__main__':
    t = TutorialController()