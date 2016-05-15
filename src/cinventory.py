

class Inventory(object):
    def __init__(self, player):
        self.player = player
        self.items = []  # List(of Item)

    def isEmpty(self):
        return len(self.items) == 0

    def getItem(self, index):
        return self.items[index]

    def removeItem(self, index):
        self.items.remove(self.getItem(index))
