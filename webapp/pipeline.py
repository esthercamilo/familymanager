from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(' — headless')
chrome_options.add_argument(' — no-sandbox')
chrome_options.add_argument(' — disable-dev-shm-usage')

driver =webdriver.Chrome('chromedriver',chrome_options=chrome_options)
driver.get("http://192.168.0.1/")

searchinput = driver.find_element_by_id("password")
searchinput.send_keys("c&mfqt17")
time.sleep(2)

searchinput.send_keys(Keys.ENTER)
time.sleep(2)

alert_box = driver.switch_to.alert
alert_box.accept()

mac_lele = "988389e7101c"
mac_lulu = "c8c7503c8d9e"

driver.get("http://192.168.0.1/fw-macfilter.htm")
time.sleep(5)

inputmac = "//*[@id=\"body_header\"]/tbody/tr[2]/td/table/tbody/tr[4]/td[2]/input"
searchinputmac = driver.find_element_by_xpath(inputmac)
searchinputmac.send_keys(mac_lele)
time.sleep(5)

addmac = "//*[@id=\"maincontent\"]/form[2]/p/input[1]"
btnaddmac = driver.find_element_by_xpath(addmac)
btnaddmac.click()

# driver.close()
# driver.quit()