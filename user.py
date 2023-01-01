from selenium.webdriver.remote.webelement import WebElement
from selenium import webdriver
from time import sleep

def Log(title, content):
    print(f"[{title}] >> {content}")

url = "https://hcs.eduro.go.kr/#/none"

data = {
    "school": "서령고",
    "name": "이재헌",
    "birth": "060208",
    "passwd": "1790"
}


class User:
    def __init__(self, school, name, birth, passwd):
        self.data = {
            "school": school,
            "name": name,
            "birth": birth,
            "passwd": passwd
        }

    def findById(self, id) -> WebElement:
        return self.driver.find_element_by_id(id)

    def findByClass(self, className) -> WebElement:
        return self.driver.find_element_by_class_name(className)

    def findSchool(self):
        # 학교 찾기
        self.findById("schul_name_input").click()

        options = self.driver.find_elements_by_tag_name("option")

        options[12].click()  # 충남
        options[22].click()  # 고등
        sleep(0.25)
        self.findById("orgname").send_keys(self.data["school"])
        sleep(0.25)
        self.findByClass("searchBtn").click()
        sleep(0.25)
        self.driver.find_element_by_tag_name("em").click()
        self.findByClass("layerFullBtn").click()

    def inputPersonInfo(self):
        # 개인 정보 입력
        self.findById("user_name_input").send_keys(self.data["name"])
        self.findById("birthday_input").send_keys(self.data["birth"])

        # 비밀번호
        self.findByClass("keyboard-img").click()

        # 가상키보드 값 정렬
        unsorted_keys = self.driver.find_elements_by_class_name("transkey_div_3_2")
        unsorted_keys += self.driver.find_elements_by_class_name("transkey_div_3_3")
        keys = {}
        for i in unsorted_keys:
            keys[i.get_attribute("aria-label")] = i  # 키보드 값 : element

        for i in self.data["passwd"]:  # 비밀번호 입력
            keys[i].click()

        self.findById("btnConfirm").click()

    def participate(self):
        #참여자 클릭
        sleep(2)
        self.findByClass("survey-button").click()

        # 참여
        sleep(1)
        self.findById("survey_q1a1").click()
        self.findById("survey_q2a3").click()
        self.findById("survey_q3a1").click()

        self.findById("btnConfirm").click()

    def start(self):
        Log("Start", f"{self.data['name']}님의 자가진단을 시작합니다.")
        self.driver = webdriver.Chrome('C:/chromedriver.exe')
        self.driver.get(url)

        self.findById("btnConfirm2").click()

        self.findSchool()
        self.inputPersonInfo()
        self.participate()
        self.driver.quit()

        Log("Start", f"{self.data['name']}님의 자가진단을 완료하였습니다.")
        sleep(1)