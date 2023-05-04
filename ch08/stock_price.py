# 주식 종목 가져오기 - 네이버 금융 > 증권 > 증권홈 > 인기 종목 검색(우측 하단)
import  requests
from bs4 import BeautifulSoup

def getcontent(item_code):
    url = 'https://finance.naver.com/item/main.naver?code=' + item_code
    response = requests.get(url)
    content = BeautifulSoup(response.text, 'html.parser')
    return content

# content = getcontent('086520')  # 호출    # 에코프로 주가 코드번호 삽입
content = getcontent('005930')  # 삼성전자
today = content.find('div', attrs={'class':'today'})
# print(today)

price = today.find('span', attrs={'class': 'blind'})
print(price.text)
print(f'에코프로 주가 : {price.text}원')




