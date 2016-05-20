from src.citem import *
from src.ccitizen import *


class Place(object):
    def __init__(self, map):
        self.map = map
        self.name = ''
        self.description = ''
        self.farSightDescription = ''
        self.items = []
        self.citizen = []
        self.soundPath = ''
        self.accessAllowed = True
        self.exitAllowed = True
        self.neigbours = [None, None, None, None]

    def canEnter(self):
        return self.accessAllowed

    def canLeave(self):
        return self.exitAllowed

    def getName(self):
        return self.name

    def getDescription(self):
        return self.description

    def getItems(self):
        return self.items

    def getCitizens(self):
        return self.citizen

    def getNeigbours(self):
        return self.neigbours

    def getPlaceInDirection(self, index):
        return self.neigbours[index]

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
        text += 'Gegenstände:\n'
        if not len(self.items) == 0:
            for i in self.items:
                text += str(actionCount) + ' - ' + i.getName() + '\n'
                actionCount += 1
        if len(self.citizen)+len(self.items) == 0:
            return ''
        return text

    def getInteractionObject(self, index):
        options = self.citizen[:]
        options.extend(self.items)
        return options[index]

    def getInteractionPossNum(self):
        if not self.getMap().getGame().getPlayer().isInteracting():
            return len(self.citizen)+len(self.items)
        else:
            return -1


class Train(Place):
    def __init__(self, map):
        Place.__init__(self, map)
        self.exitAllowed = False
        self.accessAllowed = True
        self.name = 'ICE 2027'
        self.description = 'Jetzt sitze ich hier schon seit mehreren Stunden in diesem Zug. So langsam wird mir langweilig!'
        self.farSightDescription = 'Da issn Zuch!'
        self.soundPath = ''  # Fehlt
        self.items.append(Letter(map))
        self.items[0].setPlace(self)

    def setNeigbours(self):
        self.neigbours = [None, self.map.getPlacePerName('TrainStation'), None, None]


class TrainStation(Place):
    def __init__(self, map):
        Place.__init__(self, map)
        self.name = 'Bahnhof'
        self.description = 'Dies ist der Bahnhof'
        self.farSightDescription = 'Dat issn Bahnhof!'
        self.soundPath = ''  # Fehlt
        self.citizen.append(Visitor(map))
        self.citizen[0].setPlace(self)

    def setNeigbours(self):
        self.neigbours = [None, None, None, self.map.getPlacePerName('Train')]
