import time
import names
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from source.contract.insertDataIntoFields import insertDataIntoFields


class actionsTypeInput(insertDataIntoFields):

    def fill(self):
        if  self.identifier=="XPATH":
            self.WaitAndSendTextByXpath()
        elif self.identifier=="XPATHNAME":
            self.WaitAndSendTextByXpathName()
       # elif self.identifier=="ID":
        #    self.WaitAndSendTextByID()


    def WaitAndSendTextByXpath(self):
      w = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, self.objectName)))
      WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((w)))
      self.driver.find_element(By.XPATH, self.objectName).click()
      time.sleep(1)

    def WaitAndSendTextByXpathName(self):
       L = WebDriverWait(self.driver, 200).until(EC.visibility_of_element_located((By.XPATH, self.objectName)))
       L.send_keys(self.value)

    #def WaitAndSendTextByID(self):
     #   WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.ID, self.objectName))).click()



