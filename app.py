from flask import Flask,render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import os
from Summary import *
from convert import *

STATIC_DIR = os.path.abspath('static')

#Doc
UPLOAD_FOLDER = './uploads'
ALLOWED_EXTENSIONS = {'pdf', 'png', 'jpg', 'jpeg'}
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
app = Flask(__name__, static_folder=STATIC_DIR)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/', methods=['POST', 'GET'])
def get_data():
        if request.method == 'POST':
                flag=request.form.get('lang')
                if not(request.form.get('mode')):
                        text = request.form['search']
                        if flag:
                                text=English(text)
                        text=Simplifier(text)
                else:
                        file_=request.files['img']
                        filename = secure_filename(file_.filename)
                        s=os.path.join(app.config['UPLOAD_FOLDER'], filename)
                        file_.save(s)
                        text=Text_convertor(s,flag)
                        text=Simplifier(text)
                        if flag:
                                text=English(text)
                s2=os.path.join(app.config['UPLOAD_FOLDER'], 'name.txt')
                with open(s2,'w') as f:
                    f.write(text)     
                if request.form.get('type'):
                    return redirect(url_for('legal', name='Processing'))
                else:
                    return redirect(url_for('summary', name='Processing'))


@app.route('/summary/<name>')
def summary(name):
    s2=os.path.join(app.config['UPLOAD_FOLDER'], 'name.txt')
    with open(s2,'r') as f:
        name=f.read()     
    summary = Format(generate_summary(name))

    #return htmlsummary
    return render_template('summary.html',summary=summary,name=name)

@app.route('/legal/<name>')
def legal(name):
    s2=os.path.join(app.config['UPLOAD_FOLDER'], 'name.txt')
    with open(s2,'r') as f:
        name=f.read()
    summary= generate_summary(name)
    legal= generate_legal(summary)
    per=(len(legal)/len(summary))*100
    summary=Format(summary)
    legal=Format(legal)
    return render_template('legal.html',legal=legal, summary=summary, name=name, per=per)

if __name__ == '__main__' :
        app.run(debug=True)
