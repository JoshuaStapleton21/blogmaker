from flask import Flask, render_template, request
from non_pandoc import rewrite_temp_gpt3_without_pandoc
from auth import auth as auth_blueprint
from flask_login import LoginManager, login_required, current_user 
from flask_sqlalchemy import SQLAlchemy
from models import User

db = SQLAlchemy()
app = Flask(__name__)

app.register_blueprint(auth_blueprint)

app.config['SECRET_KEY'] = '9OLWxND4o83j4K4iuopO'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

db.init_app(app)

login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    # since the user_id is just the primary key of our user table, use it in the query for the user
    return User.query.get(int(user_id))

ARTICLE_BODY_PROMPT = ""
ARTICLE_TITLE = ""

@app.route('/')
def home():
    # return render_template('index.html')
    return render_template('breve_home.html')

@app.route('/about_us')
def about_us():
    return render_template('about_us.html')

@app.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)

@app.route("/hello", methods = ['POST'])
def hello():
    global ARTICLE_BODY_PROMPT
    ARTICLE_BODY_PROMPT = request.form['article_body_prompt']
    global ARTICLE_TITLE
    ARTICLE_TITLE = request.form['article_title']
    return render_template('templates/loader.html')

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