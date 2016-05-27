from src.gameclasses.centity import *


class Citizen(Entity):
    def __init__(self, map):
        Entity.__init__(self, map)
        self.canTalk = False
        self.alreadyTalked = False
        self.talkTimes = 0
        self.inspection = ''
        self.carryingItem = None
        self.path = None

    def canTalk(self):
        """
        Gibt zurück, ob dieser Citizen noch sprechen kann
        :rtype: bool
        """
        return self.canTalk

    def alreadyTalked(self):
        """
        Gibt zurück, ob der Citizen bereits einmal gesprochen hat
        :rtype: bool
        """
        return self.alreadyTalked

    def getInspection(self):
        """
        Gibt Erinnerungen an die Vergangenheit zurück
        :rtype: str
        """
        return self.inspection

    def talk(self):
        """
        Startet, falls möglich, einen Dialog mit diesem Citizen
        :return:
        """
        if self.canTalk and self.talkTimes > 0:
            self.alreadyTalked = True
            self.talkTimes -= 1
            self.map.getGame().getDialogueHandler().startDialogue(path=self.path)
            return ''
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
        self.canTalk = True
        self.talkTimes = 1000
        self.path = 'testdialogue.json'
