from pymongo import MongoClient
import os

mongo_client = None
db = None

def init_db(app):
    global mongo_client, db
    mongo_client = MongoClient(app.config['MONGO_URI'])
    db_name = app.config['MONGO_URI'].split('/')[-1].split('?')[0]
    if not db_name:
        db_name = 'project_manager'
    db = mongo_client[db_name]

def get_db():
    return db
