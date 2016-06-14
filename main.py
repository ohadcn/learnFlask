'''
Created on Jun 14, 2016

@author: ohad
'''
from flask import Flask, render_template
from flask.globals import request
app = Flask(__name__)

datas = ['']*10
datIndex = 0

@app.route('/', methods=['GET', 'POST'])
def index():
    global datas, datIndex
    if request.method == 'POST':
        if not request.form.get('text'):
            return 'Please enter something!'
        datas[datIndex] = request.form['text']
        datIndex += 1
    return render_template('index.html', content = '<br/>'.join(datas))


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=1)