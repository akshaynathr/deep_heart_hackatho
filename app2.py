from flask import Flask,render_template,request
from werkzeug import secure_filename
import os
import subprocess
#from src import run
app=Flask(__name__)

app.config['UPLOAD_FOLDER'] = 'uploads/'


def command():
    cmd = ["./src/run.py","--plot"]
    p = subprocess.Popen(cmd, stdout = subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            stdin=subprocess.PIPE)
    out,err = p.communicate()
    return out



@app.route('/home')
def home():
	return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
     file = request.files['file']
     if file :
         filename = secure_filename(file.filename)
         file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
         subprocess.call("./test.sh",shell=True)
         #run.execute(True,False)
         return render_template("analysis.html")

if __name__=="__main__":
	app.run(debug=True)



