from src.cinventory import *

class Item(object):
    def __init__(self):
        self.name = ''
        self.place = None
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

    def drop(self, place):
        if self.inInventory() and self.canBeMoved:
            self.setPlace(place)

    def take(self):
        if not self.inInventory() and self.canBeMoved:
            self.setPlace(self.getPlace().getMap().getGame().getPlayer().getInventory())

    def getCanBeMoved(self):
        return self.canBeMoved

    def inInventory(self):
        return isinstance(self, Inventory(self.getPlace().getMap().getGame().getPlayer()))

    def getCount(self):
        return self.count

    def setCount(self, count):
        self.count = count


class Letter(Item):
    def __init__(self):
        Item.__init__(self)
        self.name = 'Brief'
        self.description = 'Dies ist ein Brief'
        self.read = False
        self.content = 'Brief'
        self.actions = ['Anschauen', 'Lesen']

    def getContent(self):
        if self.place.__name__ == 'Train':
            self.place.getMap().getPlacePerName('Train').allowExit()
            self.place.getMap().getPlacePerName('Train').denyEnter()
        self.read = True
        return self.content


