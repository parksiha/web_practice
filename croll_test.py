from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

# 1. 크롬 브라우저 열기
options = webdriver.ChromeOptions()
# options.add_argument("--headless")  # 브라우저 안띄우고 실행 (원하면 주석 처리하세요)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# 2. 웹사이트 접속
url = "https://quotes.toscrape.com/"
driver.get(url)

# 페이지 로딩 대기
time.sleep(2)

# 3. 원하는 요소 찾기 (명언과 저자)
quotes = driver.find_elements(By.CLASS_NAME, "text")
authors = driver.find_elements(By.CLASS_NAME, "author")

# 4. 데이터 출력
for quote, author in zip(quotes, authors):
    print(f"{author.text} : {quote.text}")

# 5. 브라우저 종료
driver.quit()