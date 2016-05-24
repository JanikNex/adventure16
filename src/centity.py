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
        return self.name

    def getPlace(self):
        return self.place

    def setPlace(self, place):
        self.place = place

    def getMap(self):
        return self.map

    def getDescription(self):
        return self.description

    def getActions(self):
        return self.actions

    def setActions(self, actions):
        for e in actions:
            self.actions.append(self.__actionDatabase[e])

    def getActionCount(self):
        if len(self.actions) == 0:
            return -1
        return len(self.actions)

    def getActionsAsString(self):
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
