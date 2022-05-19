from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request
import os

a = input("검색할 키워드를 입력하세요 : ")
b = int(input("개수 : "))

driver = webdriver.Chrome('크롬드라이버 경로')
driver.get('http://www.google.co.kr/imghp?hl=ko')

elem = driver.find_element_by_name("q")
elem.send_keys(a)
elem.send_keys(Keys.RETURN)
images = driver.find_elements_by_css_selector(".rg_i.Q4LuWd")
count = 0

for image in images:
    try:
        image.click()
        time.sleep(2)
        imgUrl = image.get_attribute("src")
        urllib.request.urlretrieve(imgUrl, "imgfile/img" + a + str(count)+ ".jpg")
        count += 1
        if count == b:
            break
    except:
        pass
    
driver.close()