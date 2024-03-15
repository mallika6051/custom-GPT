# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# import time
# from time import sleep
#
# driver = webdriver.Chrome()
# driver.get('http://www.google.com')
# elem = driver.find_element_by_id('input')
# time.sleep(5)
# elem.clear()
# elem.send_keys("Python")
# elem.send_keys(Keys.RETURN)



from selenium import webdriver  # Add this import statement
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get('http://www.google.com')

try:
    elem = WebDriverWait(driver, 40).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="input"]'))
    )
    elem.clear()
    elem.send_keys("Browser Automation")
    elem.send_keys(Keys.RETURN)
finally:
    driver.quit()
