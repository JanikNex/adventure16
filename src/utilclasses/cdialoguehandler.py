from src.utilclasses.cjsonhandler import *


class DialogueHandler(object):
    def __init__(self, game):
        self.game = game
        self.jsonparser = JSONHandler()
        self.path = None
        self.inDialogue = False
        self.step = 0
        self.usePrestige = 0
        self.buttonArray = []
        self.textOutput = ''

    def startDialogue(self, path):
        """
        Startet einen neuen Dialog zwischen dem Spieler und der übergebenen JSON Datei
        :param path: Dateiname der JSON Datei
        :type path: str
        """
        if not self.inDialogue:
            self.path = path
            self.jsonparser.openNewFile(self.path)
            print(self.jsonparser.getData())
            self.usePrestige = self.game.getPlayer().getPrestige()
            self.inDialogue = True
            self.game.getPlayer().startInteractWith(self)
            self.nextStep()

    def endDialogue(self):
        """
        Beendet den aktuellen Dialog, falls einer aktiv ist
        """
        if self.inDialogue:
            self.inDialogue = False
            self.path = None
            self.step = 0
            self.game.getPlayer().endInteraction()

    def getButtonArray(self, mode='all'):
        """
        Gibt die Inhalte der Antwortbuttons zurück.
        :param mode: default ist all, durch text bekommt man nur den Text und durch goto nur die goTo-Zahlen
        :rtype: list
        """
        if len(self.buttonArray) == 0 or (
                    len(self.buttonArray[0]) == 0 and len(self.buttonArray[1]) == 0 and len(self.buttonArray[2]) == 0):
            return []
        else:
            if mode == 'all':
                return self.buttonArray
            elif mode == 'text':
                return [self.buttonArray[0][0], self.buttonArray[1][0], self.buttonArray[2][0]]
            elif mode == 'goto':
                return [self.buttonArray[0][1], self.buttonArray[1][1], self.buttonArray[2][1]]

    def getTextOutput(self):
        """
        Gibt den aktuellen Textoutput zurück.
        :return: ['Text', 'Operator-char']
        :rtype: list
        """
        return self.textOutput

    def nextStep(self, select=None):
        """
        Geht mit dem Dialog in den nächsten Schritt und updated alle Parameter
        :param select: Button, welcher als Antwortmöglichkeit aufgewählt wurde
        """
        if self.step == -1:
            self.endDialogue()
            return
        if select is None:
            thisStep = self.jsonparser.getData()[str(self.usePrestige)][str(self.step)]
            self.textOutput = [thisStep['text'], thisStep['operator']]
            print(thisStep)
            if thisStep['operator'] == 'P':
                self.step = int(thisStep['goTo'])
                self.game.getPlayer().increasePrestige(int(thisStep['prestigeChange']))
            elif thisStep['operator'] == 'C':
                if 'buttons' in thisStep:
                    self.buttonArray = thisStep['buttons']
                else:
                    self.step = int(thisStep['skipTo'])
        else:
            self.step = self.getButtonArray('goto')[select]
            thisStep = self.jsonparser.getData()[str(self.usePrestige)][str(self.step)]
            self.textOutput = [thisStep['text'], thisStep['operator']]
            print(thisStep)
            if thisStep['operator'] == 'P':
                self.step = int(thisStep['goTo'])
                self.game.getPlayer().increasePrestige(
                    int(thisStep['prestigeChange']))
            elif thisStep['operator'] == 'C':
                if 'buttons' in thisStep:
                    self.buttonArray = thisStep['buttons']
                if not self.getButtonArray('goto')[select]:
                    self.step = int(thisStep['skipTo'])
                else:
                    self.step = self.getButtonArray('goto')[select]

    def isInDialogue(self):
        """
        Gibt zurück, ob gerade ein Dialog aktiv ist
        :rtype: bool
        """
        return self.inDialogue
