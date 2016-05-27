from src.gameclasses.cplace import *


class Map(object):
    def __init__(self, game):
        self.game = game
        self.places = []
        self.places.append(Train(self))
        self.places.append(TrainStation(self))
        self.connectPlaces()

    def getPlacees(self):
        """
        Gibt eine Liste aller vorhandenen Orte zurück
        :return: Liste aller Orte
        :rtype: list
        """
        return self.places

    def getPlacePerName(self, name):
        """
        Gibt Ortobjekt nach Namen zurück
        :param name: Klassenname
        :return: Ortobjekt
        :rtype: object
        """
        for i in self.places:
            if i.__class__.__name__ == name:
                return i
        return False

    def connectPlaces(self):
        """
        Setzt die Verbindungen der einzelnen Orte untereinander
        """
        for i in self.places:
            i.setNeigbours()

    def getGame(self):
        """
        Gibt das aktuelle Gameobjekt zurück
        :return: Gameobjekt
        :rtype: object
        """
        return self.game
