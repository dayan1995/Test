import time
import pytest
import unittest

@pytest.mark.usefixtures("init_driver")
class TestCase1(unittest.TestCase):
    def test_search(self):
        from source.helper.readAndFillData import readAndFillData
        from source.helper.readDataJson import readDataJson
        self.driver.maximize_window()
        # read the file
        datafiles = ["data_search"]
        self.dataJson = readDataJson(datafiles).readData()
        # Login and Welcome Page
        # scroll through the information
        readAndFillData(self.driver, self.dataJson["Search-one-way"]).readAndFill()
        time.sleep(10)










