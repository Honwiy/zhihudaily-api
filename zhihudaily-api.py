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

@app.route('/content/<id>')
def content(id):
    headers = {
    'User-Agent': 'Mozilla/5.0'
    }
    r = requests.get("https://news-at.zhihu.com/api/4/news/{id}".format(id=id),headers = headers)
    
    result = make_response(r.text)
    result.headers['Access-Control-Allow-Origin']='*'
    return result

@app.route('/before/<date>')
def before(date):
    headers = {
    'User-Agent': 'Mozilla/5.0'
    }
    r = requests.get("https://news-at.zhihu.com/api/4/news/before/{date}".format(date=date),headers = headers)
    
    result = make_response(r.text)
    result.headers['Access-Control-Allow-Origin']='*'
    return result

@app.route('/story-extra/<id>')
def storyExtra(id):
    headers = {
    'User-Agent': 'Mozilla/5.0'
    }
    r = requests.get("https://news-at.zhihu.com/api/4/story-extra/{id}".format(id=id),headers = headers)
    result = make_response(r.text)
    result.headers['Access-Control-Allow-Origin']='*'
    return result

@app.route('/long-comments/<id>')
def longComments(id):
    headers = {
    'User-Agent': 'Mozilla/5.0'
    }
    r = requests.get("https://news-at.zhihu.com/api/4/story/{id}/long-comments".format(id=id),headers = headers)
    result = make_response(r.text)
    result.headers['Access-Control-Allow-Origin']='*'
    return result

@app.route('/short-comments/<id>')
def shortComments(id):
    headers = {
    'User-Agent': 'Mozilla/5.0'
    }
    r = requests.get("https://news-at.zhihu.com/api/4/story/{id}/short-comments".format(id=id),headers = headers)
    result = make_response(r.text)
    result.headers['Access-Control-Allow-Origin']='*'
    return result



if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)