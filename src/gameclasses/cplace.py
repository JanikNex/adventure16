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
        self.neigbours = jsonhandler.getData()[str(id)]['neigbours']
        del jsonhandler


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

    def getID(self):
        return self.id

    def getCitizens(self):
        return self.citizen

    def getNeigbours(self):
        result = []
        for i in self.neigbours:
            result.append(self.map.getPlacePerID(i))
        return result

    def getPlaceInDirection(self, index):
        return self.getNeigbours()[index]

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

    def createItem(self, item):
        self.items.append(item)
        item.setPlace(self)
        self.map.addItem(item)

    def createCitizen(self, citizen):
        self.citizen.append(citizen)
        citizen.setPlace(self)
        self.map.addCitizen(citizen)
