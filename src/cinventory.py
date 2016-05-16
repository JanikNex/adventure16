

class Inventory(object):
    def __init__(self, player):
        self.player = player
        self.items = []  # List(of Item)

    def isEmpty(self):
        return len(self.items) == 0

    def isFull(self):
        return len(self.items) == 11

    def getItem(self, index):
        if index <= len(self.items)-1:
            return self.items[index]

    def isItemInSlot(self, index):
        return index <= (len(self.items)-1)

    def removeItemAtIndex(self, index):
        self.items.remove(self.getItem(index))

    def removeItem(self, item):
        self.items.remove(item)

    def addItem(self, item):
            self.items.append(item)

    def isItemInInventory(self, item):
        return item in self.items
