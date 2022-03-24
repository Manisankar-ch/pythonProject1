import time

from selenium import webdriver
from selenium.webdriver.common.alert import Alert

driver  = webdriver.Chrome(executable_path="E:/browsers/chromedriver.exe")
driver.get("http://demo.automationtesting.in/Alerts.html")


driver.find_element_by_xpath('//*[@id="OKTab"]/button').click()
time.sleep(5)
al=Alert(driver)
al.accept()

driver.close()
