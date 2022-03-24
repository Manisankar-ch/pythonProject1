from selenium import webdriver
import time
from selenium.webdriver.common.by import By


driver=webdriver.Chrome(r"E:\browsers\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
row=len(driver.find_elements_by_xpath("/html/body/div[3]/div[2]/fieldset[2]/div[1]/table/tbody/tr"))
col=len(driver.find_elements_by_xpath("/html/body/div[3]/div[2]/fieldset[2]/div[1]/table/tbody/tr[1]/td"))
print(row,col)
ele= driver.find_element_by_xpath("/html/body/div[3]/div[2]/fieldset[2]/legend")
driver.execute_script("arguments[0].scrollIntoView();",ele)
for i in range(1,row+1):
    for j in range(1,col+1):
        value=driver.find_element_by_xpath("/html/body/div[3]/div[2]/fieldset[2]/div[1]/table/tbody/tr["+str(i)+"]/td["+str(j)+"]").text
        print(value,end="      ")
    print()
driver.close()
# /html/body/div[3]/div[2]/fieldset[2]/div[1]/table/tbody/tr[2]/td[2]