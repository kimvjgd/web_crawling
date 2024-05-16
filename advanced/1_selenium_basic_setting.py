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

# 크롬 드라이버 자동 업데이트
from webdriver_manager.chrome import ChromeDriverManager

# browser 꺼짐 방지
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# 불필요한 에러 메세지 없애기
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

# chrome driver manager로 chrome driver를 자동으로 설치해준다.
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)
# 웹페이지 해당 주소로 이동
driver.get("https://www.naver.com")

