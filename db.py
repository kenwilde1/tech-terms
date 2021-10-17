from flask import Flask
from flask_pymongo import pymongo

client = pymongo.MongoClient(
    "mongodb+srv://root:Beverton0!@cluster0.o3rjb.mongodb.net/tech-jargon?retryWrites=true&w=majority")
db = client.get_database('tech-jargon')
user_collection = pymongo.collection.Collection(db, 'user_collection')
term_collection = pymongo.collection.Collection(db, 'term_collection')
