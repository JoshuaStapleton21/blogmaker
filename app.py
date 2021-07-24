from flask import Flask, render_template
from flask import request
from gpt3_request import get_open_api_response
from gpt3_publish import publish_gtp3_output

app = Flask(__name__)

ARTICLE_BODY_PROMPT = ""
ARTICLE_TITLE = ""

### In order to get this working, PATH environment variable needs to be set to pandoc
### To do this, you need to add PATH in the kudu shell for this container
### In order to do that, you need to add an applicationHost.xdt file to home/site using the bash script.
### In order to do this, you need to use echo commands to manually write to the file
### In order to do that, you need to figure out how to escape quotation marks

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
    get_open_api_response(str(ARTICLE_BODY_PROMPT), str(ARTICLE_TITLE)) # get the response, and write it to md
    publish_gtp3_output() # publish the response from md as a new article
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