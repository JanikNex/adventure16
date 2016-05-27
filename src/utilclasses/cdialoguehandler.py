from src.utilclasses.cjsonhandler import *


class DialogueHandler(object):
    def __init__(self, game):
        self.game = game
        self.jsonphraser = JSONHandler()
        self.path = None
        self.inDialogue = False
        self.step = 0
        self.usePrestige = 0
        self.buttonArray = []
        self.textOutput = ''

    def startDialogue(self, path):
        if not self.inDialogue:
            self.path = path
            self.jsonphraser.openNewFile(self.path)
            self.usePrestige = self.game.getPlayer().getPrestige()
            self.inDialogue = True
            self.game.getPlayer().startInteractWith(self)
            self.nextStep()
            return ''

    def endDialogue(self):
        if self.inDialogue:
            self.inDialogue = False
            self.path = None
            self.step = 0
            self.game.getPlayer().endInteraction()

    def getButtonArray(self, mode='all'):
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
        return self.textOutput

    def nextStep(self, select=None):
        if self.step == -1:
            self.endDialogue()
            return
        self.textOutput = self.jsonphraser.getData()[str(self.usePrestige)][str(self.step)]['text']
        if select is None:
            thisStep = self.jsonphraser.getData()[str(self.usePrestige)][str(self.step)]
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
            thisStep = self.jsonphraser.getData()[str(self.usePrestige)][str(self.step)]
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
        return self.inDialogue
