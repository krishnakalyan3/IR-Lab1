#!/usr/bin/env python

'''
Read the mapreduce output from mongodb and calculates the assoiciation rules based
on the formulas described in the slides.
support (a -> b) = count(a,b)/count({})
confidence (a -> b) =  count(a,b)/count(a)
stores the output results to mongodb database and a raw csv file 
'''

from os import path
from pymongo import MongoClient
import csv
conn = MongoClient()
db = conn.ir_mongo

def support(xy_count, corpus_count):
	sup = xy_count/corpus_count 
	return sup

def confidence(xy_count,x_count):
	conf = xy_count/x_count
	return conf

items_count = db.items_count.find()
items_pair_count = db.items_pair_count.find()

corpus_count = db.corpus.count()

data_op = []
for i in items_count:
	x_name  = i['_id']['item']
	x_count = i['value']
	
	for j in db.items_pair_count.find({'_id.item1': x_name}):
		item1 = j['_id']['item1']
          	item2 = j['_id']['item2']
		pair_value = j['value']
		supp = support(pair_value,corpus_count)
		conf = confidence(pair_value,x_count)
		data_op.append([item1,item2,supp,conf])
	
print "Writing output to a file"
with open("rules.csv", "wb") as f:
    writer = csv.writer(f)
    writer.writerows(data_op)

print "Writing output to table"
for line in data_op:
	data = {}
	data['item1'] = line[0]
	data['item2'] = line[1]
	data['supp'] = line[2]
	data['conf'] = line[3]
	db.output.insert(data)
