# flask 웹 프레임워크 사용하기
import flask                    # ver1
from flask import Flask         # ver2

# fla = flask.Flask(__name__)   # ver1
app = Flask(__name__)           # ver2

@app.route('/')    # 127.0.0.1:5000/
def index():
    return "<h1>Hello~ flask!</h1>"

@app.route('/sajangnim')        # / 슬래시 뒤에 붙는 명칭은 http://127.0.0.1:5000/sajangnim 주소 경로라고 생각하면 됨.
def login():
    return "<h1><i>로그인</i> 페이지입니다.</h1>"

@app.route('/board/view')
def detail():
    return "<h1>게시판 상세 페이지</h1>"

app.run() # 서버 실행

'''
웹 MVC
flask1.py - 컨트롤러
'''