from src.gameclasses.cplace import *


class Map(object):
    def __init__(self, game):
        """
        Erstellt ein neues Map Objekt, durchläuft die placedata Datei und erstellt alle vorhandenen Räume
        Zudem verwaltet dieses Objekt alle Items und Citizens und kann somit Objekte anhand ihrer Namen zurückgeben
        :param game: Game
        :type game: Game
        """
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

    def getPlaces(self):
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
        """
        Gibt das Placeobjekt mit gegebener PlaceID zurück
        :param id: PlaceID aus der Placedata JSON Datei
        :type id: int
        :return: Gesuchter Platz oder None, falls kein Place mit dieser ID vorhanden ist
        :rtype: Place
        """
        for i in self.places:
            if i.getID() == id:
                return i
        return None

    def getGame(self):
        """
        Gibt das aktuelle Gameobjekt zurück
        :return: Gameobjekt
        :rtype: object
        """
        return self.game

    def addItem(self, item):
        """
        Fügt ein Itemobjekt zur Itemliste hinzu
        :param item: Item
        :type item: Item
        """
        self.items.append(item)

    def addCitizen(self, citizen):
        """
        Fügt ein citizenobjekt zur Citizenliste hinzu
        :param citizen: Citizen
        :type citizen: Citizen
        """
        self.citizen.append(citizen)

    def getItemPerName(self, name):
        """
        Gibt ein Item mit gegebenem Namen zurück
        :param name: Name eines Items
        :type name: str
        :return: Item
        :rtype: Item
        """
        for i in self.items:
            if i.getName() == name:
                return i
        return False

    def getCitizenPerName(self, name):
        """
        Gibt einen Citizen mit gegebenem Namen zurück
        :param name: Name eines Citizens
        :type name: str
        :return: Citizen
        :rtype: Citizen
        """
        for i in self.citizen:
            if i.getName() == name:
                return i
        return False
