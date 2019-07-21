from flask import Flask, render_template, jsonify, request
from grandpy.mainfile import process_question
from grandpy.classes import *

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False # to keep tones when returning json file

@app.route('/')
@app.route('/home/')
def home():
    return render_template('home.html')

@app.route('/api', methods= ['POST'])
def ajax():
    if request.method == 'POST':
        text = request.form['usertext']
        response = process_question(text)
        # return render_template('momo.html',text=response)
        return jsonify(response)

    
if __name__ == "__main__":
    app.run(debug=True, port=5000)