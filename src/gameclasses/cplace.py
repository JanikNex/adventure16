from src.gameclasses.citem import *
from src.gameclasses.ccitizen import *
from src.utilclasses.cjsonhandler import *


class Place(object):
    def __init__(self, map, id):
        jsonhandler = JSONHandler()
        jsonhandler.openNewFile('placedata')
        self.map = map
        self.id = int(id)
        self.name = jsonhandler.getData()[str(id)]['name']
        self.description = jsonhandler.getData()[str(id)]['description']
        self.farSightDescription = jsonhandler.getData()[str(id)]['farSightDescription']
        self.items = []
        self.citizen = []
        for i in jsonhandler.getData()[str(id)]['items']:
            self.createItem(eval(i))
        for i in jsonhandler.getData()[str(id)]['citizen']:
            self.createCitizen(eval(i))
        self.soundPath = jsonhandler.getData()[str(id)]['soundpath']
        self.accessAllowed = jsonhandler.getData()[str(id)]['accessAllowed']
        self.exitAllowed = jsonhandler.getData()[str(id)]['exitAllowed']
        self.enterDeniedMessage = jsonhandler.getData()[str(id)]['enterDeniedMessage']
        self.exitDeniedMessage = jsonhandler.getData()[str(id)]['exitDeniedMessage']
        self.neighbors = jsonhandler.getData()[str(id)]['neighbors']
        print('[DEBUG] Generated', self.name)
        del jsonhandler

    def canEnter(self):
        """
        Gibt zurück, ob dieser Platz betreten werden kann. Kann er nicht betreten werden aber der Spieler besitzt einen
        Schlüssel, wird der Platz freigeschaltet.
        :rtype: bool
        """
        if self.accessAllowed:
            return True
        elif not self.accessAllowed and self.map.getGame().getPlayer().hasKeyForPlace(self):
            self.map.getGame().getPlayer().useKey(self)
            self.accessAllowed = True
            return True
        elif not self.accessAllowed and not self.map.getGame().getPlayer().hasKeyForPlace(self):
            return False

    def canLeave(self):
        """
        Gibt zurück, ob dieser Platz verlassen werden kann
        :rtype: bool
        """
        return self.exitAllowed

    def getName(self):
        """
        Gibt den Namen des Platzes zurück
        :rtype: str
        """
        return self.name

    def getDescription(self):
        """
        Gibt die Beschreibung des Platzes zurück
        :rtype: str
        """
        return self.description

    def getItems(self):
        """
        Gibt die Itemobjekte, welche auf diesem Platz liegen zurück
        :rtype: list
        """
        return self.items

    def getID(self):
        """
        Gibt die ID des Platzes zurück
        :rtype: int
        """
        return self.id

    def getCitizens(self):
        """
        Gibt die Citizenobjekte, welche sich auf diesem Platz befinden zurück
        :rtype: list
        """
        return self.citizen

    def getVisibleCitizens(self):
        """
        Gibt eine Liste nur der sichtbaren Citizens zurück.
        :return: Liste sichtbarer Citizens
        :rtype: list
        """
        citizens = []
        for i in self.citizen:
            if i.isVisible():
                citizens.append(i)
        return citizens

    def getVisibleItems(self):
        """
        Gibt eine Liste nur der sichtbaren Items zurück.
        :return: Liste sichtbarer Items
        :rtype: list
        """
        items = []
        for i in self.items:
            if i.isVisible():
                items.append(i)
        return items

    def getEnterDeniedMessage(self):
        """
        Gibt die Nachicht zurück, welche angezeigt werden soll, falls ein Ort nicht betreten werden kann
        :rtype: str
        """
        return self.enterDeniedMessage

    def getExitDeniedMessage(self):
        """
        Gibt die Nachicht zurück, welche angezeigt werden soll, falls ein Ort nicht verlassen werden kann
        :rtype: str
        """
        return self.exitDeniedMessage

    def getNeighbors(self):
        """
        Gibt die Nachbarobjekte zurück
        :return: list of Place
        :rtype: list
        """
        result = []
        for i in self.neighbors:
            result.append(self.map.getPlacePerID(i))
        return result

    def getPlaceInDirection(self, index):
        """
        Gibt das Nachbarobjekt in einer bestimmten Richtung zurück.
        :param index: Richtungsindex
        :type index: int
        :return: Place
        :rtype: Place
        """
        return self.getNeighbors()[index]

    def getSound(self):
        """
        Gibt den Soundpath des Objekts zurück
        :return: Soundpath des Objekts
        :rtype: str
        """
        return self.soundPath

    def allowEnter(self):
        """
        Erlaubt das betreten dieses Ortes
        """
        self.accessAllowed = True

    def denyEnter(self):
        """
        Verbietet das betreten dieses Ortes
        """
        self.accessAllowed = False

    def allowExit(self):
        """
        Erlaubt das verlassen dieses Ortes
        """
        self.exitAllowed = True

    def denyExit(self):
        """
        Verbietet das verlassen dieses Ortes
        """
        self.exitAllowed = False

    def getMap(self):
        """
        Gibt die Map zurück
        :return: Map
        :rtype: Map
        """
        return self.map

    def getFarsightDescription(self):
        """
        Gibt die Entfernungsbeschreibung dieses Ortes zurück
        :return: Entfernungsbeschreibung
        :rtype: str
        """
        return self.farSightDescription

    def removeItem(self, item):
        """
        Entfernt ein gegebenes Item von diesem Ort
        :param item: zu entfernendes Item
        :type item: Item
        """
        self.items.remove(item)

    def addItem(self, item):
        """
        Fügt ein gegebenes Item zu diesem Ort hinzu
        :param item: hinzuzufügendes Item
        :type item: Item
        """
        self.items.append(item)

    def getInteractableThingsAsString(self):
        """
        Gibt die Interaktionsmöglichkeiten, also alle Personen und Gegenstände dieses Ortes zusammen mit ihrer
        ActionID zurück
        :return: Ineraktionsmöglichkeiten
        :rtype: str
        """
        text = 'Du kannst mit folgenden Personen oder Gegenständen interagieren:\n'
        actionCount = 0
        if not len(self.getVisibleCitizens()) == 0:
            text += 'Personen:\n'
            for i in self.getVisibleCitizens():
                text += str(actionCount) + ' - ' + i.getName() + '\n'
                actionCount += 1
        if not len(self.getVisibleItems()) == 0:
            text += 'Gegenstände:\n'
            for i in self.getVisibleItems():
                text += str(actionCount) + ' - ' + i.getName() + '\n'
                actionCount += 1
        if len(self.getVisibleCitizens()) + len(self.getVisibleItems()) == 0:
            return ''
        return text

    def getInteractionObject(self, index):
        """
        Gibt ein Interaktionsobjekt mit einer gegebenen ActionID zurück
        :param index: ActionID
        :type index: int
        :return: Entity
        :rtype: Entity
        """
        options = self.getVisibleCitizens()[:]
        options.extend(self.getVisibleItems())
        return options[index]

    def getInteractionPossNum(self):
        """
        Gibt die maximale Anzahl an Interaktionsmöglichkeiten zurück
        :return:
        """
        if not self.getMap().getGame().getPlayer().isInteracting():
            return len(self.getVisibleCitizens()) + len(self.getVisibleItems())
        else:
            return -1

    def createItem(self, item):
        """
        Erstellt ein gegebenes Item komplett im gesamten Spiel
        :param item: Item
        :type item: Item
        """
        self.items.append(item)
        item.setPlace(self)
        self.map.addItem(item)

    def createCitizen(self, citizen):
        """
        Erstellt einen gegebenen Citizen komplett im gesamten Spiel
        :param citizen: Citizen
        :type citizen: Citizen
        """
        self.citizen.append(citizen)
        citizen.setPlace(self)
        self.map.addCitizen(citizen)
