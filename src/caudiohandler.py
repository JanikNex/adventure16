import winsound


class AudioHandler(object):
    def __init__(self, filepath):
        self.playing = False
        self.file = filepath

    def play(self):
        if not self.playing:
            self.playing = True
            winsound.PlaySound(self.file, winsound.SND_FILENAME | winsound.SND_LOOP | winsound.SND_NODEFAULT | winsound.SND_ASYNC)

    def stop(self):
        if self.playing:
            self.playing = False
            winsound.PlaySound(None, 0)
