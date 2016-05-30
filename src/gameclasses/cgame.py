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
        self.player.enterPlace(self.map.getPlacePerID(0))

    def getPlayer(self):
        """
        Gibt den Spieler zurück
        :return: Spieler
        :rtype: Player
        """
        return self.player

    def getMap(self):
        """
        Gibt die Map zurück
        :return: Map
        :rtype: Map
        """
        return self.map

    def getAudioHandler(self):
        """
        Gibt den AudioHandler zurück
        :return: AudioHandler
        :rtype: AudioHandler
        """
        return self.audioHandler

    def getDialogueHandler(self):
        """
        Gibt den DialogueHandler zurück
        :return: DialoguHandler
        :rtype: DialogueHandler
        """
        return self.dialogueHandler

    def updateAudioHandler(self):
        """
        Updated den AudioHandler auf den SoundPath des aktuellen Standorts des Spielers
        """
        if self.player.getPlace().getSound() == '':
            self.audioHandler.stop()
        else:
            self.audioHandler.setFilePath(self.player.getPlace().getSound())
            self.audioHandler.play()
