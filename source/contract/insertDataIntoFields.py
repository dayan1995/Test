from abc import ABC, abstractmethod

class insertDataIntoFields(ABC):
    def __init__(self, driver, name, identifier=None, value=None):
        self.driver = driver
        self.identifier = identifier
        self.objectName = name
        self.value = value

    @abstractmethod
    def fill(self):
        pass

