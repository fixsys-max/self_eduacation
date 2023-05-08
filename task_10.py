import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--disable-notifications")
options.add_argument("--disable-geolocation")

driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 5)

try:
    driver.get('https://rozetka.com.ua/')

    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'li.header-actions__item--user button.header__button'))).click()
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.form__row button.auth-modal__register-link'))).click()
    wait.until(EC.presence_of_element_located((By.ID, 'registerUserName'))).send_keys('Имя')
    wait.until(EC.presence_of_element_located((By.ID, 'registerUserSurname'))).send_keys('Фамилия')
    wait.until(EC.presence_of_element_located((By.ID, 'registerUserPhone'))).send_keys('0961234567')
    wait.until(EC.presence_of_element_located((By.ID, 'registerUserEmail'))).send_keys('test_email@example.com')
    wait.until(EC.presence_of_element_located((By.ID, 'registerUserPassword'))).send_keys('QwAsZx!2')

finally:
    time.sleep(3)
    driver.quit()
