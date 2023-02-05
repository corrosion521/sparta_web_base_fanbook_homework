from flask import Flask, render_template, request, jsonify
app = Flask(__name__)


# 이하 3줄 db사용 위해
from pymongo import MongoClient

client = MongoClient('mongodb+srv://test:sparta@cluster0.n0vryb2.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta


@app.route('/')
def home():
   return render_template('index.html')

@app.route("/homework", methods=["POST"])
def homework_post():
    name_receive = request.form['name_give']
    comment_receive = request.form['comment_give']

    # db에 넣기
    doc = {
        'name': name_receive,
        'comment': comment_receive,
    }
    db.homework.insert_one(doc)

    return jsonify({'msg':'응원 댓글 작성 완료!'})

@app.route("/homework", methods=["GET"])
def homework_get():
    # 여러개 찾기 - 예시 ( _id 값은 제외하고 출력)
    homework_list = list(db.homework.find({}, {'_id': False}))

    # response의 구성물 중 하나가 'homework'
    # dictionary느낌 기억
    return jsonify({'homework': homework_list})

if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)