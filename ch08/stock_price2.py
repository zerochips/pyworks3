# 주식 종목 가져오기 - 네이버 금융 > 증권 > 증권홈 > 인기 종목 검색(우측 하단)
import  requests
from bs4 import BeautifulSoup

def getcontent(item_code):
    url = 'https://finance.naver.com/item/main.naver?code=' + item_code
    response = requests.get(url)
    content = BeautifulSoup(response.text, 'html.parser')
    return content

def getprice(item_code):
    content = getcontent(item_code)
    today = content.find('div', attrs={'class': 'today'})
    # print(today)
    price = today.find('span', attrs={'class': 'blind'})
    # print(price.text)
    return price.text

에코프로 = getprice('086520')
삼성전자 = getprice('005930')
SK = getprice('034730')
네이버 = getprice('035420')
KTNG = getprice('033780')


print(f'에코프로: {에코프로}원')
print(f'삼성전자: {삼성전자}원')
print(f'SK: {SK}원')
print(f'네이버: {네이버}원')
print(f'KT&G: {KTNG}원')







