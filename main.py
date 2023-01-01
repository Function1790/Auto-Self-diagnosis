from selenium.webdriver.remote.webelement import WebElement
from selenium import webdriver
from time import sleep

data = {
    "school": "한양고등학교",
    "name": "홍길동",
    "birth": "230101",
    "passwd": "0000"
}

url = "https://hcs.eduro.go.kr/#/none"

driver = webdriver.Chrome('C:/chromedriver.exe')
driver.get(url)


def findById(id) -> WebElement:
    return driver.find_element_by_id(id)


def findByClass(className) -> WebElement:
    return driver.find_element_by_class_name(className)
    

# 로그인 시작
findById("btnConfirm2").click()

# 학교 찾기
findById("schul_name_input").click()

options = driver.find_elements_by_tag_name("option")

options[12].click()  # 충남
options[22].click()  # 고등
sleep(0.25)
findById("orgname").send_keys(data["school"])
sleep(0.25)
findByClass("searchBtn").click()
sleep(0.25)
driver.find_element_by_tag_name("em").click()
findByClass("layerFullBtn").click()

# 개인 정보 입력
findById("user_name_input").send_keys(data["name"])
findById("birthday_input").send_keys(data["birth"])

# 비밀번호
findByClass("keyboard-img").click()

# 가상키보드 값 정렬
unsorted_keys = driver.find_elements_by_class_name("transkey_div_3_2")
unsorted_keys += driver.find_elements_by_class_name("transkey_div_3_3")
keys = {}
for i in unsorted_keys:
    keys[i.get_attribute("aria-label")] = i  # 키보드 값 : element

for i in data["passwd"]:  # 비밀번호 입력
    keys[i].click()

findById("btnConfirm").click()

# 참여자 클릭
sleep(2)
findByClass("survey-button").click()

# 참여
sleep(1)
findById("survey_q1a1").click()
findById("survey_q2a3").click()
findById("survey_q3a1").click()

findById("btnConfirm").click()

sleep(10)
