"""
import other modules 
"""
import numpy as np

"""
imports function
"""
import json 



"""
some helper functions
"""

#def readRefJsonFile(readData):
#    retDict = {}
#    readKeys = readData.keys()
#    for keys in readKeys:
#        if readData[keys] == list:
#            recReadJsonList(readData[keys])
#        retDict[keys] = getResponsiveDataType(readData[keys])
#    return retDict
#
#def recReadRefJsonList(list):
#    retList = []
#    for items in list:
#        if items == list:
#            recReadJsonList(items)
#        retList.append(getResponsiveDataType(items))
#    return retList
#                
#def getResponsiveDataType(value):
#    if value == "int":
#        return 10
#    if value == "long":
#        return 4294967552
#    if value == "float":
#        return 1.0
#    if value == "complex":
#        return 3.14j
#    if value == "string":
#        return "default"
#    else:
#        #logging.warning('getResponsiveDataType: can not decode input value')  
#        return 0


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
class user():
    def __init__(self,refJson,inComeData):
        self._userRefJson = refJson
        self.checkElement(inComeData)
        self._userData = readIncommingJson(inComeData)

    def getObjectAsBSON(self):
        if readIncommingJson(self._userData,self._userRefJson) != -1 :
            try:
                decodeData = json.dumps(self._userData, ensure_ascii=False)
            
            except:
                decodeData = json.dumps(self._userRefJson,ensure_ascii=False)
                #logging.warning('getObjectAsBSON: can not decode json to bson') 
        else:
            decodeData = json.dumps(self._userRefJson,ensure_ascii=False)

    def getKeysFromObject(self):
        return self._userData.keys()

    def checkElement(self,element):
        failure = True
        try:
            decodeData = json.dumps(element, ensure_ascii=False)
            failure = False
        except:
            failure = True
        return failure

    def addpendPlace(self,object):
        #get old data from db
        oldPlaces = self._userData["places"]
        oldNumOfPlaces = self._userData["numOfPlaces"]
        oldPlaces.append(object["user_id"])
        oldNumOfPlaces += 1
        #update the db oject
        self._userData["places"] = oldPlaces
        self._userData["numOfPlaces"] = oldNumOfPlaces

    def safeObject(self):
        #remove old object
        mongo.db.users.remove(self._userData["user_id"])
        mongo.db.users.insert(self.getObjectAsBSON(self._userData))




class place():
    def __init__(self,refJson,inComeData):
        self._placeRefJson = refJson
        self.checkElement(inComeData)
        self._userData = readIncommingJson(inComeData)

    def getObjectAsBSON(self):
        if readIncommingJson(self._placeData,self._placeRefJson) != -1 :
            try:
                decodeData = json.dumps(self._placeData, ensure_ascii=False)
            
            except:
                decodeData = json.dumps(self._placeRefJson,ensure_ascii=False)
                #logging.warning('getObjectAsBSON: can not decode json to bson') 
        else:
            decodeData = json.dumps(self._placeRefJson,ensure_ascii=False)
            
    def getKeysFromObject(self):
        return self._userData.keys()

    def checkElement(self,element):
        failure = True
        try:
            decodeData = json.dumps(element, ensure_ascii=False)
            failure = False 
        except:
            failure = True
        return failure
"""
