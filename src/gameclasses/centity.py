class Entity(object):
    def __init__(self, map):
        self.name = ''
        self.place = None
        self.map = map
        self.description = ''
        self.actions = []
        self.__actionDatabase = ['Anschauen', 'Erinnerungen hervorrufen', 'Verlassen', 'Lesen', 'Ansprechen']
        self.quitPhrase = 'Exit'

    def getName(self):
        """
        Gibt den Namen der Entity zurück
        :return: Name
        :rtype: str
        """
        return self.name

    def getPlace(self):
        """
        Gibt den Ort der Entity zurück
        :return: Ort
        :rtype: object
        """
        return self.place

    def setPlace(self, place):
        """
        Setzt den Ort der Entity auf gegebenes Placeobject
        :param place: Placeobjekt
        :rtype: object
        """
        self.place = place

    def getMap(self):
        """
        Gibt Map des Spiels zurück
        :return: Map
        :rtype: object
        """
        return self.map

    def getDescription(self):
        """
        Gibt Beschreibung des Objekts zurück
        :return: Beschreibung
        :rtype: str
        """
        return self.description

    def getActions(self):
        """
        Gibt mögliche Actions zurück
        :return: Actions
        :rtype: str
        """
        return self.actions

    def setActions(self, actions):
        """
        Setzt Actions für dieses Objekt
        :param actions: Actions mit Index-Ints aus der actiondatabase
        :type actions: list
        """
        for e in actions:
            self.actions.append(self.__actionDatabase[e])

    def getActionCount(self):
        """
        Gibt die Anzahl der vorhandenen Aktionsmöglichkeiten zurück
        :return: Anzahl der Aktionen
        :rtype: int
        """
        if len(self.actions) == 0:
            return -1
        return len(self.actions)

    def getActionsAsString(self):
        """
        Gibt Interaktionsmöglichkeiten als String zurück
        :return: Interaktionsmöglichkeiten
        :rtype: str
        """
        text = 'Du hast folgende Interaktionsmöglichkeiten\n'
        actionCount = 0
        if not len(self.actions) == 0:
            for i in self.actions:
                text += str(actionCount) + ' - ' + i + '\n'
                actionCount += 1
        if len(self.actions) == 0:
            return ''
        return text

    def interact(self, interactionCall):
        """
        Führt eine gegebene Interaktion durch. Dafür wird der interactionCall mit den Interaktionen der action
        database abgeglichen und die pasende Funktion zurückgegeben
        :param interactionCall: Actioncode
        :type interactionCall: str
        :return: Methode
        :rtype function
        """
        if interactionCall in self.actions:
            if interactionCall == self.__actionDatabase[0]:
                return self.description
            elif interactionCall == self.__actionDatabase[1]:
                return self.inspection
            elif interactionCall == self.__actionDatabase[2]:
                self.map.getGame().getPlayer().endInteraction()
                return self.quitPhrase
            elif interactionCall == self.__actionDatabase[3]:
                self.getPlace().getMap().getGame().getPlayer().pickUpItem(self)
                return self.getContent()
            elif interactionCall == self.__actionDatabase[4]:
                return self.talk()