from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# use customized
# s = Service("/usr/local/bin/chromedriver")

options = Options()
options.headless = True
options.add_experimental_option("detach", True) # to keep browser open

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)


def loadWeb():
    driver.get("https://google.com")

loadWeb()
