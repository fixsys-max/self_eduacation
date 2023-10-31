import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


driver = webdriver.Chrome()

ulr = 'https://www.random.org/dice/'
driver.get(ulr)

button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[value="Roll Dice"]')))
button.click()

time.sleep(5)
driver.quit()
