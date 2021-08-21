from flask import Flask , jsonify , render_template
from wp_detector import url_check
app = Flask(__name__)

@app.route('/')
def hello(name=None):
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)