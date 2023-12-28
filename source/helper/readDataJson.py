import json

class readDataJson:
    def __init__(self, datafiles):
        self.files = datafiles
        self.dictionary = {}

    def readData(self):

        for jsonfiles in self.files:
            with open('../configuration/' + jsonfiles + '.json', encoding='utf-8') as file:
                datajson = json.load(file)
                self.dictionary.update(datajson)

        return self.dictionary