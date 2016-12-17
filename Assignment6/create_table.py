#!/usr/bin/env python

'''
Read data from groceries.csv and populates the mongodb
database. 
prints the number of rows read
'''

# Imports
from os import path
import codecs
from pymongo import MongoClient

conn = MongoClient()
conn.drop_database('ir_mongo')
db = conn.ir_mongo

count = 0 
with codecs.open('data/groceries.csv', encoding='latin2') as data:
	for line in data:
		count += 1
		data_line = sorted(line.strip().split(','))
		dict_mongo = {}
		dict_mongo['content'] = data_line
		db.corpus.insert(dict_mongo)

print "Inserted Records ", count
