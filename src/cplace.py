from src.citem import *


class Place(object):
    def __init__(self, map):
        self.map = map
        self.name = ''
        self.description = ''
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

    def removeItem(self, item):
        self.items.remove(item)

    def addItem(self, item):
        self.items.append(item)


class Train(Place):
    def __init__(self, map):
        Place.__init__(self, map)
        self.exitAllowed = True
        self.accessAllowed = True
        self.name = 'ICE 2027'
        self.description = 'Jetzt sitze ich hier schon seit mehreren Stunden in diesem Zug. So langsam wird mir langweilig!'
        self.soundPath = ''  # Fehlt
        self.items.append(Letter())

    def setNeigbours(self):
        self.neigbours = [None, self.map.getPlacePerName('TrainStation'), None, None]


class TrainStation(Place):
    def __init__(self, map):
        Place.__init__(self, map)
        self.name = 'Bahnhof'
        self.description = 'Dies ist der Bahnhof'
        self.soundPath = ''  # Fehlt

    def setNeigbours(self):
        self.neigbours = [None, None, None, self.map.getPlacePerName('Train')]
