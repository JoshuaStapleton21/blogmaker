from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')
    
# @app.route('/education.html')
# def education():
#     return render_template('templates/2021/07/06/education.html')

@app.route('/meaning_of_life.html')
def meaning_of_life():
    return render_template('templates/2021/07/06/meaning_of_life.html')

@app.route('/zksnarks.html')
def zksnarks():
    return render_template('templates/2021/07/07/zksnarks.html')

@app.route('/ai_horror.html')
def ai_horror():
    return render_template('templates/2021/07/11/ai_horror.html')

if __name__ == '__main__': # there is always one line between the last app route and these last two lines
    app.run(debug=True)