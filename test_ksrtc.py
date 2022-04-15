import random
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.common.by import by
# from selenium.webdriver.support.select import select
from selenium.webdriver.support.wait import WebDriverWait
wait = WebDriverWait(driver,20)
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://ksrtc.in/oprs-web/")
driver.implicitly_wait(10)
driver.maximize_window()
from_place=driver.find_element_by_id("fromPlaceName")
from_place.send_keys("ben")
# time.sleep(5)
from_link = wait.until(EC visibility_of_element_located("//a[text()='BENGALURU']"))
from_link.click()
# time.sleep(5)