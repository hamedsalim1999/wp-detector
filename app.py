from flask import Flask , jsonify , render_template,request
from wp_detector import url_check

app = Flask(__name__)

@app.route('/')
def hello(name=None):
    return render_template('index.html')

@app.route('/url',methods=["POST"])
def api_api_single_check():
    data = request.get_json()
    return url_check(data['url'])

if __name__ == '__main__':
    app.run(debug=True)