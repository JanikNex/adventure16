from src.cinventory import *


class Item(object):
    def __init__(self, map):
        self.name = ''
        self.place = None
        self.map = map
        self.texturePath = None
        self.canBeMoved = False
        self.description = ''
        self.actions = []
        self.count = 1

    def getName(self):
        return self.name

    def getPlace(self):
        return self.place

    def setPlace(self, place):
        self.place = place

    def getTexture(self):
        return self.texturePath

    def getDescription(self):
        return self.description

    def getActions(self):
        return self.actions

    def getActionCount(self):
        if len(self.actions) == 0:
            return -1
        return len(self.actions)

    def getActionsAsString(self):
        text = 'Du hast folgende Interaktionsmöglichkeiten\n'
        actionCount = 0
        if not len(self.actions) == 0:
            for i in self.actions:
                text += str(actionCount) + ' - ' + i + '\n'
                actionCount += 1
        if len(self.actions) == 0:
            return ''
        return text

    def inInventory(self):
        return self.map.getGame().getPlayer().getInventory().isItemInInventory(self)

    def drop(self, place):
        if self.inInventory() and self.canBeMoved:
            self.setPlace(place)

    def take(self):
        if not self.inInventory() and self.canBeMoved:
            self.setPlace(self.getPlace().getMap().getGame().getPlayer().getInventory())

    def getCanBeMoved(self):
        return self.canBeMoved

    def getCount(self):
        return self.count

    def setCount(self, count):
        self.count = count

    def interact(self, interactionCall):
        if interactionCall == 'Anschauen':
            return self.description


class Letter(Item):
    def __init__(self, map):
        Item.__init__(self, map)
        self.name = 'Brief'
        self.description = 'Dies ist ein Brief'
        self.read = False
        self.content = 'Brief'
        self.texturePath = 'Letter.gif'
        self.actions = ['Anschauen', 'Lesen', 'Weglegen']

    def getContent(self):
        if self.place.__class__.__name__ == 'Train':
            self.place.getMap().getPlacePerName('Train').allowExit()
            self.place.getMap().getPlacePerName('Train').denyEnter()
        self.read = True
        return self.content

    def interact(self, interactionCall):
        if not self.inInventory():
            self.getPlace().getMap().getGame().getPlayer().pickUpItem(self)
        if interactionCall == 'Anschauen':
            return self.description
        elif interactionCall == 'Lesen':
            return self.getContent()
        elif interactionCall == 'Weglegen':
            self.map.getGame().getPlayer().endInteraction()
            return "Brief geschlossen!"