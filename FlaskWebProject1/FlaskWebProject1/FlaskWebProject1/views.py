"""
Routes and views for the flask application.
"""

"""
imports from system
"""
from datetime import datetime
import logging 
import random
import numpy as np
import json 

"""
project imports
"""
from FlaskWebProject1 import app,collectionUsers,collectionPlaces,db
from FlaskWebProject1 import dbHelper


"""
imports for flask
"""
from flask import render_template,jsonify
from flask import Flask, request, redirect, url_for, send_from_directory
from bson import ObjectId
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
class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)
"""



def convertDataType(value,refValue):
    if value == "place" or value =="user":
        return str(value)
    if refValue == "int":
        return int(value)
    if refValue == "uint":
        return np.uint64(value)
    if refValue == "long": 
        return np.long(value)
    if refValue == "float":
        return float(value)
    if refValue == "complex":
        return complex(value)
    if refValue == "string":
        return str(value)
    if refValue == "date":
        return str(value)
    else:
#        logging.warning('convertDataType: can not decode input value')  
        return 0

def recReadJsonList(valueList,refList):
    retList =[]
    for index, element in enumerate(valueList):
        if isinstance (element,list):
            recReadJsonList(element,refList[index],refList[index])
        ret = convertDataType(valueList[index],refList[index])
        retList.append(ret)
    return retList

def readIncommingJson(file,refFile):
    retDict ={}
    if (file["type"] == "user") & (refFile["type"] == "user"):
        keys = file.keys()
        for keys in file:
            if file[keys] == list:
                recReadJsonList(file[keys],refFile[keys])
            retDict[keys] = convertDataType(file[keys],refFile[keys])
#        logging.info('readIncommingJson: decoce user json')
        return retDict
          
    if (file["type"] == "place") & (refFile["type"] == "place"):
        keys = file.keys()
        for keys in file:
            if isinstance (file[keys],list):
                tmpList = refFile[keys]
                retDict[keys] = recReadJsonList(file[keys],tmpList)
            retDict[keys] = convertDataType(file[keys],refFile[keys])
#        logging.info('readIncommingJson: decoce place json')
        return retDict
        
    else:
#        logging.warning('readIncommingJson: can not decode input json file')  
        return -1   

"""
default sites for mongodb
"""
@app.route('/')
@app.route('/home')
def home():
    """Renders the home page.""" 
    #test script for read ref json format
    """
    collect = db.collection_names(include_system_collections=False)
    Data = json.loads(open("C://git//hackathon216//picodyssey_backend//FlaskWebProject1//FlaskWebProject1//FlaskWebProject1//place.json").read())
    print (json.dumps(Data,indent=4, sort_keys=True))
    realData = json.loads(open("C://git//hackathon216//picodyssey_backend//FlaskWebProject1//FlaskWebProject1//FlaskWebProject1//place2.json").read())    
    print (json.dumps(realData,indent=4, sort_keys=True))

    incommingData = readIncommingJson(realData,Data)


    User = json.loads(open("C://git//hackathon216//picodyssey_backend//FlaskWebProject1//FlaskWebProject1//FlaskWebProject1//user.json").read())
    print (json.dumps(User,indent=4, sort_keys=True))
    realUser = json.loads(open("C://git//hackathon216//picodyssey_backend//FlaskWebProject1//FlaskWebProject1//FlaskWebProject1//user2.json").read())    
    print (json.dumps(realUser,indent=4, sort_keys=True))

    incommingUser = readIncommingJson(realUser,User)

    collectionUsers.insert(incommingUser)
    collectionPlaces.insert(incommingData)
    """
    return render_template('Hello.html')

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
    user = collectionUsers.find_one_or_404({'uuid': username})
    user.pop("_id")
    return flask.jsonify(**user)
    

"""
add new user to mongodb get uuid
"""
@app.route('/newUser', methods=['GET', 'POST'])
def addUserProfile(username):
    content = request.get_json(silent=True)
    print(content)
    logging.debug("get /newUser/<username>")
    mongo.db.users.insert_one(content)
    
"""
add new user to mongodb get uuid
"""
@app.route('/addPlace/<uuuid_user>', methods=['GET', 'POST'])
def addPlace(username):
    content = request.get_json(silent=True)
    print(content)
    logging.debug("get /newUser/<username>")
    mongo.db.users.insert_one(content)    

"""
get place by uuid 
"""
@app.route('/getPlace/<placename>')
def getPlaceByUuid(placename):
    logging.debug("get /getPlace/<placename> ")
    place = collectionPlaces.find_one_or_404({'placeId': placename})
    place.pop("_id")
    return jsonify(**place)
    
    
"""
get random place from mongodb ignore user places  
"""
@app.route('/getRandPlace')
def getRandPlace():
    logging.debug("get /getRandPlace ")
    container = mongo.db.places.find({"type": "place"})
    


"""
get random place from mongodb ignore user places  
"""
@app.route('/get3RandPlaces')
def get3RandPlace():
    logging.debug("get /get3RandPlaces ")
    containerPlaces = mongo.db.places.find({'type': "place"})
    retList = []
    i = 0
    for i in range(0,3):
        randPlaceIDs = random.randint(0,len(containerPlaces))
        retList.append(containerPlaces(randPlaceIDs))
    return Flask.jsonify(**retList)


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)
