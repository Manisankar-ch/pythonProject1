from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains


driver=webdriver.Chrome(r"E:\browsers\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
ele=driver.find_element_by_xpath("/html/body/div[4]/div/fieldset/legend")
driver.execute_script("arguments[0].scrollIntoView();",ele)
mouse=driver.find_element_by_id("mousehover")
place=driver.find_element_by_xpath("/html/body/div[4]/div/fieldset/div/div/a[1]")
act=ActionChains(driver)
act.move_to_element(mouse).move_to_element(place).click().perform()
driver.close()