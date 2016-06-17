"""
Routes and views for the flask application.
"""

"""
imports from system
"""
from datetime import datetime
import logging as lg 

"""
project imports
"""
from FlaskWebProject1 import app
from FlaskWebProject1 import dbHelper


"""
imports for flask
"""
from flask import render_template
from flask import Flask, request, redirect, url_for, send_from_directory


"""
imports for werkzeug
"""
from werkzeug.utils import secure_filename


"""
configure logging
"""
logging.basicConfig(filename='example.log', filemode='w',format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.DEBUG)
logging.warning('!!! First Log !!!')




@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )

@app.route('/getUser/<username>')
def getUserProfile(username):
    logging.debug("search for userProfile")
    user = mongo.db.users.find_one_or_404({'_id': username})
    return render_template('index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/getUser')
def getUserProfile():
    logging.debug("function getUserProfile: search for userProfile")
    username = request.args.get('username')
    user = mongo.db.users.find_one_or_404({'_id': username})
    return render_template('index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/newPlace')
def addNewPlaceToUser():
    logging.debug("function addNewPlaceToUser: search for userProfile")
    username = request.args.get('username')
    user = mongo.db.users.find_one_or_404({'_id': username})
    return render_template('index.html',
        title='Home Page',
        year=datetime.now().year,
    )

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)
