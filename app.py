from flask import Flask , render_template,request,send_file
from wp_detector import url_check
from csv_file import parse_csv
from datetime import datetime

app = Flask(__name__)
UPLOAD_FOLDER = 'static/files'
@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/url',methods=["POST"])
def api_api_single_check():
    data = request.get_json()
    return url_check(data['url'])

@app.route("/uploadFiles", methods=['POST'])
def uploadFiles():
      # get the uploaded file
      uploaded_file = request.files['file']
      filename = str(datetime.now().strftime("%Y%m%d-%H%M%S")).replace(" ","-")
      if uploaded_file.filename != '':
           file_path = UPLOAD_FOLDER + filename + ".csv"
          # set the file path
           uploaded_file.save(file_path)
           parse_csv(file_path)
          # save the file
      return send_file(UPLOAD_FOLDER + filename + "-out.csv", as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)