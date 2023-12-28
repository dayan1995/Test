import pytest
from selenium import webdriver
import os
from dotenv import load_dotenv
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="class")
def init_driver(request):
    pass
    load_dotenv()
    options = Options()
    options.add_argument("start-maximized")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_experimental_option('useAutomationExtension', False)
    options.add_argument('--disable-blink-features=AutomationControlled')
    driver = webdriver.Chrome(options=options)
    url = os.getenv('URL')
    driver.get(url)
    request.cls.driver = driver
    yield