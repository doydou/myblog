from flask import Flask
from gevent import pywsgi

#创建一个flask的应用程序
app = Flask(__name__)

#定义两个路由 '/' 和 '/blog',并分别渲染两个不同的模板
@app.route("/")
def index():
    return render_template('index.html')

@app.route('/blog')
def blog():
    return render_template('bolg.html')

if __name__ == "__main__":
    server = pywsgi.WSGIServer(('127.0.0.1',5000), app)
    server.serve_forever()
