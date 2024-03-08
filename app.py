from flask import Flask, request, redirect,jsonify,render_template
from datetime import datetime
from flask_cors import CORS
import json
import random
alerts = []
currentalerts = ''

app = Flask(__name__)
CORS(app)
def current_date_yyyymmdd():
    # 현재 날짜를 가져옴
    current_date = datetime.now()
    # 'yyyymmdd' 형태로 포맷팅하여 문자열로 변환
    formatted_date = current_date.strftime('%Y%m%d')
    return str(formatted_date)




@app.route('/')
def main():
    print(currentalerts)
    return render_template('index.html',alert= alerts, currentalert = currentalerts)


app.run()
