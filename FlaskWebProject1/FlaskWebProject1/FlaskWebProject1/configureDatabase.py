# -*- coding: utf-8 -*-
"""
Created on Sat Jun 18 18:48:17 2016

@author: Stefan Blattmann
"""

import requests
import cv2
import os

#adding some users to the database


Ali= {
	"userId" : "2589",
	"name" : "Ali",
	"numberOfPlaces" : "0",
	"places" : "",
	"type" : "user"}


Memed = {
	"userId" : "3597",
	"name" : "Memed",
	"numberOfPlaces" : "0",
	"places" : "",
	"type" : "user"}

Sven = {
	"userId" : "5897",
	"name" : "Sven",
	"numberOfPlaces" : "0",
	"places" : "",
	"type" : "user"}

Hans = {
	"userId" : "4478",
	"name" : "Hans",
	"numberOfPlaces" : "0",
	"places" : "",
	"type" : "user"}
 
Lisa = {
	"userId" : "2259",
	"name" : "Lisa",
	"numberOfPlaces" : "0",
	"places" : "",
	"type" : "user"}
 
Anna = {
	"userId" : "9862",
	"name" : "Anna",
	"numberOfPlaces" : "0",
	"places" : "",
	"type" : "user"} 

names =  [Ali,Memed,Sven,Hans,Lisa,Anna]
for people in names:
    res = requests.post('http://192.168.0.104:80/addUser', json=people)
    if res.ok:
        print(res.json())
Hauptbahnhof = {
   "placeId" : "0815",
   "userId" : "4711",
   "date": "205",
   "name": "Hauptbahnhof",
   "geoN": ["20"],
   "geoE": ["40"],
   "image": "",
   "thumbnail": "0815_thumbnail.jpg",
   "rate": "4.5",
   "numberOfRates": "20",
   "description": "Hauptbahnhof Freiburg",
   "city": "Freiburg",
   "type" : "place"
}     
 
Hermann = {
   "placeId" : "2569",
   "userId" : "3597",
   "date": "205",
   "name": "Hermann Cafe",
   "geoN": ["20"],
   "geoE": ["40"],
   "image": "",
   "thumbnail": "2569_thumbnail.jpg",
   "rate": "4.5",
   "numberOfRates": "20",
   "description": "Cooles Cafe",
   "city": "Freiburg",
   "type" : "place"
}    
    
BlaueBrücke = {
   "placeId" : "7777",
   "userId" : "5897",
   "date": "205",
   "name": "BlaueBrücke",
   "geoN": ["20"],
   "geoE": ["40"],
   "image": "",
   "thumbnail": "7777_thumbnail.jpg",
   "rate": "4.5",
   "numberOfRates": "20",
   "description": "Blaue Brücke in  freiburg",
   "city": "Freiburg",
   "type" : "place"
}   

Theater = {
   "placeId" : "8888",
   "userId" : "4478",
   "date": "205",
   "name": "Theater",
   "geoN": ["20"],
   "geoE": ["40"],
   "image": "",
   "thumbnail": "8888_thumbnail.jpg",
   "rate": "4.5",
   "numberOfRates": "20",
   "description": "Theater Haus freiburg",
   "city": "Freiburg",
   "type" : "place"
}   

UniBib = {
   "placeId" : "8591",
   "userId" : "2259",
   "date": "205",
   "name": "UniBib",
   "geoN": ["20"],
   "geoE": ["40"],
   "image": "",
   "thumbnail": "8591_thumbnail.jpg",
   "rate": "4.5",
   "numberOfRates": "20",
   "description": "UniBib freiburg",
   "city": "Freiburg",
   "type" : "place"
}   

Bertholdsbrunnen = {
   "placeId" : "1382",
   "userId" : "9862",
   "date": "205",
   "name": "Bertholdsbrunnen",
   "geoN": ["20"],
   "geoE": ["40"],
   "image": "",
   "thumbnail": "1382_thumbnail.jpg",
   "rate": "4.5",
   "numberOfRates": "20",
   "description": "Bertholdsbrunnen freiburg",
   "city": "Freiburg",
   "type" : "place"
}          
"""    
Hauptbahnhof = {
   "placeId" : "0815",
   "userId" : "4711",
   "date": "205",
   "name": "Hauptbahnhof",
   "geoN": ["20"],
   "geoE": ["40"],
   "image": "WP_20160618_16_35_44_Pro_LI.jpg",
   "thumbnail": "",
   "rate": "4.5",
   "numberOfRates": "20",
   "description": "Hauptbahnhof Freiburg",
   "city": "Freiburg",
   "type" : "place"
}     
 
Hermann = {
   "placeId" : "2569",
   "userId" : "3597",
   "date": "205",
   "name": "Hermann Cafe",
   "geoN": ["20"],
   "geoE": ["40"],
   "image": "WP_20160618_16_36_12_Pro_LI.jpg",
   "thumbnail": "",
   "rate": "4.5",
   "numberOfRates": "20",
   "description": "Cooles Cafe",
   "city": "Freiburg",
   "type" : "place"
}    
    
BlaueBrücke = {
   "placeId" : "7777",
   "userId" : "5897",
   "date": "205",
   "name": "BlaueBrücke",
   "geoN": ["20"],
   "geoE": ["40"],
   "image": "WP_20160618_16_37_01_Pro_LI.jpg",
   "thumbnail": "",
   "rate": "4.5",
   "numberOfRates": "20",
   "description": "Blaue Brücke in  freiburg",
   "city": "Freiburg",
   "type" : "place"
}   

Theater = {
   "placeId" : "8888",
   "userId" : "4478",
   "date": "205",
   "name": "Theater",
   "geoN": ["20"],
   "geoE": ["40"],
   "image": "WP_20160618_16_42_06_Pro_LI.jpg",
   "thumbnail": "",
   "rate": "4.5",
   "numberOfRates": "20",
   "description": "Theater Haus freiburg",
   "city": "Freiburg",
   "type" : "place"
}   

UniBib = {
   "placeId" : "1382",
   "userId" : "2259",
   "date": "205",
   "name": "UniBib",
   "geoN": ["20"],
   "geoE": ["40"],
   "image": "WP_20160618_16_42_45_Pro_LI.jpg",
   "thumbnail": "",
   "rate": "4.5",
   "numberOfRates": "20",
   "description": "UniBib freiburg",
   "city": "Freiburg",
   "type" : "place"
}   

Bertholdsbrunnen = {
   "placeId" : "1382",
   "userId" : "9862",
   "date": "205",
   "name": "Bertholdsbrunnen",
   "geoN": ["20"],
   "geoE": ["40"],
   "image": "WP_20160618_16_45_53_Pro_LI.jpg",
   "thumbnail": "",
   "rate": "4.5",
   "numberOfRates": "20",
   "description": "Bertholdsbrunnen freiburg",
   "city": "Freiburg",
   "type" : "place"
}  
""" 
#os.chdir("C://data//uploads") 
places =  [Hauptbahnhof,Hermann,BlaueBrücke,Theater,UniBib,Bertholdsbrunnen]


for place in places:
    res = requests.post('http://192.168.0.104:80/addPlace', json=place)
    if res.ok:
        print(res.json())
        
"""
images = ["C:\data\images\WP_20160618_16_35_44_Pro_LI.jpg","C:\data\images\WP_20160618_16_36_12_Pro_LI.jpg","C:\data\images\WP_20160618_16_37_01_Pro_LI.jpg","C:\data\images\WP_20160618_16_42_06_Pro_LI.jpg","C:\data\images\WP_20160618_16_42_45_Pro_LI.jpg","C:\data\images\WP_20160618_16_45_53_Pro_LI.jpg"]    

for index,image in enumerate(images):
    files = {'upload_file': open(str(image),'r')}
    tmpUid= places[index]
    r = requests.post("http://192.168.0.104:80/uploadImage/"+str(tmpUid), files=files)

 
def resizeImage(placeId,filename):
	image = cv2.imread(str(filename))
	#calc the ratio
	r = 250.0 / image.shape[1]
	dim = (250, int(image.shape[0] * r))
	 
	# perform the actual resizing of the image
	resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
	tmp = placeId.get("placeId")
     
	cv2.imwrite(str(tmp)+"_thumbnail.jpg", resized)    

for index,image in enumerate(images):
    resizeImage(places[index],image)
"""    
    