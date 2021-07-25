from flask import Flask, render_template
from flask import request
from non_pandoc import rewrite_temp_gpt3_without_pandoc

app = Flask(__name__)

ARTICLE_BODY_PROMPT = ""
ARTICLE_TITLE = ""

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/hello", methods = ['POST'])
def hello():
    global ARTICLE_BODY_PROMPT
    ARTICLE_BODY_PROMPT = request.form['article_body_prompt']
    global ARTICLE_TITLE
    ARTICLE_TITLE = request.form['article_title']
    return render_template('templates/2021/07/11/loader.html')

@app.route("/done")
def done():
    return render_template('templates/2021/07/11/temp_gpt3.html')

@app.route("/slow")
def slow():
    print("User title: ", ARTICLE_TITLE)
    print("Processing user input of ", ARTICLE_BODY_PROMPT)
    rewrite_temp_gpt3_without_pandoc(str(ARTICLE_BODY_PROMPT), str(ARTICLE_TITLE))
    return "Yah Yeet"

@app.route('/meaning_of_life.html')
def meaning_of_life():
    return render_template('templates/2021/07/06/meaning_of_life.html')

@app.route('/zksnarks.html')
def zksnarks():
    return render_template('templates/2021/07/07/zksnarks.html')

@app.route('/ai_horror.html')
def ai_horror():
    return render_template('templates/2021/07/11/ai_horror.html')

@app.route('/gpt3_demo.html')
def gpt3_demo():
    return render_template('templates/2021/07/17/gpt3_demo.html')

@app.route('/feral_mozart.html')
def feral_mozart():
    return render_template('templates/2021/07/24/feral_mozart.html')

if __name__ == '__main__': # there is always one line between the last app route and these last two lines
    app.run(debug=True)