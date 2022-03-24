from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="E:/browsers/chromedriver.exe")
driver.get("https://demoqa.com/select-menu")

ele=driver.find_element_by_xpath("//*[@id='selectMenuContainer']/div[7]/div/div/div/div[1]/div[1]")
tot=Select(ele)

for i in tot:
    print(i.text)

driver.close()
