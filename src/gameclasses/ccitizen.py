from src.gameclasses.centity import *
from src.gameclasses.citem import *
from src.utilclasses.cjsonhandler import *


class Citizen(Entity):
    def __init__(self, map, citizenid):
        Entity.__init__(self, map)
        jsonhandler = JSONHandler()
        jsonhandler.openNewFile('citizendata')
        self.name = jsonhandler.getData()[str(citizenid)]['name']
        self.description = jsonhandler.getData()[str(citizenid)]['description']
        self.canTalk = jsonhandler.getData()[str(citizenid)]['canTalk']
        self.inspection = jsonhandler.getData()[str(citizenid)]['inspection']
        self.setActions(jsonhandler.getData()[str(citizenid)]['actions'])
        self.quitPhrase = jsonhandler.getData()[str(citizenid)]['quitPhrase']
        self.talkTimes = jsonhandler.getData()[str(citizenid)]['talkTimes']
        self.path = jsonhandler.getData()[str(citizenid)]['path']
        self.visible = jsonhandler.getData()[str(citizenid)]['visible']
        self.carryingItem = None
        if jsonhandler.getData()[str(citizenid)]['carryingItem'] is not None:
            self.carryingItem = eval(jsonhandler.getData()[str(citizenid)]['carryingItem'])
        if self.carryingItem is not None:
            self.carryingItem.setPlace(self)
            self.map.addItem(self.carryingItem)
        self.alreadyTalked = False
        print('[DEBUG] Generated', self.name)
        del jsonhandler

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
            if self.carryingItem is not None:
                self.carryingItem.drop(self.carryingItem.getMap().getGame().getPlayer().getPlace())
                self.carryingItem.getMap().getGame().getPlayer().getPlace().addItem(self.carryingItem)
                self.carryingItem = None
            self.map.getGame().getDialogueHandler().startDialogue(path=self.path)
            return ''
        else:
            return 'Du kannst mit dieser Person nicht sprechen!'
