from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
import certifi

ca = certifi.where()
# mongodb 설정 부분
client = MongoClient('mongodb+srv://test:sparta@cluster0.5y4p9ef.mongodb.net/?retryWrites=true&w=majority',tlsCAFile=ca)
db = client.dbsparta

# flask 초기화
app = Flask(__name__)

@app.route('/')
def home():
   return render_template('index.html')


# 편지 남기기 서버 부분
@app.route('/letter')
def letter():
   return render_template('letter.html')


@app.route("/happy", methods=["POST"])
def web_happy_post():
    name_receive = request.form['name_give']
    comment_receive = request.form['comment_give']

    all_friends = list(db.happy.find({},{'_id':False}))
    count = len(all_friends) + 1

    doc = {
        'num': count,
        'name': name_receive,
        'comment': comment_receive,
    }
    db.happy.insert_one(doc)

    return jsonify({'msg': '남기기 완료!'})


@app.route("/happy", methods=["GET"])
def web_happy_get():
    friend_list = list(db.happy.find({}, {'_id': False}))
    return jsonify({'friend': friend_list})


@app.route("/message/done", methods=["POST"])
def message_done():
    message_receive = request.form['message_give']
    result = db.happy.delete_one({'num': int(message_receive)})
    return jsonify({'msg': 'message 삭제!'})


# 소개 서버 부분
@app.route('/about')
def about():
   return render_template('about.html')


if __name__ == '__main__':  
   app.run('0.0.0.0',port=5000,debug=True)






   '''
from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.iofm7.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta

app = Flask(__name__)

@app.route('/')
def home():
   return render_template('index.html')



if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)
   '''

