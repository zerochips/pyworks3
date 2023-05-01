# 컨트롤러 - 모든걸 제어 - start_app.py
# templates 폴더, static 폴더
# 웹 서버 - flask 사용

from flask import Flask, render_template

app = Flask(__name__)

# url - '/' 경로 설정
@app.route('/')
def index():
    return render_template('index.html')

app.run()