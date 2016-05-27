from src.gameclasses.cinventory import *


class Player(object):
    def __init__(self, game):
        self.game = game
        self.place = None
        self.prestige = 0
        self.inventory = Inventory(self)
        self.interactingWith = None
        self.facing = 'n'

    def getPlace(self):
        """
        Gibt den aktuellen Standort des Spielers zurück
        :return: Place
        """
        return self.place

    def setPlace(self, place):
        """
        Setzt den aktuellen Standort des Spielers
        :rtype: Place
        :param place: object
        """
        self.place = place

    def dropItem(self, index):
        """
        Drops ein Item aus dem Inventar am momentanen Aufenthaltsort des Spielers
        :param index: bool
        """
        self.inventory.getItem(index).drop()
        self.inventory.removeItem(index)

    def isInteracting(self):
        """
        Gibt True oder False zurück, ob der Spieler gerade mit etwas interagiert
        :return: bool
        """
        return self.interactingWith != None

    def enterPlace(self, place):
        """
        Betritt einen neuen Platz
        :rtype: Place
        :param place: Neuer Auenthaltsort
        """
        self.setPlace(place)
        self.game.updateAudioHandler()

    def goDirection(self):
        """
        Lässt den Spieler in die Richtung laufen, in welche er zuletzt geschaut hat
        :rtype: bool
        :return: Erfolgreich?
        """
        if self.place.canLeave() and not self.isInteracting():
            if self.facing == 'n':
                if self.place.getNeigbours()[0] is not None:
                    if self.place.getPlaceInDirection(0).canEnter():
                        self.enterPlace(self.place.getPlaceInDirection(0))
                        return True
                else:
                    return False
            elif self.facing == 'e':
                if self.place.getNeigbours()[1] is not None:
                    if self.place.getPlaceInDirection(1).canEnter():
                        self.enterPlace(self.place.getPlaceInDirection(1))
                        return True
                else:
                    return False
            elif self.facing == 's':
                if self.place.getNeigbours()[2] is not None:
                    if self.place.getPlaceInDirection(2).canEnter():
                        self.enterPlace(self.place.getPlaceInDirection(2))
                        return True
                else:
                    return False
            elif self.facing == 'w':
                if self.place.getNeigbours()[3] is not None:
                    if self.place.getPlaceInDirection(3).canEnter():
                        self.enterPlace(self.place.getPlaceInDirection(3))
                        return True
                else:
                    return False
        return False

    def getPossibleDirections(self):
        """
        Gibt angrenzende Orte an aktuellen Standort zurück
        :return: Liste der angerenzenden Orte
        :rtype: list
        """
        return self.getPlace().getNeigbours()

    def getFacing(self):
        """
        Gibt aktuelle Blickrichtung des Spielers zurück
        :return: Richtung
        :rtype: char
        """
        return self.facing

    def setFacing(self, direction):
        """
        Setzt Blickrichtung auf gegebenen char
        :param direction: neue Blickrichtung
        :type direction: char
        """
        self.facing = direction

    def getPrestige(self):
        """
        Gibt Prestige des Spielers zurück
        :return: Prestige des Spielers
        :rtype: int
        """
        return self.prestige

    def getInventory(self):
        """
        Gibt Inventarobjekt des Spielers zurück
        :return: Inventar
        :rtype: Item
        """
        return self.inventory

    def setPrestige(self, new):
        """
        Setzt Prestige des Spielers auf gegebenen Wert
        :param new: neuer Prestige-Wert
        :type new: int
        """
        self.prestige = new

    def decreasePrestige(self, value):
        """
        Verringert Prestige-Wert des Spielers um gegebenen Wert
        :param value: Wert, um den Prestige verringert werden soll
        :type value: int
        """
        self.prestige -= value

    def increasePrestige(self, value):
        """
        Erhöht Prestige-Wert des Spielers um gegebenen Wert
        :param value: Wert, um den Prestige erhöht werden soll
        :type value: int
        """
        self.prestige += value

    def startInteractWith(self, object):
        """
        Startet Interaktion des Spielers mit gegebenem Objekt
        :param object: Interaktionsobjekt
        :type object: object
        """
        if not self.isInteracting():
            self.interactingWith = object

    def endInteraction(self):
        """
        Beendet aktuelle Interaktion des Spielers
        """
        self.interactingWith = None

    def getInteraction(self):
        """
        Gibt Objekt, mit dem der Spieler gerade interargiert zurück
        :return: Interaktionsobjekt
        :rtype: Entity
        """
        return self.interactingWith

    def pickUpItem(self, item):
        """
        Hebt ein Item vom aktuellen Standort auf und packt es ins Inventar
        :param item: Item, welches aufgehoben werden soll
        :type item: Item
        """
        if not self.inventory.isFull() and not item.inInventory():
            item.take()
            self.inventory.addItem(item)
            self.place.removeItem(item)

    def canMove(self):
        """
        Kann sich der Spieler momentan bewegen?
        :return: Antwort
        :rtype: bool
        """
        if self.isInteracting() or (len(self.getPossibleDirections()) - self.getPossibleDirections().count(None)) == 4:
            return False
        else:
            return True

    def nextInteraction(self, button=None):
        """
        Geht in den nächsten Interaktionsschritt mit
         :param button: Index des Buttons, falls die Funktion durch anklicken eines Buttons aufgerufen wurde
         :type button: int
        """
        # if self.interactingWith.__class__.__name__ == 'DialogueHandler':
        self.game.getDialogueHandler().nextStep(button)