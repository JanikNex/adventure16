from src.gameclasses.cinventory import *
from src.gameclasses.centity import *
from src.utilclasses.cjsonhandler import *


class Item(Entity):
    def __init__(self, map, itemid):
        Entity.__init__(self, map)
        jsonhandler = JSONHandler()
        jsonhandler.openNewFile('itemdata')
        self.name = jsonhandler.getData()[str(itemid)]['name']
        self.description = jsonhandler.getData()[str(itemid)]['description']
        self.texturePath = jsonhandler.getData()[str(itemid)]['texturepath']
        self.setActions(jsonhandler.getData()[str(itemid)]['actions'])
        self.canBeMoved = bool(jsonhandler.getData()[str(itemid)]['canBeMoved'])
        self.count = int(jsonhandler.getData()[str(itemid)]['count'])
        print('[DEBUG] Generated', self.name)
        del jsonhandler

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
    def __init__(self, map, itemid):
        Item.__init__(self, map, itemid)
        jsonhandler = JSONHandler()
        jsonhandler.openNewFile('itemdata')
        self.read = False
        self.content = jsonhandler.getData()[str(itemid)]['content']
        self.quitPhrase = 'Brief geschlossen'
        del jsonhandler

    def getContent(self):
        if self.place.getPlayer().getPlace().getID() == 0:
            self.place.getPlayer().getPlace().getMap().getPlacePerID(0).allowExit()
            self.place.getPlayer().getPlace().getMap().getPlacePerID(0).denyEnter()
        self.read = True
        return self.content

