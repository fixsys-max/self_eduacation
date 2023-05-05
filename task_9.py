import time
import random

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


driver = webdriver.Chrome()
driver.get('https://www.random.org/coins/')

select_flip = Select(driver.find_element(By.CSS_SELECTOR, 'select[name="num"]'))
select_flip.select_by_value('1')

select_coin = Select(driver.find_element(By.CSS_SELECTOR, 'select[name="cur"]'))
select_coin.select_by_index(random.randint(1, 88))

driver.find_element(By.CSS_SELECTOR, 'input[value="Flip Coin(s)"]').click()

time.sleep(5)
driver.quit()
