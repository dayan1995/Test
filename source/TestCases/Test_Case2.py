import time
import pytest
import unittest
from source.helper.readAndFillData import readAndFillData
from source.helper.readDataJson import readDataJson

@pytest.mark.usefixtures("init_driver")
class TestCase2(unittest.TestCase):
    def test_daily(self):
        self.driver.maximize_window()
        # read the file
        datafiles = ["data_daily_fares"]
        self.dataJson = readDataJson(datafiles).readData()
        # Login and Welcome Page
        # scroll through the information
        readAndFillData(self.driver, self.dataJson["Search-daily-fares"]).readAndFill()
        time.sleep(10)





