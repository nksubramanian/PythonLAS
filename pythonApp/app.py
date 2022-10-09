import os

from flask import Flask, render_template, request
import random
import lasio as lasio
from werkzeug.utils import secure_filename

Upload = 'static/upload'
app = Flask(__name__)
app.config['uploadFolder'] = Upload
# list of cat images
images = [
    "http://ak-hdl.buzzfed.com/static/2013-10/enhanced/webdr05/15/9/anigif_enhanced-buzz-26388-1381844103-11.gif",
    "http://ak-hdl.buzzfed.com/static/2013-10/enhanced/webdr01/15/9/anigif_enhanced-buzz-31540-1381844535-8.gif",
    "http://ak-hdl.buzzfed.com/static/2013-10/enhanced/webdr05/15/9/anigif_enhanced-buzz-26390-1381844163-18.gif",
    "http://ak-hdl.buzzfed.com/static/2013-10/enhanced/webdr06/15/10/anigif_enhanced-buzz-1376-1381846217-0.gif",
    "http://ak-hdl.buzzfed.com/static/2013-10/enhanced/webdr03/15/9/anigif_enhanced-buzz-3391-1381844336-26.gif",
    "http://ak-hdl.buzzfed.com/static/2013-10/enhanced/webdr06/15/10/anigif_enhanced-buzz-29111-1381845968-0.gif",
    "http://ak-hdl.buzzfed.com/static/2013-10/enhanced/webdr03/15/9/anigif_enhanced-buzz-3409-1381844582-13.gif",
    "http://ak-hdl.buzzfed.com/static/2013-10/enhanced/webdr02/15/9/anigif_enhanced-buzz-19667-1381844937-10.gif",
    "http://ak-hdl.buzzfed.com/static/2013-10/enhanced/webdr05/15/9/anigif_enhanced-buzz-26358-1381845043-13.gif",
    "http://ak-hdl.buzzfed.com/static/2013-10/enhanced/webdr06/15/9/anigif_enhanced-buzz-18774-1381844645-6.gif",
    "http://ak-hdl.buzzfed.com/static/2013-10/enhanced/webdr06/15/9/anigif_enhanced-buzz-25158-1381844793-0.gif",
    "http://ak-hdl.buzzfed.com/static/2013-10/enhanced/webdr03/15/10/anigif_enhanced-buzz-11980-1381846269-1.gif"
]

@app.route('/')
def index():
    url = random.choice(images)
    return render_template('index.html', url=url)

@app.route("/getfile", methods=["POST"])
def getfile():
    file = request.files['file']
    return file.read()

@app.route("/getwells", methods=["GET"])
def getwells():
    file = request.files['file']
    file.save(secure_filename(file.filename))
    filename = file.filename
    file_name = request.form[filename]
    with open(file_name, 'r') as f:
        file_content = f.read()
    return file_content


@app.route("/upload", methods = ['POST'])
def upload():
    file = request.files['file']
    filename = file.filename
    print(filename)
    file.save(file.filename)
    print(os.path)
    return filename



@app.route("/getfilename", methods=["POST"])
def getfilename():
    file = request.files['file']
    return str(file.filename)



if __name__ == "__main__":
    app.run(host="0.0.0.0")
