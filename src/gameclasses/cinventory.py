

class Inventory(object):
    def __init__(self, player):
        self.player = player
        self.items = []  # List(of Item)

    def isEmpty(self):
        """
        Gibt zurück, ob das Inventar leer ist oder nicht
        :return: Status
        :rtype: bool
        """
        return len(self.items) == 0

    def isFull(self):
        """
        Gibt zurück, ob das Inventar leer ist oder nicht
        :return: Status
        :rtype: bool
        """
        return len(self.items) == 11

    def getItem(self, index):
        """
        Gibt das Itemobjekt, welchs sich an gegebenem Index gebindet zurück
        :rtype: object
        """
        if index <= len(self.items)-1:
            return self.items[index]

    def isItemInSlot(self, index):
        """
        Gibt zurück, ob sich ein Item in einem bestimmten Inventar-Slot befindet
        :param index: Inventarslot
        :type index: int
        :rtype: bool
        """
        return index <= (len(self.items)-1)

    def removeItemAtIndex(self, index):
        """
        Entfernt ein Item von gegebenem Index
        :param index: Index des Items, welches entfernt werden soll
        :type index: int
        """
        self.items.remove(self.getItem(index))

    def removeItem(self, item):
        """
        Entfernt ein bestimmtes Itemobjekt aus dem Inventar
        :param item: Itemobjekt
        :type item: object
        """
        self.items.remove(item)

    def addItem(self, item):
        """
        Fügt ein gegebenes Itemobjekt zum Inventar hinzu
        :param item: Itemobjekt
        :type item: object
        """
        self.items.append(item)

    def isItemInInventory(self, item):
        """
        Gibt zurück, ob sich ein gegebenes Item im Inventar befindet
        :param item: Itemobekt
        :type item: object
        :return:
        """
        return item in self.items

    def getPlayer(self):
        """
        Gibt den dazugehörigen Spieler zurück
        :return: Player
        """
        return self.player

    def getMap(self):
        return self.player.getGame().getMap()