from flask import Flask, render_template
from flask import request, redirect
from gpt3_request import get_open_api_response
import time
import logging
# Acquire the logger for a library (azure.mgmt.resource in this example)
logger = logging.getLogger('azure.mgmt.resource')

# Set the desired logging level
logger.setLevel(logging.DEBUG)

from gpt3_publish import publish_gtp3_output

app = Flask(__name__)

ARTICLE_BODY_PROMPT = ""
ARTICLE_TITLE = ""

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
    logging.info("pow")
    logging.info("yeet")
    return render_template('templates/2021/07/07/zksnarks.html')

@app.route('/ai_horror.html')
def ai_horror():
    return render_template('templates/2021/07/11/ai_horror.html')

@app.route('/gpt3_demo.html')
def gpt3_demo():
    return render_template('templates/2021/07/17/gpt3_demo.html')

# @app.route('/signup', methods = ['POST'])
# def signup():
#     article_body_prompt = request.form['article_body_prompt']
#     article_title = request.form['article_title']
#     # print(article_title)
#     # print("Processing user input of ", article_body_prompt)
#     # get_open_api_response(str(article_body_prompt), str(article_title)) # get the response, and write it to md
#     # publish_gtp3_output() # publish the response from md as a new article
#     # redirect('templates/loader.html')
#     # time.sleep(10)
#     # return render_template('templates/2021/07/11/loader.html')
#     return render_template('templates/2021/07/11/temp_gpt3.html')

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

if __name__ == '__main__': # there is always one line between the last app route and these last two lines
    app.run(debug=True)