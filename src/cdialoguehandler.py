class DialogueHandler(object):
    def __init__(self, game):
        self.inDialogue = False
        self.citizenText = []
        self.protagonistText = []
        self.nextTalker = None
        self.stepProtagonist = 0
        self.stepCitizen = 0
        self.needAnswer = False
        self.reactionArray = []
        self.game = game


    def endDialogue(self):
        if self.inDialogue:
            self.inDialogue = False
            self.citizenText = []
            self.protagonistText = []
            self.nextTalker = None
            self.stepCitizen = 0
            self.stepProtagonist = 0
            self.reactionArray = []
            self.game.getPlayer.endInteraction()

    def startDialogue(self, text=[[],[]], start = 'p'):
        if not self.inDialogue and not self.game.getPlayer().isInteracting():
            self.inDialogue = True
            self.game.getPlayer.startInteractionWith(self)
            self.citizenText = text[0]
            self.protagonistText = text[1]
            self.nextTalker = start

    def isInDialogue(self):
        return self.inDialogue

    def nextStep(self, select = None):
        if self.inDialogue:
            if select is None and not self.needAnswer:
                if self.nextTalker == 'c':
                    self.nextTalker = 'p'
                    text = self.citizenText[self.stepCitizen][0]
                    buttons = [self.citizenText[self.stepCitizen][1][0], self.citizenText[self.stepCitizen][2][0], self.citizenText[self.stepCitizen][3][0]]
                    reactionText = [self.citizenText[self.stepCitizen][1][1], self.citizenText[self.stepCitizen][2][1], self.citizenText[self.stepCitizen][3][1]]
                    self.reactionArray = self.citizenText[self.stepCitizen][4]
                    if not buttons == [[],[],[]]:
                        self.needAnswer = True
                    else:
                        self.needAnswer = False
                    return [text, buttons, reactionText]
                elif self.nextTalker == 'p':
                    self.nextTalker = 'c'
                    self.stepCitizen = self.protagonistText[self.stepProtagonist][1]
                    return self.protagonistText[self.stepProtagonist][0]
            elif self.needAnswer and select is not None:
                if self.nextTalker == 'c':
                    self.nextTalker = 'p'
                    text = self.citizenText[self.stepCitizen][0]
                    buttons = [self.citizenText[self.stepCitizen][1][0], self.citizenText[self.stepCitizen][2][0],
                               self.citizenText[self.stepCitizen][3][0]]
                    reactionText = [self.citizenText[self.stepCitizen][1][1], self.citizenText[self.stepCitizen][2][1],
                                    self.citizenText[self.stepCitizen][3][1]]
                    self.reactionArray = self.citizenText[self.stepCitizen][4]
                    if not buttons == [[], [], []]:
                        self.needAnswer = True
                    else:
                        self.needAnswer = False
                    return [text, buttons, reactionText]
                elif self.nextTalker == 'p':
                    self.nextTalker = 'c'
                    self.stepProtagonist = self.reactionArray[select]
                    self.stepCitizen = self.protagonistText[self.stepProtagonist][1]
                    return self.protagonistText[self.stepProtagonist][0]
