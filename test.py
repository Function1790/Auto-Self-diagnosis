from selenium import webdriver

driver = webdriver.Chrome('C:/chromedriver.exe')
driver.get("http://naver.com")
elem1 = driver.find_element_by_id("query")
elem1.send_keys("셀레니움")

elem2 = driver.find_element_by_id("search_btn")
elem2.click()
