from src.gameclasses.citem import *
from src.gameclasses.ccitizen import *
from src.utilclasses.cjsonhandler import *


class Place(object):
    def __init__(self, map, id):
        jsonhandler = JSONHandler()
        jsonhandler.openNewFile('placedata')
        self.map = map
        self.id = int(id)
        self.name = jsonhandler.getData()[str(id)]['name']
        self.description = jsonhandler.getData()[str(id)]['description']
        self.farSightDescription = jsonhandler.getData()[str(id)]['farSightDescription']
        self.items = []
        self.citizen = []
        for i in jsonhandler.getData()[str(id)]['items']:
            self.createItem(eval(i))
        for i in jsonhandler.getData()[str(id)]['citizen']:
            self.createCitizen(eval(i))
        self.soundPath = jsonhandler.getData()[str(id)]['soundpath']
        self.accessAllowed = jsonhandler.getData()[str(id)]['accessAllowed']
        self.exitAllowed = jsonhandler.getData()[str(id)]['exitAllowed']
        self.enterDeniedMessage = jsonhandler.getData()[str(id)]['enterDeniedMessage']
        self.exitDeniedMessage = jsonhandler.getData()[str(id)]['exitDeniedMessage']
        self.neighbors = jsonhandler.getData()[str(id)]['neighbors']
        print('[DEBUG] Generated', self.name)
        del jsonhandler

    def canEnter(self):
        """
        Gibt zurück, ob dieser Platz betreten werden kann
        :rtype: bool
        """
        return self.accessAllowed

    def canLeave(self):
        """
        Gibt zurück, ob dieser Platz verlassen werden kann
        :rtype: bool
        """
        return self.exitAllowed

    def getName(self):
        """
        Gibt den Namen des Platzes zurück
        :rtype: str
        """
        return self.name

    def getDescription(self):
        """
        Gibt die Beschreibung des Platzes zurück
        :rtype: str
        """
        return self.description

    def getItems(self):
        """
        Gibt die Itemobjekte, welche auf diesem Platz liegen zurück
        :rtype: list
        """
        return self.items

    def getID(self):
        """
        Gibt die ID des Platzes zurück
        :rtype: int
        """
        return self.id

    def getCitizens(self):
        """
        Gibt die Citizenobjekte, welche sich auf diesem Platz befinden zurück
        :rtype: list
        """
        return self.citizen

    def getEnterDeniedMessage(self):
        """
        Gibt die Nachicht zurück, welche angezeigt werden soll, falls ein Ort nicht betreten werden kann
        :rtype: str
        """
        return self.enterDeniedMessage

    def getExitDeniedMessage(self):
        """
        Gibt die Nachicht zurück, welche angezeigt werden soll, falls ein Ort nicht verlassen werden kann
        :rtype: str
        """
        return self.exitDeniedMessage

    def getNeighbors(self):
        result = []
        for i in self.neighbors:
            result.append(self.map.getPlacePerID(i))
        return result

    def getPlaceInDirection(self, index):
        return self.getNeighbors()[index]

    def getSound(self):
        return self.soundPath

    def allowEnter(self):
        self.accessAllowed = True

    def denyEnter(self):
        self.accessAllowed = False

    def allowExit(self):
        self.exitAllowed = True

    def denyExit(self):
        self.exitAllowed = False

    def getMap(self):
        return self.map

    def getFarsightDescription(self):
        return self.farSightDescription

    def removeItem(self, item):
        self.items.remove(item)

    def addItem(self, item):
        self.items.append(item)

    def getInteractableThingsAsString(self):
        text = 'Du kannst mit folgenden Personen oder Gegenständen interagieren:\n'
        actionCount = 0
        if not len(self.citizen) == 0:
            text += 'Personen:\n'
            for i in self.citizen:
                text += str(actionCount) + ' - ' + i.getName() + '\n'
                actionCount += 1
        if not len(self.items) == 0:
            text += 'Gegenstände:\n'
            for i in self.items:
                text += str(actionCount) + ' - ' + i.getName() + '\n'
                actionCount += 1
        if len(self.citizen) + len(self.items) == 0:
            return ''
        return text

    def getInteractionObject(self, index):
        options = self.citizen[:]
        options.extend(self.items)
        return options[index]

    def getInteractionPossNum(self):
        if not self.getMap().getGame().getPlayer().isInteracting():
            return len(self.citizen) + len(self.items)
        else:
            return -1

    def createItem(self, item):
        self.items.append(item)
        item.setPlace(self)
        self.map.addItem(item)

    def createCitizen(self, citizen):
        self.citizen.append(citizen)
        citizen.setPlace(self)
        self.map.addCitizen(citizen)
