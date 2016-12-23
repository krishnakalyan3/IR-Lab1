#!/usr/bin/env python

'''
Runs mapreduce from the groceries.csv files and inserts the mapreduce output
to mongodb database.
input [item1, item2, ...]
output ((item1,item2),count)
'''

from pymongo import MongoClient
from bson.code import Code

conn = MongoClient()
db = conn.ir_mongo
db.items_pair_count.drop()

mapper = Code('''
function(){
	for (var i = 0; i < this.content.length; i++ ){
		for (var j = 0; j < this.content.length; j++ ){

			if (i != j){
				emit({item1:this.content[i],item2:this.content[j]}, 1);
			}
		}
	}
}
''')

reducer = Code('''
function(key,values){
	var total = 0
	for (var i =0; i< values.length; i++){
	total += values[i];
	}
	return total;
}
''')

db.corpus.map_reduce(mapper,reducer, 'items_pair_count')
print "MapReduce Complete"
