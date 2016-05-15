from src.cinventory import *


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
        return self.interactingWith is not None

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
                if self.place.getPlaceInDirection(0).canEnter():
                    self.enterPlace(self.place.getPlaceInDirection(0))
                else:
                    return False
            elif self.facing == 'e':
                if self.place.getPlaceInDirection(1).canEnter():
                    self.enterPlace(self.place.getPlaceInDirection(1))
                else:
                    return False
            elif self.facing == 's':
                if self.place.getPlaceInDirection(2).canEnter():
                    self.enterPlace(self.place.getPlaceInDirection(2))
                else:
                    return False
            elif self.facing == 'w':
                if self.place.getPlaceInDirection(3).canEnter():
                    self.enterPlace(self.place.getPlaceInDirection(3))
                else:
                    return False
        return False

    def getPossibleDirections(self):
        return self.getPlace().getNeigbours()

    def getFacing(self):
        return self.facing

    def setFacing(self, direction):
        self.facing = direction

    def getPrestige(self):
        return self.prestige

    def setPrestige(self, new):
        self.prestige = new

    def decreasePrestige(self, value):
        self.prestige -= value

    def increasePrestige(self, value):
        self.prestige += value

    def canMove(self):
        if self.isInteracting() and (len(self.getPossibleDirections())-self.getPossibleDirections().count(None)) == 4:
            return False
        else:
            return True
