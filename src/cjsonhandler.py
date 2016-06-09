import json as js


class JSONHandler(object):
    def __init__(self):
        self.filepath = None
        self.data = None

    def openNewFile(self, path):
        self.data = None
        self.filepath = path
        try:
            with open('json/'+str(path)) as data:
                self.data = js.load(data)
        except:
            print('FileSystem Error: Could not open JSON File!')

    def getData(self):
        return self.data


t = JSONHandler()
t.openNewFile("testdialogue.json")
print(t.getData())