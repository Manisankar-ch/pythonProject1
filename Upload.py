from selenium import webdriver
from selenium.webdriver import ActionChains

driver=webdriver.Chrome(r"E:\browsers\chromedriver.exe")
driver.get("https://demoqa.com/upload-download")
driver.find_element_by_id("uploadFile").send_keys("E:\example.py")
val=driver.find_element_by_xpath("//*[@id='uploadedFilePath']").text
print(val)
driver.close()