import time
import pytest
import unittest
from source.helper.readAndFillData import readAndFillData
from source.helper.readDataJson import readDataJson
from Test_Case2 import TestCase2

@pytest.mark.usefixtures("init_driver")
class TestCase1(unittest.TestCase):
    def test_search(self):
        self.driver.maximize_window()
        # read the file
        datafiles = ["data_search"]
        self.dataJson = readDataJson(datafiles).readData()
        # Login and Welcome Page
        # scroll through the information
        readAndFillData(self.driver, self.dataJson["Search-one-way"]).readAndFill()
        time.sleep(10)










