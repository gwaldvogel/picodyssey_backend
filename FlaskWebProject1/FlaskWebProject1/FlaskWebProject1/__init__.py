"""
The flask application package.
"""

from flask import Flask
from flask_pymongo import PyMongo


import platform
if platform.system == "Windows":
    PROCESSING_FOLDER = 'C://data//imagesBig'
    UPLOAD_FOLDER = 'C://data//images'
elif platform.system == "Linux":
    PROCESSING_FOLDER = 'C://data//imagesBig'
    UPLOAD_FOLDER = '/home/ubuntu/data/images'
else:
    PROCESSING_FOLDER = 'C://data//imagesBig'
    UPLOAD_FOLDER = 'C://data//images'

"""
allowed upload formates
"""    
ALLOWED_EXTENSIONS = set(['jpg', 'jpeg'])

"""
ssl keys for the server
"""
SERVER_KEY = ""
SERVER_CRT = ""

app = Flask(__name__)

"""
configure some specific defaults for the app
"""
app.config["MONGO_DBNAME"] = "test"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MONGOALCHEMY_DATABASE'] = 'test'
"""
start db connector
"""
mongo = PyMongo(app)

import FlaskWebProject1.views
import FlaskWebProject1.dbHelper
