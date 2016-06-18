# -*- coding: utf-8 -*-
"""
Created on Sat Jun 18 18:48:17 2016

@author: Stefan Blattmann
"""

import requests


#adding some users to the database


Ali= {
	"userId" : "2589",
	"name" : "Ali",
	"numberOfPlaces" : "1",
	"places" : "0815",
	"type" : "user"}


Memed = {
	"userId" : "3597",
	"name" : "Memed",
	"numberOfPlaces" : "1",
	"places" : "2569",
	"type" : "user"}

Sven = {
	"userId" : "5897",
	"name" : "Sven",
	"numberOfPlaces" : "1",
	"places" : "7777",
	"type" : "user"}

Hans = {
	"userId" : "4478",
	"name" : "Hans",
	"numberOfPlaces" : "1",
	"places" : "8888",
	"type" : "user"}
 
Lisa = {
	"userId" : "2259",
	"name" : "Lisa",
	"numberOfPlaces" : "1",
	"places" : "1382",
	"type" : "user"}
 
Anna = {
	"userId" : "9862",
	"name" : "Anna",
	"numberOfPlaces" : "1",
	"places" : "4690",
	"type" : "user"} 
 
names =  [Ali,Memed,Sven,Hans,Lisa,Anna]
for people in names:
    res = requests.post('http://localhost:80/addUser', json=people)
    if res.ok:
        print(res.json())

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
   "image": "hello.jpg",
   "thumbnail": "hello_thumbnail.jpg",
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
   "userId" : "2259",
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
places =  [UniBib,Theater,BlaueBrücke,Hermann,Hauptbahnhof,Bertholdsbrunnen]
for place in places:
    res = requests.post('http://localhost:80/addPlace', json=place)
    if res.ok:
        print(res.json())
