from src.gameclasses.cplace import *


class Map(object):
    def __init__(self, game):
        self.game = game
        self.places = []
        self.items = []
        self.citizen = []
        print('[DEBUG] Map generation started...')
        jsonhandler = JSONHandler()
        jsonhandler.openNewFile('placedata')
        for i in jsonhandler.getData():
            self.places.append(Place(self, i))
        del jsonhandler
        print('[DEBUG] Map generation finished...')

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
            if i.getName() == name:
                return i
        return False

    def getPlacePerID(self, id):
        for i in self.places:
            if i.getID() == id:
                return i
        return None

    def connectPlaces(self):
        """
        Setzt die Verbindungen der einzelnen Orte untereinander
        """
        for i in self.places:
            i.setNeighbors()

    def getGame(self):
        """
        Gibt das aktuelle Gameobjekt zurück
        :return: Gameobjekt
        :rtype: object
        """
        return self.game

    def addItem(self, item):
        self.items.append(item)

    def addCitizen(self, citizen):
        self.citizen.append(citizen)

    def getItemPerName(self, name):
        for i in self.items:
            if i.getName() == name:
                return i
        return False

    def getCitizenPerName(self, name):
        for i in self.citizen:
            if i.getName() == name:
                return i
        return False
