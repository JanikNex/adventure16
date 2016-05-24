class DialogueHandler(object):
    def __init__(self, game):
        self.game = game
        self.text = None
        self.currentRow = None
        self.inDialogue = False
        self.step = 0
        self.buttonArray = []
        self.textOutput = ''
        self.prestigeChange = 0

    def startDialogue(self, text):
        if not self.inDialogue:
            self.text = text
            self.inDialogue = True
            self.game.getPlayer().startInteractWith(self)
            self.updateParameter()
            return ''

    def endDialogue(self):
        if self.inDialogue:
            self.inDialogue = False
            self.currentRow = None
            self.text = None
            self.step = 0
            self.game.getPlayer().endInteraction()

    def getButtonArray(self, mode = 'all'):
        if len(self.buttonArray) == 0 or (len(self.buttonArray[0]) == 0 and len(self.buttonArray[1]) == 0 and len(self.buttonArray[2]) == 0):
            return []
        else:
            if mode == 'all':
                return self.buttonArray
            elif mode == 'text':
                return [self.buttonArray[0][0], self.buttonArray[1][0], self.buttonArray[2][0]]
            elif mode == 'goto':
                return [self.buttonArray[0][1], self.buttonArray[1][1], self.buttonArray[2][1]]

    def getTextOutput(self):
        return self.textOutput

    def getPrestigeChange(self):
        return self.prestigeChange

    def updateParameter(self):
        if self.inDialogue:
            self.currentRow = self.text[self.step]
            self.textOutput = self.currentRow[2]
            if self.currentRow[1] == 'P':
                self.prestigeChange = self.currentRow[4]
            else:
                self.prestigeChange = 0
            if self.currentRow[1] == 'C':
                self.buttonArray = self.currentRow[3]
            else:
                self.buttonArray = []

    def nextStep(self, select=None):
        #self.updateParameter()
        if select is None:
            if self.currentRow[1] == 'P':
                if self.currentRow[3] == -1:
                    self.endDialogue()
                else:
                    self.step = self.currentRow[3]
            elif self.currentRow[1] == 'C':
                if self.currentRow[4] is not None:
                    if self.currentRow[4] == -1:
                        self.endDialogue()
                    else:
                        self.step = self.currentRow[4]
        elif 0 <= select < 3:
            if self.currentRow[1] == 'P':
                pass  # Sollte nicht passieren
            elif self.currentRow[1] == 'C':
                self.step = self.getButtonArray('goto')[select]
        self.updateParameter()

    def isInDialogue(self):
        return self.inDialogue
