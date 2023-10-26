from flask import Flask, request, render_template
import json

app = Flask(__name__)

# 정적 파일 제공 (index.html)
@app.route('/')
def index():
    return render_template('index.html')

# POST 요청에 대한 라우트
@app.route('/postdata', methods=['POST'])
def post_data():
    data = request.json
    print('POST 데이터:', data)
    return '데이터를 서버에서 받았습니다.'

# 서버 시작
if __name__ == '__main__':
    app.run(debug=True)