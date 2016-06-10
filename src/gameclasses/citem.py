from src.gameclasses.cinventory import *
from src.gameclasses.centity import *
from src.utilclasses.cjsonhandler import *


class Item(Entity):
    def __init__(self, map, itemid):
        """
        Erstellt ein neues Itemobjekt, welches auf einer Entity basiert. Zum erstellen werden die benötigten
        Informationen, pasend ur übergebenen ItemID, aus der JSON Datei ausgelesen.
        :param map: Map
        :param itemid: ItemID des Items in der JSON Datei
        :type map: Map
        :type itemid: int
        """
        Entity.__init__(self, map)
        jsonhandler = JSONHandler()
        jsonhandler.openNewFile('itemdata')
        self.name = jsonhandler.getData()[str(itemid)]['name']
        self.description = jsonhandler.getData()[str(itemid)]['description']
        self.texturePath = jsonhandler.getData()[str(itemid)]['texturepath']
        self.setActions(jsonhandler.getData()[str(itemid)]['actions'])
        self.canBeMoved = bool(jsonhandler.getData()[str(itemid)]['canBeMoved'])
        self.count = int(jsonhandler.getData()[str(itemid)]['count'])
        self.visible = jsonhandler.getData()[str(itemid)]['visible']
        print('[DEBUG] Generated', self.name)
        del jsonhandler

    def getTexture(self):
        """
        Gibt den Texturpfad zurück
        :return: texturepath
        :rtype: str
        """
        return self.texturePath

    def inInventory(self):
        """
        Gibt zurück, ob sich dieses Item im Spielerinventar befinded
        :rtype: bool
        """
        return self.map.getGame().getPlayer().getInventory().isItemInInventory(self)

    def drop(self, place):
        """
        Setzt den Ort dieses Items, falls es sich im Inventar befinded auf einen gegebenen Ort
        :param place: Place
        """
        if self.inInventory() and self.canBeMoved:
            self.setPlace(place)

    def take(self):
        """
        Setzt den Ort dieses Items, falls es sich nicht im Inventar befinded auf das Inventar des Spielers
        """
        if not self.inInventory() and self.canBeMoved:
            self.setPlace(self.getPlace().getMap().getGame().getPlayer().getInventory())

    def getCanBeMoved(self):
        """
        Gibt zurück, ob dieses Item bewegt werden kann.
        :rtype: bool
        """
        return self.canBeMoved

    def getCount(self):
        """
        Gibt die Anzahl des Objekts zurück.
        :rtype: int
        """
        return self.count

    def setCount(self, count):
        """
        Setzt die Anzahl des Objekts auf einen gegebenen Wert
        :param count: Neue Anzahl
        :type count: int
        """
        self.count = count


class Letter(Item):
    def __init__(self, map, itemid):
        """
        Erstellt ein LetterObjekt, welches ein Item mit Content-Zusatz ist.
        Durch eine Methode kann der content rurückgegeben werden und außerdem die Türen geschlossen werden, falls der
        Spieler sich zu dem Zeitpunkt im Zug befindet.
        :param map: Map
        :param itemid: ItemID des Items in der JSON Datei
        :type map: Map
        :type itemid: int
        """
        Item.__init__(self, map, itemid)
        jsonhandler = JSONHandler()
        jsonhandler.openNewFile('itemdata')
        self.content = jsonhandler.getData()[str(itemid)]['content']
        self.quitPhrase = 'Brief geschlossen'
        del jsonhandler

    def getContent(self):
        """
        Gibt den Inhalt des Briefs zurück, erlaubt das Verlassen des Zuges und verbietet das betreten.
        :rtype: str
        """
        if self.place.getPlayer().getPlace().getID() == 0:
            self.place.getPlayer().getPlace().getMap().getPlacePerID(0).allowExit()
            self.place.getPlayer().getPlace().getMap().getPlacePerID(0).denyEnter()
        return self.content


class GhostNote(Letter):
    def __init__(self, map, itemid):
        """
        Erstellt ein GhostNote Objekt, welches ein Brief ist, welcher allerdings beim lesen verschwindet
        (bzw unsichtbar wird)
        :param map: Map
        :param itemid: ItemID des Items in der JSON Datei
        :type map: Map
        :type itemid: int
        """
        Letter.__init__(self, map, itemid)
        self.quitPhrase = 'Notiz löste sich in Luft auf!'

    def getContent(self):
        """
        Gibt den Inhalt der Notiz zurück und lässt diese verschwinden.
        :rtype: str
        """
        self.hide()
        return self.content


class Key(Item):
    def __init__(self, map, itemid):
        """
        Erstelllt ein Key Objekt, welches ein Item ist, welches in der JSON gespeicherte Räume aufschließen kann.
        :param map: Map
        :param itemid: ItemID des Items in der JSON Datei
        :type map: Map
        :type itemid: int
        """
        Item.__init__(self, map, itemid)
        jsonhandler = JSONHandler()
        jsonhandler.openNewFile('itemdata')
        self.canOpen = jsonhandler.getData()[str(itemid)]['canOpen']

    def getCanOpen(self):
        """
        Gibt zurück, welcher Ort mit diesem Schlüssel geöffnet werden kann.
        :rtype: int
        """
        return self.canOpen


class Readable(Letter):
    def __init__(self, map, itemid):
        """
        Erstellt ein Readable Objekt, welches ein LEtterobjekt jedoch ohne den Zugtürschließzusatz ist
        :param map: Map
        :param itemid: ItemID des Items in der JSON Datei
        """
        Letter.__init__(self, map, itemid)
        self.quitPhrase = 'Verlassen.'

    def getContent(self):
        """
        Gibt den Inhalt zurück.
        :rtype: str
        """
        return self.content
