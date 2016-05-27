import json as js


class JSONHandler(object):
    def __init__(self):
        """
        Erstellt neuen JSONHandler
        """
        self.filepath = None
        self.data = None

    def openNewFile(self, path):
        """
        Öffnet eine Datei und speichert den Inhalt in self.data
        :param path: Dateiname aus /json/
        :type path: str
        """
        self.data = None
        self.filepath = path
        try:
            with open('json/'+str(path)+'.json') as data:
                self.data = js.load(data)
        except:
            print('FileSystem Error: Could not open JSON File!')

    def getData(self):
        """
        Gibt den Inhalt der zuletzt gelesenen JSON-Datei zurück
        :return: JSON-Inhalt
        """
        return self.data


if __name__ == '__main__':
    t = JSONHandler()
    t.openNewFile("testdialogue.json")
    print(t.getData())