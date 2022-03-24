from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="E:/browsers/chromedriver.exe")
driver.get("https://demoqa.com/webtables")
# ele=driver.find_element_by_class_name("text")
ele=driver.find_element_by_xpath("//*[@id='app']/div/div/div[2]/div[2]/div[1]/div[3]/div[2]/div/div[2]/span[2]/select")
# ele=driver.find_element_by_xpath("//*[@id='example']/div[4]/div/div[2]/div[4]/div[1]/div[2]/div")
dropDown=Select(ele)
dropDown.select_by_index(1)
s=dropDown.options
print(type(s))
for i in s:
    print(i.text)
driver.close()