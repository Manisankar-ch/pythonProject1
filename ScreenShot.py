from selenium import webdriver
# driver=webdriver.Chrome(r"E:\browsers\chromedriver.exe")
driver=webdriver.Firefox(executable_path=r"E:\browsers\geckodriver.exe")
driver.get("https://www.google.com")
driver.save_screenshot("E:\ScreenShot\homepage1.jpeg")
driver.close()