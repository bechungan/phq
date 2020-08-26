from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)

app = Flask(__name__)

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbmyproject  # 'dbmyproject'라는 이름의 db를 만듭니다.


## HTML을 주는 부분
@app.route('/')
def home():
    return render_template('index.html')


@app.route('/normal')
def result_normal():
    return render_template('normal.html')


@app.route('/mild')
def result_mild():
    return render_template('mild.html')


@app.route('/moderate')
def result_moderate():
    return render_template('moderate.html')


@app.route('/severe')
def result_severe():
    return render_template('severe.html')


## API 역할을 하는 부분
@app.route('/surveyresult', methods=['POST'])
def write_survey_result():
    # 1. 클라이언트가 준 전화번호, phq1-10 가져오기
    phone_receive = request.form['phone_give']
    phq1_receive = request.form['phq1_give']
    phq2_receive = request.form['phq2_give']
    phq3_receive = request.form['phq3_give']
    phq4_receive = request.form['phq4_give']
    phq5_receive = request.form['phq5_give']
    phq6_receive = request.form['phq6_give']
    phq7_receive = request.form['phq7_give']
    phq8_receive = request.form['phq8_give']
    phq9_receive = request.form['phq9_give']
    phq10_receive = request.form['phq10_give']

    # 2. DB에 정보 삽입할 result 만들어서 mongodb 에 저장하기
    phq_survey = {
        'phone': phone_receive,
        'phq1': phq1_receive,
        'phq2': phq2_receive,
        'phq3': phq3_receive,
        'phq4': phq4_receive,
        'phq5': phq5_receive,
        'phq6': phq6_receive,
        'phq7': phq7_receive,
        'phq8': phq8_receive,
        'phq9': phq9_receive,
        'phq10': phq10_receive
    }

    db.phq.insert_one(phq_survey)
    # 3. 성공 여부 & 성공 메시지 반환하기
    return jsonify({'result': 'success', 'msg': '잘 등록되었습니다!'})


if __name__ == '__main__':
    app.run('127.0.0.1', port=5000, debug=True)
