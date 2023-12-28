from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from source.contract.insertDataIntoFields import insertDataIntoFields


class actionsTypeSelect(insertDataIntoFields):

    def fill(self):

        if self.identifier == "XPATH":
           self.WaitAndSelectByName()

    def WaitAndSelectByName(self):
        X = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, self.objectName)))
        WebDriverWait(self.driver, 40).until(EC.element_to_be_clickable((X)))
        Select(self.driver.find_element(By.XPATH, self.objectName)).select_by_value(self.value)


