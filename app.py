from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')
    
@app.route('/education.html')
def education():
    return render_template('templates/2021/07/06/education.html')

@app.route('/meaning_of_life.html')
def meaning_of_life():
    return render_template('templates/2021/07/06/meaning_of_life.html')

@app.route('/zksnarks.html')
def zksnarks():
    return render_template('templates/2021/07/07/zksnarks.html')

if __name__ == '__main__':
    app.run(debug=True)