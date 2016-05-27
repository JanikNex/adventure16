from src.gameclasses.centity import *
from src.dialogueTest import *

class Citizen(Entity):
    def __init__(self, map):
        Entity.__init__(self, map)
        self.canTalk = False
        self.alreadyTalked = False
        self.talkTimes = 0
        self.inspection = ''
        self.text = []
        self.carryingItem = None
        self.path = None

    def canTalk(self):
        return self.canTalk

    def alreadyTalked(self):
        return self.alreadyTalked

    def getInspection(self):
        return self.inspection

    def getText(self):
        return self.text

    def talk(self):
        if self.canTalk and self.talkTimes > 0:
            self.alreadyTalked = True
            self.talkTimes -= 1
            return self.map.getGame().getDialogueHandler().startDialogue(path=self.path)
        else:
            return 'Du kannst mit dieser Person nicht sprechen!'


class Visitor(Citizen):
    def __init__(self, map):
        Citizen.__init__(self, map)
        self.name = 'Random Person'
        self.description = 'Dat issn komischer Typ'
        self.inspection = 'Was ganz emotionales muss hier hin!'
        self.setActions([0, 1, 4, 2])
        self.quitPhrase = 'Von Person abgewendet!'
        self.text = getText()
        self.canTalk = True
        self.talkTimes = 1000
        self.path = 'testdialogue.json'

