# Airline Sentiment


A sentiment analysis job about the problems of each major U.S. airline. Twitter data was scraped from February of 2015 and contributors were asked to first classify positive, negative, and neutral tweets, followed by categorizing negative reasons (such as "late flight" or "rude service").

##Requirements: 

1. MongoDB 3.0
2. python 2.7.10
3. pymongo 3.2.0
4. Django 1.5.11

##Instructions: 

##Installation of Linux:

download linux : http://kelvin.ist.rit.edu/~mjmics

##follow below commands to install MongoDB: 

cd ~/Downloads
tar xvzf mongo...tgz
cd ~/Downloads/mongo.../bin
sudo cp -p * /usr/local/bin
echo $PATH
echo $SHELL

NOTE: /usr/local/bin/ is in your path


##Importing Dataset into MongoDB:

1. Terminal 1 -> Type mongod to start the server
2. Terminal 2 -> Type mongo to make the client connect to server.

In this server shell, type "mongoimport --db users --collection airline --type csv --headerline --file /Desktop/airline.csv"  to import dataset. 
Hint: make the file path as same as where the file is.


##Install pymongo

1. pip install pymongo
2. sudo apt-get install build-essential python-dev
3. sudo apt-get install git
4. git clone git://github.com/mongodb/mongo-python-driver.git pymongo
5. cd pymongo
6. sudo python setup.py install
7. sudo python setup.py bdist_egg
8. pip install https://github.com/mongodb/mongo-python-driver/archive/3.1rc0.tar.gz

##open python shell

1.import pymongo
2.from pymongo import MongoClient

##Install Django 

1.sudo apt-get update
2.sudo apt-get install python-django

## Run the server

1. open the terminal
2. change directory to tweetone folder and locate manage.py
3. execute $python manage.py runserver
4. in the terminal window a link to localhost will be provided by the server, click on the link to get to the application

## Application usage

1. The landing page would be a welcome page where there would be a link 'Tweets!!!'.
2. Click on the 'Tweets!!!' to get to the search page.
3. You will be provided with a list search parameters such as search by username, text, sentiment and created at.
4. Once you provide a value for the search click on the button 'Search' to get all the documents.
5. If you want to display all the information for one of these documents click on the text link on the tweet.
6. It would take you to another page to display the information for the document. 
7. If you want to add comments, you are provided with a text area to add comments and click on the 'add comment' button.
8. The added comment gets updated to the document.
9. Click on 'back to search' link to go back the search.
 























