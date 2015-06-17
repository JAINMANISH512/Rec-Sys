"""
Rec-Sys is a login based database system implementing the recommendation system
for searching of Documents
"""

# all the imports

from flask import Flask
from flask import render_template , request , redirect, url_for, flash, session, escape
from flask.ext.bcrypt import Bcrypt
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager, login_required, login_user, logout_user, current_user

from models import User, db
from forms import LoginForm, SearchForm

from functions import * 

import sqlite3

from app import app


# from flask import session, g, abort 
# from contextlib import closing

# def init_db():
#     with closing(connect_db()) as db:
#         with app.open_resource('schema.sql', mode='r') as f:
#             db.cursor().executescript(f.read())
#         db.commit()


# # configuration
# DATABASE = '/tmp/flaskr.db'
# DEBUG = True
# #SECRET_KEY = 'development key'
# USERNAME = 'admin'
#PASSWORD = 'default'



#logger = logging.getLogger(__name__)
#login_manager.login_view = "users.login"
login_manager = LoginManager()
bcrypt = Bcrypt()

@login_manager.user_loader
def user_loader(user_id):
    """Given *user_id*, return the associated User object.

    :param unicode user_id: user_id (username) user to retrieve
    """
    return User.query.get(user_id)


app = Flask(__name__)
app.secret_key = 'iocl database'


@app.route("/login", methods=["GET", "POST"])
def login():
    """For GET requests, display the login form. For POSTS, login the current user
    by processing the form."""
    print db
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.get(form.username.data)
        if user:
            if bcrypt.check_password_hash(user.password, form.password.data):
                user.authenticated = True
                db.session.add(user)
                db.session.commit()
                login_user(user, remember=True)
                
                next = flask.request.args.get('next')
                if not next_is_valid(next):
                    return flask.abort(400)

                return redirect(url_for("database"))
    return render_template("login.html", form=form)

@app.route("/logout", methods=["GET"])
@login_required
def logout():
    """Logout the current user."""
    user = current_user
    user.authenticated = False
    db.session.add(user)
    db.session.commit()
    logout_user()
    form = LoginForm()
    return render_template("login.html", form=form)

@app.route('/about')
def about():
    """the about page"""
    return render_template('about.html')

@app.route('/')
def index():
    """redirect page"""
    return redirect(url_for('login'))

# @app.route('/login', methods=['GET', 'POST'])
# def login():
# 	if 'username' in session:
# 		return redirect(url_for('database'))
	
# 	form = LoginForm()
# 	if request.method == 'POST':
#         	if form.validate() == False:
# 			flash("")
#     			return render_template('login.html', form=form)
#         	else:
#     			username,password =  form.username.data,form.password.data
#     			if valid_login(username,password):
#     				session['username'] = username
#     				return redirect(url_for('database'))
#     			else:
#     				return render_template('login.html', form=form)
# 	elif request.method == 'GET':
#	    	return render_template('login.html', form=form)

@app.route('/database', methods=['GET', 'POST'])
@login_required
def database():
	# if 'username' in session:
	# 	searchform = SearchForm()
	# 	if request.method == 'POST':
 	#        	if searchform.validate() == False:
	# 			flash("")
 	#    			return render_template('database.html', form=searchform)
 	#        	else:
	#    			searchterm =  searchform.searchterm.data
 	#    			return searchterm
	# 	elif request.method == 'GET':
	#     		return render_template('database.html', form=searchform)
	# else:
	# 	return redirect(url_for('login'))

	print db
    	form = SearchForm()
    	if form.validate_on_submit():
        	searchterm =  searchform.searchterm.data
        	return searchterm
    	return render_template("database.html", form=form)

# @app.route('/logout') #, methods=['GET', 'POST'])
# def logout():
# 	session.pop('username', None)
# 	return redirect(url_for('login'))

@app.errorhandler(404)
def page_not_found(error):
    return redirect(url_for('index'))

if __name__ == '__main__':
	app.run()

