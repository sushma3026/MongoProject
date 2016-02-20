from django.shortcuts import render
from django.http import Http404
from django.core.exceptions import *
from bson.objectid import ObjectId


#importing logger function 

import logging
from django.db import connection

connection.use_debug_cursor = True  # Change to force_debug_cursor in django > 1.7
l = logging.getLogger('django.db.backends')
l.setLevel(logging.DEBUG)
l.addHandler(logging.StreamHandler())

# use pymongo to connect mongoDB

from pymongo import MongoClient
connection = MongoClient("mongodb://127.0.0.1:27017/")
l.info('Mongodb connected')
# use database Users
db = connection.users
# use collections airline from Users db
tweets = db.airline

#view for main page
def main(request):
	l.info('Requesting main page')
	return render(request, 'main.html')

# view for landing page
def index(request):
	l.info('Requesting index page')
	return render(request, 'index.html')

# view for search page
def search(request):
	if request.method == "POST":
		l.info('Requesting search page')
		# get search parameters from fields
		username = request.POST.get('namefield', None)
		text=request.POST.get('textfield',None)
		sentiment=request.POST.get('sentimentfield', None)
		createdat=request.POST.get('createdatfield', None)

		# replace empty string with .* for regex
		if text=="":
			text = ".*"
		else:
			text = ".*" + text + ".*"
		if username == "":
			username = ".*"
		else:
			username = ".*" + username + ".*"
		if sentiment == "":
			sentiment = ".*"
		if createdat =="":
			createdat = ".*"
		else:
			createdat = ".*" + createdat + ".*"

		

		try:
			# mongo query to find the results for search parameters
			items = tweets.find( { 
				'name' : {'$regex': username, '$options':'-i'}, 
				'text' : {'$regex': text, '$options':'-i'} ,
				'airline_sentiment' : {'$regex': sentiment, '$options':'-i'}, 
				'tweet_created' : {'$regex': createdat, '$options':'-i'}
				})
			
			l.info('rendering search results')
			return render(request, 'index.html',{
				'items': items
				})
		except Exception, e:
			l.error('Exception thrown')
			return HttpResponse("result not found")
		else:
			l.info('Rendering Empty page without results')
			return render(request, 'index.html',{
				'items': items
				})
			
# view for comments
def comments(request, id):	
	l.info('Requesting comments page')
	if request.method == "POST":
		l.info('Adding Comments')
		# get the user comment
		comment=request.POST.get('commentfield',None)
		# update comment to the existing document by id
		commentedResult = tweets.update({"_id":ObjectId(id)}, 
                     {'$set' : {'user_comment' : comment }})
    	item = tweets.find({'_id': ObjectId(id) })
    	l.info('Displaying updated document')
	return render(request, 'comments.html', {
		'item':item
		})



