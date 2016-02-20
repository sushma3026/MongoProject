'''
Created on 25 Nov 2015

@author: osboxes
'''
from pymongo import MongoClient
from bson.objectid import ObjectId
import re



connection = MongoClient("mongodb://127.0.0.1:27017/")
db = connection.users
tweets = db.tweets

# Function definition is here
def searchbyUserName(userName):
    "This changes a passed list into this function"
    userName= ".*" + userName + ".*";
    searchresult = tweets.find({"fromUserName": {"$regex": userName,"$options":"-i"}});
    return searchresult;
    
   
   
   
# Function definition is here
def searchbyuserText(text):
    "This changes a passed list into this function"
    
    searchresult = tweets.find({"text": {"$regex": text,"$options":"-i"}});
    return searchresult;      

def searchbydate(userdate, userSpecification):
    if userSpecification == 'gt':
        searchresult = tweets.find({"createdAt" :{'$gt':userdate}});
        return searchresult;
    elif userSpecification == 'lt':
        searchresult = tweets.find({"createdAt" :{'$lt':userdate}});
        return searchresult;
    elif userSpecification == 'eq':
        searchresult = tweets.find({"createdAt" :{'$eq':userdate}});
        return searchresult;
    else:
        print("Please enter a valid choice")

def commentingMethod(userid, userComment):
    commentedResult = db.tweets.update({"_id":ObjectId(userid)}, 
                     {'$set' : {'user_comment' : userComment }})
    aftercommented = db.tweets.find_one({'_id': ObjectId(userid) })
    print (aftercommented)
    return commentedResult;
    
# Now you can call changeme function


records ={}
userName = raw_input('Enter user name for search please!');
userText = ".*" + userName+ ".*";
numberofRecords= tweets.find({'fromUserName': {'$regex': userName}}).count();
if (numberofRecords !=0):
    records = searchbyUserName(userName);
    for mydocument in records:
        print (mydocument)
else:
        print('There is no records with this name, try again please')



records ={}
userText = raw_input('Enter the text for search please!');
userText = ".*" + userText+ ".*";
numberofRecords= tweets.find({'text': {'$regex': userText}}).count();
if (numberofRecords !=0):
    records = searchbyuserText(userText);
    for mydocument in records:
        print (mydocument)
else:
        print('There is no records with this text, try again please')
        
records ={}
userdate = raw_input('Enter the full date for search like this format: '+'Tue, 30 Oct 2012 23:26:45, please!');
userdate = userdate + ' +0000';
print('Please specify your research regarding the time')
print('for greater than this time enter '+'gt')
print('for less than this time enter '+'lt')
print('for equal this time enter '+'eq')
userSpecification = raw_input('Enter here please your choice: ');
if userSpecification == 'gt':
    numberofRecords= tweets.find({"createdAt" : {'$gt': userdate}}).count();
    if (numberofRecords !=0):
        records = searchbydate(userdate,userSpecification);
    for mydocument in records:
        print (mydocument)
elif userSpecification == 'lt':
    numberofRecords= tweets.find({"createdAt" : {'$lt': userdate}}).count();
    if (numberofRecords !=0):
        records = searchbydate(userdate,userSpecification);
    for mydocument in records:
        print (mydocument)
elif userSpecification == 'eq':
    numberofRecords= tweets.find({"createdAt" : {'$eq': userdate}}).count();
    if (numberofRecords !=0):
        records = searchbydate(userdate,userSpecification);
    for mydocument in records:
        print (mydocument)
    
else:
        print('There is no records with this date, try again please')
        


userChoise = raw_input("Do you want to comments on this tweet")
if userChoise == 'yes':
    tweetId = raw_input('Please Enter tweetId ')
    result = tweets.find({'_id': ObjectId(tweetId) }).count();
    if(result !=0):
        userComment = raw_input('Please Enter your comments here ')
        commentedResult = commentingMethod(tweetId, userComment);
        print(commentedResult)
    else:
        print("There is no such document!!")
else:
        print ("Good Bye, See you later")      
     

#  to MongoDB database
connection.close()