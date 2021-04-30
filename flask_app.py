"""
★ app7の学習目標：AWS連動
참조 URL : AWS 파이썬 서버 구축(https://www.fun-coding.org/flask_advanced-5.html), (https://ndb796.tistory.com/244)
"""

import os
# pip install flask -> python -> import flask
from flask import Flask, render_template, request, redirect, session, url_for
import pymysql  # pip install pymysql
import time
from werkzeug.utils import secure_filename

app = Flask(__name__)

app.secret_key = b'zix7211'

allowed_extensions = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
app.config['upload_folder'] = 'uploads'

conn = pymysql.connect(
    user='ydhvocal',
    passwd='',
    # host='127.0.0.1',
    db='ydhvocal$mysql',
    charset='utf8'
)


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
