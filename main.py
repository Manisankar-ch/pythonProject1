import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(r"E:\browsers\chromedriver.exe")
driver.maximize_window()
driver.get("https://seleniumhq.github.io")
base_window=driver.current_window_handle
assert len(driver.window_handles)==1
driver.switch_to.new_window("window")
driver.get("https://www.guru99.com/selenium-python.html")
print(driver.title)
second_window = driver.current_window_handle
driver.maximize_window()
for window_handle in driver.window_handles:
    if window_handle==base_window:
        driver.switch_to.window(window_handle)
        print(driver.title)
        driver.close()
        break
driver.switch_to.window(second_window)
driver.switch_to.new_window("tab")
driver.get("https://www.facebook.com")
print(driver.title)






driver.close()

# driver.quit()
