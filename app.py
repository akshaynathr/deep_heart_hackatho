from flask import Flask,render_template,request
from werkzeug import secure_filename
import os
from src import run
app=Flask(__name__)

app.config['UPLOAD_FOLDER'] = 'uploads/'



@app.route('/home')
def home():
	return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
     file = request.files['file']
     if file :
         filename = secure_filename(file.filename)
         file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
         return render_template('analysis.html')

if __name__=="__main__":
	app.run(debug=True)



