# 우리가 연습하는건 BeautifulSoup4 라이브러리
# BeautifulSoup4 라이브러리 - html 태그 파싱(Parsing)
# 끌어오는걸 크롤
# BeautifulSoup(html_str<-html내용, 'html.parser')
# ul = soup.find('ul'<-태그, attrs={'class' : 'item'}<-{'키' : '값'})
from bs4 import BeautifulSoup

html_str = """
<html>
<head>
    <title>웹 스크래핑(크롤링)</title>
</head>
<body>
    <ul class='item'>
        <li>인공지능</li>        
        <li>빅데이터</li>        
        <li>로봇</li>        
    </ul>
    <ul class='comlang'>
        <li>Python</li>        
        <li>C/C#</li>        
        <li>Java</li>        
    </ul>
</body>
</html>
"""

soup = BeautifulSoup(html_str, 'html.parser')       # html.parser 파씽
first_ul = soup.find('ul', attrs={'class': 'item'})
# print(ul)             # 전체 태그 중 ul 태그만 가져옴
# print(first_ul)
# print(first_ul.text)        # 태그없이 텍스트 출력
first_li = soup.find('li')  # 첫번째 li만 찾음
# print(first_li.text)

all_li = first_ul.findAll('li')
print(all_li)           # 출력값 - [<li>인공지능</li>, <li>빅데이터</li>, <li>로봇</li>]
print(all_li[1])        # 출력값 - <li>빅데이터</li>
print(all_li[1].text)   # 출력값 - 빅데이터

for li in all_li:
    # print(li)
    print(li.text)      # 출력값 - 로봇

