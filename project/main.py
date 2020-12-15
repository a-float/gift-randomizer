from flask import Flask
from flask_login import LoginManager
from flask import Blueprint, render_template, url_for
from flask_login import login_required, current_user
from .models import User
from . import db
import random

main = Blueprint('main', __name__)

@main.route('/')
@login_required
def index():
    users = User.query.all()
    all_signed_in = True
    for u in users:
        if u.password is None:
            all_signed_in = False
            break
    gifts_are_set = users[0].gifts is not None
    can_show_results = all_signed_in and gifts_are_set
    if all_signed_in and not gifts_are_set:
        pick_gifters()
    return render_template("index.html", giftee=current_user.gifts if can_show_results else None)

def are_self_gifts(tab1, tab2):
    for i in range(len(tab1)):
        if tab1[i] == tab2[i]:
            return True
    return False

def pick_gifters():
    users = User.query.all()
    original_names = [u.name for u in users]
    names = original_names[:]
    while(are_self_gifts(names,original_names)):
        random.shuffle(names)
    print(original_names)
    print(names)
    for i in range(len(users)):
        users[i].gifts = names[i]
    db.session.commit()

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)

app = Flask(__name__)
app.config['SECRET_KEY'] = '54AS5A6S53FA1S3AS3D1'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

db.init_app(app)
login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)

from .models import User

@login_manager.user_loader
def load_user(user_id):
    # since the user_id is just the primary key of our user table, use it in the query for the user
    return User.query.get(int(user_id))

# blueprint for auth routes in our app
from .auth import auth as auth_blueprint
app.register_blueprint(auth_blueprint)

# blueprint for non-auth parts of app
from .main import main as main_blueprint
app.register_blueprint(main_blueprint)
app.debug = False