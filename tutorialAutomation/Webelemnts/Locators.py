from selenium import webdriver

driver =webdriver.Chrome(executable_path="E:/browsers/chromedriver.exe")
driver.maximize_window()
driver.get("http://automationpractice.com/index.php")
driver.find_element_by_id("search_block_top").click()
driver.back()
driver.find_element_by_name("search_query").send_keys("mens")
driver.find_element_by_class_name("btn btn-default button-search").click()
driver.back()
driver.find_element_by_link_text("T-shirts")
driver.back()
