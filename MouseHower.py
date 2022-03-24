from selenium import webdriver
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


driver=webdriver.Chrome(r"E:\browsers\chromedriver.exe")
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.find_element_by_id("txtUsername").send_keys("Admin")
driver.find_element_by_id("txtPassword").send_keys("admin123")
driver.find_element_by_id("btnLogin").click()
time.sleep(3)
admin=driver.find_element_by_xpath("//*[@id='menu_admin_viewAdminModule']/b")
user_m=driver.find_element_by_xpath("//*[@id='menu_admin_UserManagement']")
users=driver.find_element_by_xpath("//*[@id='menu_admin_viewSystemUsers']")
action=ActionChains(driver)
action.move_to_element(admin).move_to_element(user_m).move_to_element(users).click().perform()