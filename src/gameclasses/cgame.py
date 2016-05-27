from src.gameclasses.cplayer import *
from src.gameclasses.cmap import *
from src.utilclasses.caudiohandler import *
from src.utilclasses.cdialoguehandler import *


class Game(object):
    def __init__(self):
        self.player = Player(self)
        self.map = Map(self)
        self.audioHandler = AudioHandler(None)
        self.dialogueHandler = DialogueHandler(self)
        self.player.enterPlace(self.map.getPlacePerName('Train'))

    def getPlayer(self):
        return self.player

    def getMap(self):
        return self.map

    def getAudioHandler(self):
        return self.audioHandler

    def getDialogueHandler(self):
        return self.dialogueHandler

    def updateAudioHandler(self):
        if self.player.getPlace().getSound() == '':
            self.audioHandler.stop()
        else:
            self.audioHandler.setFilePath(self.player.getPlace().getSound())
            self.audioHandler.play()