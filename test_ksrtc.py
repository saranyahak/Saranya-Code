import random
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.common.by import by
# from selenium.webdriver.support.select import select
# from selenium.webdriver.support.wait import WebDriverWait
# wait = WebDriverWait(driver,20)
driver = webdriver.Chrome(ChromeDriverManager().install())
# wait = WebDriverWait(driver,20)
driver.get("https://ksrtc.in/oprs-web/")
# driver.implicitly_wait(10)
driver.maximize_window()
from_place=driver.find_element_by_id("fromPlaceName")
from_place.send_keys("ben")
time.sleep(5)
from_link =driver.find_element_by_xpath("//a[text()='BENGALURU']").click()
# from_link.click()
time.sleep(5)
to_place=driver.find_element_by_id("toPlaceName")
to_place.send_keys("AAT")
to_link =driver.find_element_by_xpath("//a[text()='AATINGAL']").click()
# to_link.click()
time.sleep(2)
date_picker = driver.find_element_by_id("txtJourneyDate")
date_picker.click()
time.sleep(5)
date_picker = driver.find_element_by_xpath("//a[text()='22']").click()
time.sleep(5)
search_for_bus = driver.find_element_by_xpath("//button[@class='btn btn-primary btn-lg btn-block btn-booking']").click()
# search_for_bus = driver.find_element_by_xpath("//button[normalize-space()='btn btn-primary btn-lg btn-block btn-booking']")
time.sleep(5)

driver.close()
