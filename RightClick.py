from selenium import webdriver
from selenium.webdriver import ActionChains

driver=webdriver.Chrome(r"E:\browsers/chromedriver.exe")
driver.get("https://demoqa.com/buttons")
ele=driver.find_element_by_id("rightClickBtn")
act=ActionChains(driver)
act.double_click(ele).click().perform()
driver.close()