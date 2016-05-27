from src.gameclasses.cinventory import *
from src.gameclasses.centity import *


class Item(Entity):
    def __init__(self, map):
        Entity.__init__(self, map)
        self.texturePath = None
        self.canBeMoved = False
        self.count = 1

    def getTexture(self):
        return self.texturePath

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


class Letter(Item):
    def __init__(self, map):
        Item.__init__(self, map)
        self.name = 'Brief'
        self.description = 'Dies ist ein Brief'
        self.read = False
        self.content = 'Brief'
        self.texturePath = 'gif/Letter.gif'
        self.setActions([0, 3, 2])
        self.quitPhrase = 'Brief geschlossen'

    def getContent(self):
        if self.place.__class__.__name__ == 'Train':
            self.place.getMap().getPlacePerName('Train').allowExit()
            self.place.getMap().getPlacePerName('Train').denyEnter()
        self.read = True
        return self.content

