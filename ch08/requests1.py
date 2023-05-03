# requests 모듈 : python의 HTTP 라이브러리임
# url을 가져올 수 있음
import requests

url = 'https://www.python.org/'
response = requests.get(url)
print(response)                 # 200 코드 - 정상 작동 중
print(response.status_code)     # 상태코드
print(response.text)            # html 태그 모두 출력됨

html = response.text
print(html)                     # html 태그 모두 출력됨

url2 = 'https://www.python.org/3'
response2 = requests.get(url2)
print(response2)

# https://www.python.org/robots.txt 자동으로 검색하는 소프트웨어 robots 라고함
# 로봇 배제 표준 - robots.txt
# 무분별하게 접급하는 것을 방지하기 위한것
# 무분별하게 검색 로봇(소프트웨어)이 접근하는 것을 막는 규정
urls = ['https://www.python.org/', 'https://www.daum.net/']
filename = 'robots.txt'

# print(urls[0] + filename)

for url in urls:
    url_path = url + filename
    print(url_path)                     # 출력값 - https://www.daum.net/robots.txt
    response = requests.get(url_path)
    print(response)                     # 출력값 - <Response [200]>


#HTML, XML을 다루는(파싱) 라이브러리
# pip install BeautifulSoup4 - 터미널에서 설치 BeautifulSoup