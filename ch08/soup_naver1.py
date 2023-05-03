# naver에서 필요한 정보 가져오기

import requests
from bs4 import BeautifulSoup

url = "https://www.naver.com/"
response = requests.get(url)
# print(response.text)  # 파싱안함
html = BeautifulSoup(response.text, 'html.parser')
# print(html)             # 파싱함
print(html.title)         # <title> 태그포함 NAVER 출력됨
print(html.title.name)    # 태그 이름
print(html.title.text)    # 태그 문자열 - <title> NAVER 문자만 출력됨

# 네이버를 시작페이지로

div = html.find('div', attrs={'class': 'service_area'})
first_a = div.find('a')
print(first_a)
print(first_a.text)       # 문자열만 알고싶으면 .text

# '주니어 네이버' 찾아 오기
all_a = div.findAll('a')
print(all_a[1])
print(all_a[1].text)

for a in all_a:
    print(a)        # 각각의 <a> 태그
    print(a.text)   # 각각의 텍스트
