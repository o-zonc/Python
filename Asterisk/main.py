from asyncore import socket_map
import random
from selenium import webdriver

import webdriverinstaller as wdinstall
import PyQtUI

# 옵션 생성
options = webdriver.ChromeOptions()
# 창 숨기는 옵션 추가
options.add_argument("headless")

# id와 비밀번호 가져오기
id = PyQtUI.
password = 'something else'

# 드라이버를 가져오고 로그인하기
driver = webdriver.Chrome(wdinstall.driver_path)
driver.implicitly_wait(1)
driver.get("https://everytime.kr/login")
driver.find_element_by_id("userid").send_keys(f"{id}")
driver.find_element_by_id("password").send_keys(f"{password}")
driver.find_element_by_xpath("//*[@class='submit']/input").click()
driver.implicitly_wait(random.random(1,3))

# 드라이버 창 닫기
# driver.quit()