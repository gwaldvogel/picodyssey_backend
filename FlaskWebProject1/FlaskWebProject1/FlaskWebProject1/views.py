"""
Routes and views for the flask application.
"""

"""
imports from system
"""
from datetime import datetime
import logging 

"""
project imports
"""
from FlaskWebProject1 import app
from FlaskWebProject1 import dbHelper


"""
imports for flask
"""
from flask import render_template, json
from flask import Flask, request, redirect, url_for, send_from_directory


"""
imports for werkzeug
"""
from werkzeug.utils import secure_filename


"""
configure logging
"""
logging.basicConfig(filename='example.log', filemode='w',format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',level=logging.DEBUG)
logging.warning('!!! First Log !!!')



"""
default sites for mongodb
"""
@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

"""
default sites for mongodb
"""
@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

"""
default sites for mongodb
"""
@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )

"""
get existing user from mongodb query for uuid
"""
@app.route('/getUser/<username>')
def getUserProfile(username):
    logging.debug("get /getUser/<username>")
    user = mongo.db.users.find_one_or_404({'uuid': username})
    return Flask.jsonify(**user)
    

"""
add new user to mongodb get uuid
"""
@app.route('/newUser', methods=['GET', 'POST'])
def addUserProfile(username):
    content = request.get_json(silent=True)
    logging.debug("get /newUser/<username>")
    
    

"""
get place by uuid 
"""
@app.route('/getPlace/<placename>')
def getPlaceByUuid(placename):
    logging.debug("get /getPlace/<placename> ")
    place = mongo.db.users.find_one_or_404({'uuid': placename})
    return Flask.jsonify(**place)
    
    
"""
get random place from mongodb ignore user places  
"""
@app.route('/getRandPlace')
def getRandPlace():
    logging.debug("get /getRandPlace ")
    user = mongo.db.users.find_one_or_404({'_id': username})
    return render_template('index.html',
        title='Home Page',
        year=datetime.now().year,
    )

"""
get random place from mongodb ignore user places  
"""
@app.route('/get3RandPlaces')
def get3RandPlace():
    logging.debug("get /getRandPlace ")
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
