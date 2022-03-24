from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="E:/browsers/chromedriver.exe")
driver.get("https://demoqa.com/select-menu")
ele=driver.find_element_by_id("cars")

lis=Select(ele)
total=lis.options
for i in total:
    print(i.text)
driver.close()

