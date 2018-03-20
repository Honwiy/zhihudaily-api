from flask import Flask
from flask import make_response
import requests

app = Flask(__name__)

@app.route('/latest')
def latest():
    headers = {
    'User-Agent': 'Mozilla/5.0'
    }
    r = requests.get("https://news-at.zhihu.com/api/4/news/latest",headers = headers)
    result = make_response(r.text)
    result.headers['Access-Control-Allow-Origin']='*'
    return result

@app.route('/content/<id>',)
def content(id):
    headers = {
    'User-Agent': 'Mozilla/5.0'
    }
    r = requests.get("https://news-at.zhihu.com/api/4/news/{id}".format(id=id),headers = headers)
    
    result = make_response(r.text)
    result.headers['Access-Control-Allow-Origin']='*'
    return result

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)