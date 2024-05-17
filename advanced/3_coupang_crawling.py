import requests
from bs4 import BeautifulSoup

main_url = "https://www.coupang.com/np/search?component=&q=%EA%B2%8C%EC%9D%B4%EB%B0%8D+%EB%A7%88%EC%9A%B0%EC%8A%A4&channel=user"

# 헤더에 User.Agent를 추가하자      <- 쿠팡은 이래야 함..
headers = {
    'User-Agent' : 'Mozilla/5.0',
    "Accept-Language": "ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3" 
}

repsonse = requests.get(main_url, headers=headers)
html = repsonse.text
soup = BeautifulSoup(html, "html.parser")

links = soup.select("a.search-product-link")
# print('links : ' , links)
for link in links:
    sub_url = 'https://www.coupang.com/' + link.attrs['href']

    response = requests.get(sub_url, headers=headers)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')

    # 중고 상품일 경우 태그가 달라진다.
    # try except로 예외처리해줘야한다.

    try:
        # 브랜드명
        brand_name = soup.select_one("a.prod-brand-name").text.strip()
    except:
        brand_name = ""
    
    # 상품명
    product_name = soup.select_one("h2.prod-buy-header__title").text.strip()

    # 가격
    product_price = soup.select_one("span.total-price > strong").text.strip()
    
    print(brand_name, product_name, product_price)
    