import os
import time
from source.actions.actionsTypeInput import actionsTypeInput
from source.actions.actionsTypeSelect import actionsTypeSelect

class readAndFillData:
    def __init__(self, driver, data):
        self.driver = driver
        self.dataList = data

    def readAndFill(self):
        for dictionary in self.dataList:
            if dictionary["fieldType"] == 'SELECT':
                select = actionsTypeSelect(self.driver, dictionary["fieldName"], dictionary["fieldIdentifier"],os.path.expandvars(dictionary["fieldValue"]))
                select.fill()
            elif dictionary["fieldType"] == 'INPUT':
                input = actionsTypeInput(self.driver, dictionary["fieldName"], dictionary["fieldIdentifier"], os.path.expandvars(dictionary["fieldValue"]))
                input.fill()