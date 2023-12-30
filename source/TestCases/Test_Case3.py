import time
import pytest
import unittest

@pytest.mark.usefixtures("init_driver")
class TestCase3(unittest.TestCase):
    def test_daily3(self):
        from source.helper.readAndFillData import readAndFillData
        from source.helper.readDataJson import readDataJson
        self.driver.maximize_window()
        # read the file
        datafiles = ["data_daily_Bussines"]
        self.dataJson = readDataJson(datafiles).readData()
        # Login and Welcome Page
        # scroll through the information
        readAndFillData(self.driver, self.dataJson["Search-daily-bussines"]).readAndFill()
        time.sleep(10)





