class Entity(object):
    def __init__(self, map):
        self.name = ''
        self.place = None
        self.map = map
        self.description = ''
        self.actions = []
        self.__actionDatabase = ['Anschauen', 'Erinnerungen hervorrufen', 'Verlassen', 'Lesen', 'Ansprechen',
                                 'Aufheben', 'Fallen lassen', 'Ansprechen ', 'Anschauen ', 'Betrachten']
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
        :rtype: Place
        """
        return self.place

    def setPlace(self, place):
        """
        Setzt den Ort der Entity auf gegebenes Placeobject
        :param place: Placeobjekt
        :type place: object
        """
        self.place = place

    def getMap(self):
        """
        Gibt Map des Spiels zurück
        :return: Map
        :rtype: Map
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
        :rtype: list
        """
        return self.actions

    def setActions(self, actions):
        """
        Setzt Actions für dieses Objekt
        :param actions: Actions mit Index-Ints aus der actiondatabase
        :type actions: list
        """
        self.actions = []
        for e in actions:
            self.actions.append(self.__actionDatabase[e])

    def replaceAction(self, old, new):
        """
        Ersetzt einen Actioncode durch einen neuen
        :param old: Alter Actioncode
        :param new: Neuer Actioncode
        """
        array = self.getActionCodes()
        for i in range(len(array)):
            if array[i] == old:
                array[i] = new
        self.setActions(array)

    def getActionCodes(self):
        array = []
        for i in self.actions:
            for e, n in enumerate(self.__actionDatabase):
                if i == n:
                    array.append(e)
        return array

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

    def isVisible(self):
        """
        Gibt zurück, ob diese Entity gerade sichtbar ist.
        :rtype: bool
        """
        return self.visible

    def hide(self):
        self.visible = False

    def show(self):
        self.visible = True

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
            # Anschauen
            if interactionCall == self.__actionDatabase[0]:
                return self.description
            # Erinnerungen hervorrufen
            elif interactionCall == self.__actionDatabase[1]:
                return self.inspection
            # Verlassen
            elif interactionCall == self.__actionDatabase[2]:
                self.map.getGame().getPlayer().endInteraction()
                return self.quitPhrase
            # Lesen
            elif interactionCall == self.__actionDatabase[3]:
                self.getPlace().getMap().getGame().getPlayer().pickUpItem(self)
                return self.getContent()
            # Ansprechen
            elif interactionCall == self.__actionDatabase[4]:
                return self.talk()
            # Aufheben
            elif interactionCall == self.__actionDatabase[5]:
                self.getMap().getGame().getPlayer().pickUpItem(self)
                self.replaceAction(5, 6)
                self.map.getGame().getPlayer().endInteraction()
                return 'Aufgehoben!'
            # Fallen lassen
            elif interactionCall == self.__actionDatabase[6]:
                self.getMap().getGame().getPlayer().dropItem(self)
                self.replaceAction(6, 5)
                self.map.getGame().getPlayer().endInteraction()
                return 'Fallen gelassen!'
            # Ansprechen und Citizen verstecken
            elif interactionCall == self.__actionDatabase[7]:
                self.hide()
                return self.talk()
            # Anschauen und Citizen verstecken
            elif interactionCall == self.__actionDatabase[8]:
                self.hide()
                return self.description
            elif interactionCall == self.__actionDatabase[9]:
                return self.getContent()
