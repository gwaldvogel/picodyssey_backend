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
    res = requests.post('http://127.0.0.1:80/addUser', json=people)
    if res.ok:
        print res.json()
    
 

    