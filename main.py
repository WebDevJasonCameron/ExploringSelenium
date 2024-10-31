from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

service = Service(executable_path = "/Users/jasoncameron/Desktop/Learning/Exploration/Exploring_Selenium/chromedriver")
driver = webdriver.Chrome(service = service)

driver.get("https://google.com")

time.sleep(10)

driver.quit()