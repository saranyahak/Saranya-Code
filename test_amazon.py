import time
# import pytest
from selenium import webdriver
# from selenium.webdriver.support.select import select
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())

def test_login():
    driver.get("https://www.amazon.in/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.in%2F%3F%26ext_vrnc%3Dhi%26tag%3Dgooghydrabk1-21%26ref%3Dnav_custrec_signin%26adgrpid%3D58355126069%26hvpone%3D%26hvptwo%3D%26hvadid%3D486458755421%26hvpos%3D%26hvnetw%3Dg%26hvrand%3D15063874882359933936%26hvqmt%3De%26hvdev%3Dc%26hvdvcmdl%3D%26hvlocint%3D%26hvlocphy%3D9303553%26hvtargid%3Dkwd-10573980%26hydadcr%3D14453_2154373%26gclid%3DCj0KCQjw0umSBhDrARIsAH7FCoeonxfY22YXYqRpAR-k-0j2brPHHZhpuGZZ654tCMmwBa4G3cyoxPEaAlqVEALw_wcB&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=inflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&")
    # driver.get('https://www.amazon.in/')
    driver.maximize_window()
    time.sleep(1)

    # sign_in=driver.find_element_by_id('nav-link-accountList-nav-line-1')
    # sign_in.click()
    # time.sleep(5)



    signin = driver.find_element_by_id('ap_email')
    signin.send_keys("username")
    submit = driver.find_element_by_id('continue')
    submit.click()

    password = driver.find_element_by_id('ap_password')
    password.send_keys("password")
    signin_sunmit = driver.find_element_by_id('signInSubmit')
    signin_sunmit.click()

    mobile = driver.find_element_by_xpath("//a[text()='Mobiles']")
    mobile.click()


    samsung_check_box = driver.find_element_by_xpath('//span[text()="Samsung"]')
    samsung_check_box.click()

    max_price = driver.find_element_by_id('low-price')
    max_price.send_keys("10000")
    min_price = driver.find_element_by_id('high-price')
    min_price.send_keys("20000")
    go_submit = driver.find_element_by_xpath('//input[@class="a-button-input"]')
    go_submit.click()