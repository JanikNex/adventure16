from src.cplace import *


class Map(object):
    def __init__(self, game):
        self.game = game
        self.places = []
        self.places.append(Train(self))
        self.places.append(TrainStation(self))
        self.connectPlaces()

    def getPlacees(self):
        return self.places

    def getPlacePerName(self, name):
        for i in self.places:
            if i.__class__.__name__ == name:
                return i
        return False

    def connectPlaces(self):
        for i in self.places:
            i.setNeigbours()
