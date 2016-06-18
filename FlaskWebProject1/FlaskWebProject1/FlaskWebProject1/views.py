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
import cv2
import base64
import os

"""
project imports
"""
from FlaskWebProject1 import app,collectionUsers,collectionPlaces,db



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
defaultDir = os.curdir

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
thumbnail creation
"""


def resizeImage(placeId,filename):
        image = cv2.imread(str(filename))
        #calc the ratio
        r = 250.0 / image.shape[1]
        dim = (250, int(image.shape[0] * r))
         
        # perform the actual resizing of the image
        resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
        
        cv2.imwrite(str(placeId)+"_thumbnail.jpg", resized)
        return str(placeId)+"_thumbnail.jpg"


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
    user = collectionUsers.find_one_or_404({'userId': username})
    user.pop("_id")
    return jsonify(**user)
   
"""
get place by uuid 
"""
@app.route('/getPlace/<uuid_place>')
def getPlaceByUuid(uuid_place):
    logging.debug("get /getPlace/<placename> ")
    place = collectionPlaces.find_one_or_404({'placeId': uuid_place})
    place.pop("_id")
    return jsonify(**place)
      
"""
get random place from mongodb ignore user places  
"""
@app.route('/getPlaces')
def getPlaces():
    places = collectionPlaces.find({'type': "place"})
    logging.debug("get /getRandPlace ")
#    retList = {}
#    for index,place in enumerate(places):
#        retList.update({str(index):(place.get("placeId"))}) 
#   return jsonify(**retList)
    retList = []
    for place in places:
        retList.append(place.get("placeId")) 
    return jsonify({"allPlaces" : retList})
    
"""
get random place from mongodb ignore user places  
"""
@app.route('/getRandPlace')
def getRandPlaces():
    logging.debug("getRandPlaces/")
    containerPlaces = collectionPlaces.find({'type': "place"})
    randPlaceIDs = random.randint(0,(collectionPlaces.find({'type': "place"}).count()))
    tmpPlace = containerPlaces[randPlaceIDs]
    tmpPlace.pop("_id")
    os.chdir("C://data//uploads") 
    tmpPath = tmpPlace.get("thumbnail")
    imageStr = str(base64.b64encode(open(tmpPath, "rb").read()))
    tmpPlace.update({"image": imageStr})
    os.chdir(defaultDir)
    return jsonify(**tmpPlace) 
    

"""
get random place from mongodb ignore user places  
"""
@app.route('/getUserPlaces/<uuidUser>')
def getUserPlace(uuidUser):
    logging.debug("get /getUserPlaces/")
    user = collectionUsers.find({"userId":str(uuidUser)})
    #allPlaces = user.get("places")
    tmpList = []
    for items in user:
        if items.get("places") != "":
            tmpList.append(items.get("places"))
    if len(tmpList) > 1:
        idList = tmpList[0].split(':')
    else:
        idList = tmpList[0]
    return jsonify({"userPlaces" : idList})

"""
add new user to mongodb get uuid
"""
@app.route('/addUser', methods=['POST'])
def addUserProfile():
    content = request.get_json(silent=True)
    print(content)
    logging.debug("get /newUser/<username>")
    collectionUsers.insert(content)
    #return 'OK'
    
"""
add new user to mongodb get uuid
"""
@app.route('/addPlace', methods=['POST'])
def addPlace():
    content = request.get_json(silent=True)
    print(content)
    logging.debug("get /newUser/<username>")
    collectionPlaces.insert(content)    
    user = content.get("userId")
    userFound = collectionUsers.find_one_or_404({'userId': user})
    tempNumOfPlaces = userFound.get("numberOfPlaces")
    tempNumber = int(tempNumOfPlaces)
    tempNumber += 1
    userFound.pop("numberOfPlaces")
    userFound.update({"numberOfPlaces" : str(tempNumber)})
#    tmpList = []
#    for items in userFound:
#        tmpList.append(items.get("places"))   
    strPlaces = userFound.get("places")
    tmp = content.get("placeId")
    tmp2 = ":"+tmp
    idList = str(strPlaces)+str(tmp2)

    #remove old user
    tmpId = userFound.get("userId")
    collectionUsers.remove({'userId': str(tmpId)})  
    userFound.pop("places")
    userFound.update({"places" : str(idList)})
    print(userFound)
    collectionUsers.insert(userFound)  
    #return 'OK'

        
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/uploadImage/<uuidPlace>', methods=['GET', 'POST'])
def upload_file(uuidPlace):
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            #logging.info('upload_file: no file detect')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            #logging.info('upload_file: no file detect')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            tmpPath = resizeImage(uuidPlace,str(app.config['UPLOAD_FOLDER'])+filename)
            #update place thumbnail
            placeFound = collectionPlaces.find_one_or_404({'placeId': uuidPlace})
            placeFound.update({"thumbnail" : str(tmpPath)})
            """
            tmpId = placeFound.get("_id")
            collectionPlaces.remove({'_id': str(tmpId)})  
            collectionPlaces.insert(placeFound)
            userFound.update({"places" : str(idList)})
            print(userItem)
            collectionUsers.insert(userFound)  
            """
            #return 'OK'
          