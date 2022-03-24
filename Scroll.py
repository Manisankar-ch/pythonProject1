from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Chrome(executable_path="E:/browsers/chromedriver.exe")
driver.maximize_window()
driver.get("https://www.tutorialspoint.com/index.htm")
driver.execute_script("window.scrollBy(0,1000)")
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
ele=driver.find_element_by_xpath("/html/body/div[4]/div[1]/div[1]/div/div[2]/a/img")
driver.execute_script("arguments[0].scrollIntoView();",ele)
print("Hello")
wb=WebDriverWait(driver,10)

