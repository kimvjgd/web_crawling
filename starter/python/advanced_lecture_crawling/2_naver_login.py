# Selenium - 최신 업데이트된 방식 사용
# 크롬 드라이버 자동 업데이트 코드
# 브라우저 꺼짐 방지 코드
# 불필요한 에러 메세지 제거

# Selenium4
# 이미 깔았다면?
# pip install --upgrade pip
# pip install --upgrade selenium

# 처음한다면
# pip install selenium
# pip install webdriver_manager     -- web driver를 update해주는 녀석

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# 크롬 드라이버 자동 업데이트
from webdriver_manager.chrome import ChromeDriverManager

import time
import pyautogui
import pyperclip

# browser 꺼짐 방지
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# 불필요한 에러 메세지 없애기
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

# chrome driver manager로 chrome driver를 자동으로 설치해준다.
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)



# 웹페이지 해당 주소로 이동
driver.implicitly_wait(5)   # 웹페이지가 로딩될 때까지 5초는 기다린다.
driver.maximize_window()    # 화면을 최대화
driver.get("https://nid.naver.com/nidlogin.login?mode=form&url=https://www.naver.com/")

# <input type="text" id="id" name="id" placeholder="아이디" title="아이디" class="input_text" maxlength="41" value="">

# 아이디 입력창
id = driver.find_element(By.CSS_SELECTOR, '#id')
id.click()
# id.send_keys('temp_id')   # 너무 빨라서 bot으로 인식한다.
pyperclip.copy('temp_id')
pyautogui.hotkey("ctrl", "v")
time.sleep(1)

# 비번 입력창
pw = driver.find_element(By.CSS_SELECTOR, '#pw')
pw.click()
# pw.send_keys("xxx_temp_pw_xxx")
pyperclip.copy('xxx_temp_pw_xxx')
pyautogui.hotkey("ctrl", "v")
time.sleep(1)

# 로그인 버튼
login_btn = driver.find_element(By.CSS_SELECTOR, '#log\.login')
login_btn.click()

