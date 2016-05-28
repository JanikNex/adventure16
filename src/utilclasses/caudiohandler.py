import winsound


class AudioHandler(object):
    def __init__(self, filepath):
        """
        Erstellt neuen AudioHandler
        :param filepath: Pfad zu Audiodatei oder None
        :type filepath: str or None
        """
        self.playing = False
        self.file = filepath
        if self.file is not None:
            self.file = "src/wav/"+str(self.file)+".wav"

    def play(self):
        """
        Beginnt mit der Wiedergabe des aktuellen Soundpaths
        """
        if not self.playing:
            self.playing = True
            winsound.PlaySound(self.file, winsound.SND_FILENAME | winsound.SND_LOOP | winsound.SND_NODEFAULT | winsound.SND_ASYNC)

    def stop(self):
        """
        Stoppt die Wiedergabe
        """
        if self.playing:
            self.playing = False
            winsound.PlaySound(None, 0)

    def setFilePath(self, filepath):
        """
        Stoppt die Wiedergabe und setzt den neuen Filepath
        :param filepath: Neuer Filepath zu Audiodatei
        :type filepath: str
        """
        self.stop()
        self.file = filepath
        if self.file is not None:
            self.file = "wav/" + str(self.file) + ".wav"
