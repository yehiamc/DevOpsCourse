from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# driver = webdriver.Chrome(executable_path="/Users/yehiamc/Downloads/chromedriver")
# driver.implicitly_wait(10)
# driver.get("https://translate.google.com")
# print(driver.current_url)
# print(driver.title)
# print(driver.page_source)
# driver.find_element_by_id("source").click()
# # elements = driver.find_elements_by_id("source")
# # print(len(elements))
# # element1 = elements[0]
# # driver.find_element_by_xpath()
# elements = driver.find_elements_by_id("source")
# # driver.find_element_by_id("source").send_keys("Hello")
# x = driver.find_element_by_id("source")
# if x.is_enabled() == True:
#     x.click()
#     x.send_keys("Hello")
# elements = driver.find_element_by_id("source").send_keys(Keys.ENTER)
# if x.get_attribute("autocapitalize") == "off":
#     print("Off")
#
# driver.quit()
driver = webdriver.Chrome(executable_path="/Users/yehiamc/Downloads/chromedriver")
driver.implicitly_wait(10)
driver.get("https://gofile.io/?t=uploadFiles")
driver.find_element_by_id("btnChooseFiles").send_keys("/Users/yehiamc/Downloads/trash.jpeg")
driver.quit()
